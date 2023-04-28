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
            lam=((Q[1]-P[1])/(Q[0]-P[0])) % self.p
        else :
            lam=((3*P[0]**2+self.a)/(2*P[1])) % self.p
        x=(lam**2-P[0]-Q[0]) %self.p
        y=(lam*(P[0]-x)-P[1]) %self.p
        return [x,y]

    def sub(self,P,Q):
        return self.add(P,[Q[0],-Q[1]])

    def mul(self,k,A):
        k1=k%self.p
        for _ in range(k1-1):
            res=self.add(A,A)
        return res

def main():
    a = int(input())
    b = int(input())
    p = int(input())
    A=list(map(int,input().split()))
    B = list(map(int, input().split()))
    k=int(input())
    EC=ECC(a,b,p)
    print(EC.add(A,B))
    print(EC.sub(A,B))
    print(EC.mul(k, A))
if __name__ == '__main__':
    main()
