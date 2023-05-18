import gmpy2
class ECC(object):
    def __init__(self,a,b,p,G):
        self.a=a
        self.b=b
        self.p=p
        self.O=[0,0]
        self.G=G
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

    def encrypt(self,M,k,pub):
        K=self.mul(k,pub)
        C1=self.mul(k,self.G)
        C2=self.add(K,M)
        return C1,C2
    def decrypt(self,C1,C2,pri):
        K=self.mul(pri,C1)
        M=self.sub(C2,K)
        return M

def main():
    p = int(input())
    a = int(input())
    b = int(input())
    G = list(map(int, input().split()))
    op = int(input())
    EC = ECC(a, b, p, G)
    if op==1:
        M= list(map(int, input().split()))
        k= int(input())
        pub=list(map(int, input().split()))
        C1,C2=EC.encrypt(M,k,pub)
        print(C1[0],C1[1])
        print(C2[0], C2[1])
    else:
        C1=list(map(int, input().split()))
        C2=list(map(int, input().split()))
        pri=int(input())
        res = EC.decrypt(C1,C2,pri)
        print(res[0], res[1])




if __name__ == '__main__':
    main()
