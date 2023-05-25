import hashlib
import math
import SM3
import gmpy2
class SM2(object):
    def __init__(self,a,b,p,G,n):
        self.a=a
        self.b=b
        self.p=p
        self.O=[0,0]
        self.G=G
        self.n=n
    def add(self,P,Q):
        if P==self.O:
            return Q
        if Q==self.O:
            return P
        if P[0]==Q[0] and P[1]!=Q[1]:
            return self.O
        if P!=Q:
            lam=((Q[1]-P[1])*int(gmpy2.invert(Q[0]-P[0],self.p))) % self.p
        else :
            lam=((3*P[0]**2+self.a)*int(gmpy2.invert(2*P[1],self.p))) % self.p
        x=(lam**2-P[0]-Q[0]) %self.p
        y=(lam*(P[0]-x)-P[1]) %self.p
        return [x,y]

    def sub(self,P,Q):
        return self.add(P,[Q[0],-Q[1]])

    def mul(self,k,A):
        k1=bin(k%self.p)[2:]
        count=0
        res=self.O
        while count<len(k1):
            res = self.add(res, res)
            if k1[count]=='1':
                res = self.add(res, A)
            count+=1
        return res

    def transByte(self, a, p):
        t = math.ceil(math.log(p, 2))
        l = (t + 8 - 1) // 8
        return a.to_bytes(length=l, signed=False, byteorder='big')

    def gen_ZA(self,ID, P):
        entlen_a = len(ID) * 8
        entlen_a = entlen_a.to_bytes(length=2, byteorder='big')
        return SM3.sm3_digest(
            entlen_a + ID + self.transByte(self.a, self
        .p) + self.transByte(self
        .b, self.p) + self.transByte(self.G[0], self.p) + self.transByte(self.G[1], self.p) + self.transByte(
                P[0], self.p) + self.transByte(P[1], self.p))

    def xor(self,a,b,klen):
        return bin(int(a,2)^int(b,2))[2:].rjust(klen,'0')

    def sign(self,ID, m, d, K, P):
        m_ = self.gen_ZA(ID, P) + m
        e = SM3.sm3_digest(m_)
        e = int.from_bytes(e, byteorder='big')
        x1, y1 = self.mul(K,self.G)
        r = (e + x1) % self.n
        s = gmpy2.invert(1 + d, self.n) * (K - r * d) % self.n
        return r, s

    def verify(self,ID, m, r, s, P):
        if r > self.n - 1 or r < 1:
            return False
        if s > self.n - 1 or s < 1:
            return False
        m_ = self.gen_ZA(ID, P) + m
        e = SM3.sm3_digest(m_)
        e = int.from_bytes(e, byteorder='big', signed=False)
        t = (r + s) % self.n
        if t == 0:
            return False
        s_ = self.mul(s,self.G)
        t_ = self.mul(t,P)
        x1, y1 = self.add(s_,t_)
        r_ = (e + x1) % self.n
        return r_ == r

def main():
    p = int(input())
    a = int(input())
    b = int(input())
    G = list(map(int, input().split()))
    n = int(input())
    ID = input()
    P = list(map(int, input().split()))
    M = input()
    Mode = input()
    sm2sig=SM2(a,b,p,G,n)
    if Mode == 'Sign':
        d = int(input())
        K = int(input())
        r,s = sm2sig.sign(ID.encode(), M.encode(), d, K, P)
        print(r)
        print(s)
    elif Mode == 'Vrfy':
        r = int(input())
        s = int(input())
        print(sm2sig.verify(ID.encode(), M.encode(), r, s, P))



if __name__ == '__main__':
    main()