"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # add self.ram
        self.ram = [0] * 256
        # 256 slots, leave one out so it can move =255

        # later will remove op codes, hardcoded for now
        # self.op = op

        # registers are lists 8 bytes long
        self.reg = [0] * 8

        # program counter
        self.pc = 0

    # read from ram
    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value

    def load(self):
        """Load a program into memory."""
        
        address = 0

        # For now, we've just hardcoded a program:

        # op codes - hard coded
        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000, # NOP - no operation
            0b00001000, # not listed?
            0b01000111, # PRN R0
            0b00000000, # NOP - no operation
            0b00000001, # HLT
        ]

        for instruction in program:
            # creating a ram address for each instruction
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        # alu is for mathematical operations
        # like a calculator

        # has op
        # has registers

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
        instruction_register = 0
        print("Test complete")