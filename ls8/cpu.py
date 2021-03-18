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

    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
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

        running = True
        while running == True:
            # self.trace()
            # print("self.reg: ",self.reg)
            # print("ram: ", self.ram)

            # fetch
            cmd = self.ram[self.pc]
            op1 = self.ram[self.pc + 1]
            op2 = self.ram[self.pc + 2]

            # decode
            # LDI 0b10000010
            if cmd == 0b10000010:
                print("This is an LDI")
                print("Test run completed")
                running = False

            # HLT 0b00000001
            elif cmd == 0b00000001:
                print("Program halted")
                running = False

            else:
                # to print binary add :b
                print(f"I don't understand the command at ram[{self.pc}]: {self.ram[self.pc]:b}")
                running = False