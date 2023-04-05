class MT19937(object):
    def __init__(self,seed):
        self.MT=[0]*624
        self.index=0
        self.seed=seed
        self.initialize_generator()
    def initialize_generator(self):
        self.MT[0]=self.seed
        for i in range(1,624):
            self.MT[i]=(0x6c078965 * (self.MT[i-1]^self.MT[i-1]>>30)+i)&0xFFFFFFFF
    def extract_number(self):
        if self.index==0:
            self.generate_numbers()
        y=self.MT[self.index]
        y=y^ y>>11
        y = y ^ (y<<7&0x9d2c5680)
        y = y ^ (y<<15&0xefc60000)
        y = y ^ y>>18
        y=y&0xFFFFFFFF
        self.index=(self.index+1) %624
        return y
    def generate_numbers(self):
        for i in range(624):
            y=(self.MT[i] & 0x80000000)+(self.MT[(i+1)%624]&0x7FFFFFFF)
            self.MT[i]=self.MT[(i + 397) % 624] ^ (y>>1)
            if y%2!=0:
                self.MT[i]=self.MT[i]^0x9908b0df

def main():
    seed=int(input())
    mt=MT19937(seed)
    for i in range(20):
        print(mt.extract_number())
if __name__ == '__main__':
    main()
