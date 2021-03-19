"""CPU functionality."""

import sys

""" 
ls8.py runs this code:

    cpu = CPU()

    cpu.load()
    cpu.run()

"""
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        
        self.pc = 0

    # MAR = Memory Address Register
    # MDR = Memory Data Register

    # using "addr" and "data" for readability

    def ram_read(self, addr):
        return self.ram[addr]

    def ram_write(self, addr, data):
        self.ram[addr] = data

    def load(self):
        """Load a program into memory."""

        ram_addr = 0

        # New way: load from file
        # ---------------------------------
        # sys.argv[1] reads the user's cmd line input after this python filename
        # int("num_string", 2) converts binary string to int



        program = []
        program_file = open(sys.argv[1], 'r')

        for line in program_file:
            if line[0]=="#":
                continue
            
            elif line[0].isspace()==True:
                continue

            else:
                formatted_line = int(line[0:8],2)
                program.append(formatted_line)

        # print(program)
        program_file.close()



        # Old way: hardcoded program
        # ---------------------------------
        # For now, we've just hardcoded a program:



        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]


        # ---------------------------------

        for instruction in program:
            self.ram[ram_addr] = instruction
            ram_addr += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()


    def run(self):
        """Run the CPU."""

        # LDI | 82 | 0b10000010
        def run_ldi(self,operand_a,operand_b):

            # set operand_a (register #) to operand_b (integer)
            print("LDI")
            # print(f"LDI: set reg[{reg_num}]: {self.reg[reg_num]}")

            reg_num = operand_a
            reg_data = operand_b
            self.reg[reg_num] = reg_data

            self.pc += 3   

        # PRN | 71 | 0b01000111
        def run_prn(self,operand_a):
            # print the value at register[operand_a]
            # print("PRN")
            print(self.reg[operand_a])
            self.pc += 2

        # HLT | 1 | 0b00000001
        def run_hlt(self):
            # print("HALT")
            running = False

        dispatch = {
            # LDI | 82 | 0b10000010
            0b10000010: run_ldi,
            # PRN | 71 | 0b01000111
            # 0b01000111: run_prn,
            # ADD (alu) | 160 | 0b10100000
            # 0b10100000: run_add,
            # MUL (alu) | 162 | 0b10100010
            # 0b10100010: run_mul,
            # HLT | 1 | 0b00000001
            0b00000001: run_hlt,
        }

        cmd_list = dispatch.keys()

        running = True
        while running == True:

            # run this for debugging
            # self.trace()

            # fetch
            cmd_code = self.ram[self.pc]

            operand_a = self.ram[self.pc + 1]
            operand_b = self.ram[self.pc + 2]

            # # LDI | 82 | 0b10000010
            # if cmd_code == 0b10000010:
            #     # set operand_a (register #) to operand_b (integer)
            #     # print("LDI")
            #     reg_num = operand_a
            #     reg_data = operand_b

            #     self.reg[reg_num] = reg_data

            #     # print(f"LDI: set reg[{reg_num}]: {self.reg[reg_num]}")
            #     self.pc += 3

            # # PRN | 71 | 0b01000111
            # elif cmd_code == 0b01000111:
            #     # print the value at register[operand_a]
            #     # print("PRN")
            #     reg_num = operand_a
            #     print(self.reg[reg_num])
            #     self.pc += 2

            # # ADD (alu) | 0b10100000 | 160
            # elif cmd_code == 0b10100000:
            #     # print("ADD")
            #     self.alu("ADD",operand_a,operand_b)
            #     self.pc += 3

            # # MUL (alu) | 0b10100010 | 162
            # elif cmd_code == 0b10100010:
            #     # print("MUL")
            #     self.alu("MUL",operand_a,operand_b)
            #     self.pc += 3

            # # HLT | 1 | 0b00000001
            # elif cmd_code == 0b00000001:
            #     # print("HALT")
            #     running = False


            if cmd_code in cmd_list:
                print(cmd_code)
                dispatch[cmd_code](operand_a,operand_b)
                # running = False

            else:
                # to print binary add :b
                print(f"I don't understand the command at ram[{self.pc}]: {self.ram[self.pc]} | {self.ram[self.pc]:b}")
                print("Program exited")
                running = False
