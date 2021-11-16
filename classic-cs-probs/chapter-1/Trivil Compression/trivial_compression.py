class CompressedGene:
    def __init__(self, gene) -> None:
        self._compress(gene)

        def _compress(self, gene) -> None:
            self.bit_string = 1
            for nucleotide in gene.upper():
                self.bit_string <<= 2 #! shift left 2 bits
                if nucleotide == "A":
                    self.bit_string |= 0b00
                elif nucleotide == 'C':
                    self.bit_string |= 0b01
                elif nucleotide == 'G':
                    self.bit_string |= 0b10
                elif nucleotide == 'T':
                    self.bit_string |= 0b11
                else:
                    raise ValueError(f'Invaid neucliotide :{nucleotide}')
        
        def decompress(self)-> str:
            gene = ''
            for i in range(0, self.bit_string.bitlength() - 1, 2):
                bits = self.bit_string >> i & 0b11
                if bits == 0b00:    #A
                    gene += "A"
                elif bits == 0b01:  #C
                    gene += "C"
                elif bits == 0b10:  #G
                    gene += "G"
                elif bits == 0b11:  #T
                    gene += "T"
                else:
                    raise ValueError(f'Invalid bits: {bits}')
            return gene[::-1] # [::-1] reverses string by slicing backward