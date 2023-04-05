
def BBS(length,p,q,s):
    N=p*q
    X=s**2 % N
    r=0
    for i in range(length):
        X=X**2 % N
        r=r | (X%2)<<i
    return r



def main():
    length=int(input())
    p=int(input())
    q = int(input())
    s=int(input())
    print(BBS(length,p,q,s))
if __name__ == '__main__':
    main()