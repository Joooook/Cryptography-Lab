import gmpy2


class ECC(object):
    def __init__(self,a,b,p):
        self.a=a
        self.b=b
        self.p=p
        self.O=[0,0]

    def add(self,P,Q):
        if P==self.O:
            return Q
        if Q==self.O:
            return P
        if P[0]==Q[0] and P[1]!=Q[1]:
            return self.O
        if P!=Q:
            lam=((Q[1]-P[1])*gmpy2.invert(Q[0]-P[0],self.p)) % self.p
        else :
            lam=((3*P[0]**2+self.a)*gmpy2.invert(2*P[1],self.p)) % self.p
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

def main():
    p = int(input())
    a = int(input())
    b = int(input())
    A=list(map(int,input().split()))
    B = list(map(int, input().split()))
    k=int(input())
    EC=ECC(a,b,p)
    res=EC.add(A, B)
    print(res[0],res[1])
    res = EC.sub(A, B)
    print(res[0], res[1])
    res = EC.mul(k, A)
    print(res[0], res[1])
if __name__ == '__main__':
    main()
