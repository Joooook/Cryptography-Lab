import hashlib

import gmpy2

def sign(p,q,a,M,s,r):
    x=gmpy2.powmod(a,r,p)
    e=int(hashlib.sha1((M+str(x)).encode()).hexdigest(),16)
    y=(r+s*e) %q
    return e,y

def verify(p,q,a,M,v,e,y):
    x = (gmpy2.powmod(a, y, p) * gmpy2.powmod(v, e, p)) % p
    return e==int(hashlib.sha1((M+str(x)).encode()).hexdigest(),16)

def main():
    p = int(input())
    q = int(input())
    a = int(input())
    M = input()
    Mode = input()
    if Mode == 'Sign':
        s = int(input())
        r = int(input())
        R = sign(p,q,a,M,s,r)
        print(R[0], R[1])
    elif Mode == 'Vrfy':
        v=int(input())
        e,y = list(map(int,input().split()))
        print(verify(p,q,a,M,v,e,y))


if __name__ == '__main__':
    main()
