class Device():
    
    def __init__(self, len_register, ip_idx = None) -> None:
        self.registers = [0 for i in range(len_register)]
        self.ip_idx = ip_idx

    def instruction_pointer(self):
        if self.ip_idx is not None:
            return self.registers[self.ip_idx]
        else:
            return None

    def increment_ip(self):
        self.registers[self.ip_idx] += 1

    def exec_instruction(self, opcode, A, B, C):
        match opcode:
            case 'addr':
                self.registers[C] = self.registers[A] + self.registers[B]
            case 'addi':
                self.registers[C] = self.registers[A] + B
            case 'mulr':
                self.registers[C] = self.registers[A] * self.registers[B]
            case 'muli':
                self.registers[C] = self.registers[A] * B
            case 'banr':
                self.registers[C] = self.registers[A] & self.registers[B]
            case 'bani':
                self.registers[C] = self.registers[A] & B
            case 'borr':
                self.registers[C] = self.registers[A] | self.registers[B]
            case 'bori':
                self.registers[C] = self.registers[A] | B
            case 'setr':
                self.registers[C] = self.registers[A]
            case 'seti':
                self.registers[C] = A
                
            case 'gtir':
                self.registers[C] = 1 if A > self.registers[B] else 0
            case 'gtri':
                self.registers[C] = 1 if self.registers[A] > B else 0
            case 'gtrr':
                self.registers[C] = 1 if self.registers[A] > self.registers[B] else 0
            
            case 'eqir':
                self.registers[C] = 1 if A == self.registers[B] else 0
            case 'eqri':
                self.registers[C] = 1 if self.registers[A] == B else 0
            case 'eqrr':
                self.registers[C] = 1 if self.registers[A] == self.registers[B] else 0

    def __repr__(self):
        return str(self.registers)