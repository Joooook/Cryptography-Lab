import hashlib
import math

import gmpy2
class SM2(object):
    def __init__(self,a,b,p,G,Par):
        self.a=a
        self.b=b
        self.p=p
        self.O=[0,0]
        self.G=G
        self.Par=Par
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
    def H256(self,Z):
        return self.bytes2bit(hashlib.sha256(int.to_bytes(int(Z,2),math.ceil(len(Z)/8),'big')).hexdigest())
    def KDF(self,Z,klen):
        H=[]
        ct=1
        last=math.ceil(klen/256)-1
        for i in range(math.ceil(klen/256)):
            H.append(self.H256(Z+bin(ct)[2:].rjust(32,'0')))
            ct+=1
        if klen%256!=0:
            H[last]=H[last][:klen-256*math.floor(klen/256)]
        return ''.join(H)

    def field2bytes(self,a):
        t=self.Par
        l=t//4
        return hex(a)[2:].rjust(l,'0')

    def field2bit(self,a):
        return self.bytes2bit(self.field2bytes(a))
    def point2bytes(self, C):
        X1=self.field2bytes(C[0])
        Y1=self.field2bytes(C[1])
        return '04'+X1+Y1
    def bytes2field(self,a):
        return int(a,16)

    def bytes2point(self, C):
        C=C[2:]
        X = self.bytes2field(C[:self.Par//4])
        Y = self.bytes2field(C[self.Par//4:])
        return [X,Y]
    def bit2bytes(self,bits):
        return hex(int(bits,2))[2:].rjust(math.ceil(len(bits)/4),'0')
    def bytes2bit(self,B):
        return bin(int(B,16))[2:].rjust(len(B)*4,'0')
    def point2bit(self,C):
        return self.bytes2bit(self.point2bytes(C))
    def xor(self,a,b,klen):
        return bin(int(a,2)^int(b,2))[2:].rjust(klen,'0')
    def encrypt(self,M,k,pub):
        klen=len(M)
        C1=self.point2bit(self.mul(k, self.G))
        kpub=self.mul(k,pub)
        x2,y2=self.field2bit(kpub[0]),self.field2bit(kpub[1])
        t=self.KDF(x2+y2,klen)
        C2=self.xor(M,t,klen)
        C3=hashlib.sha256(int.to_bytes(int(x2+M+y2,2),math.ceil(len(x2+M+y2)/8),'big')).hexdigest()
        return self.bit2bytes(C1)+self.bit2bytes(C2)+C3
    def decrypt(self,C,pri):
        l = self.Par//4
        C1=self.bytes2point(C[:l*2+2])
        C2=self.bytes2bit(C[l*2+2:-64])
        klen = len(C2)
        priC1=self.mul(pri,C1)
        x2, y2 = self.field2bit(priC1[0]), self.field2bit(priC1[1])
        t=self.KDF(x2+y2,klen)
        M=self.bit2bytes(self.xor(C2,t,klen))
        return M


def main():
    p=int(input())
    a=int(input())
    b=int(input())
    G = list(map(int, input().split()))
    Par=int(input())
    op=int(input())
    SM=SM2(a,b,p,G,Par)
    if op==1:
        M= input()[2:]
        M=SM.bytes2bit(M)
        pub = list(map(int, input().split()))
        k=int(input())
        print('0x'+SM.encrypt(M,k,pub))
    else:
        C = input()[2:]
        pri = int(input())
        print('0x'+SM.decrypt(C,pri))




if __name__ == '__main__':
    main()