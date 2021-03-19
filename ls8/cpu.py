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
        self.running = False
        
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

        # load from file
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
        self.running = True

        # HLT | 1 | 0b00000001
        def run_hlt(self):
            # Stop the program
            # print("HALT")
            self.running = False

        # TODO RET | 17 | 0b00010001
        def run_ret(self):
            # return from the subroutine
            # pop the value from the top of the stack
            # store the value in the pc (program counter)
            print("RET")

        # TODO PUSH | 69 | 0b1000101
        def run_push(self):
            # push a value to the stack
            # decrement the stack pointer (sp)
            # copy the value in reg[op_a] to ram[sp]
            print("PUSH")
            self.pc += 2

        # TODO POP | 70 | 0b01000110 
        def run_pop(self):
            # pop the value at the top of the stack
            # into reg[op_a]
            # increment stack pointer
            print("POP")
            self.pc += 2

        # PRN | 71 | 0b01000111
        def run_prn(self):
            # print the value at reg[op_a]
            # print("PRN")
            print(self.reg[operand_a])
            self.pc += 2

        # LDI | 82 | 0b10000010
        def run_ldi(self):
            # load integer(op_b) into reg[op_a]
            # print("LDI")
            reg_num = operand_a
            reg_data = operand_b
            self.reg[reg_num] = reg_data

            self.pc += 3   

        # ADD (alu) | 160 | 0b10100000 
        def run_add(self):
            # using the ALU: reg[op_a] += reg[op_b]
            # print("ADD")
            self.alu("ADD",operand_a,operand_b)
            self.pc += 3

        # MUL (alu) | 162 | 0b10100010
        def run_mul(self):
            # using the ALU: reg[op_a] *= reg[op_b]
            # print("MUL")
            self.alu("MUL",operand_a,operand_b)
            self.pc += 3

        dispatch = {
            # HLT | 1 | 0b00000001
            0b00000001: run_hlt,
            # RET | 17 | 0b00010001
            0b00010001: run_ret,
            # PUSH | 69 | 0b1000101
            0b1000101: run_push,
            # POP | 70 | 0b01000110 
            0b01000110: run_pop,
            # PRN | 71 | 0b01000111
            0b01000111: run_prn,
            # LDI | 82 | 0b10000010
            0b10000010: run_ldi,
            # ADD (alu) | 160 | 0b10100000
            0b10100000: run_add,
            # MUL (alu) | 162 | 0b10100010
            0b10100010: run_mul,
        }

        cmd_list = dispatch.keys()
        while self.running == True:
            # run this for debugging
            # self.trace()

            # fetch
            cmd_code = self.ram[self.pc]

            operand_a = self.ram[self.pc + 1]
            operand_b = self.ram[self.pc + 2]

            if cmd_code in cmd_list:
                # valid command, dispatch a function
                # print(cmd_code)
                cmd_run=dispatch[cmd_code](self)

            else:
                # command not recognized
                # to print binary add :b
                print(f"I don't understand the command at ram[{self.pc}]: {self.ram[self.pc]} | {self.ram[self.pc]:b}")
                print("Program exited")
                self.running = False
