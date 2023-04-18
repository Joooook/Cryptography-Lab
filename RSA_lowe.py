import gmpy2
def Egcd(a, b):
    c = a
    d = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while c % d != 0:
        gcd = c % d
        q = c // d
        c = d
        d = gcd
        ppx = s0 - s1 * q
        s0 = s1
        s1 = ppx
        ppy = t0 - t1 * q
        t0 = t1
        t1 = ppy
    gcd = d
    return ppx, ppy, gcd


def invmod(a, n):
    inv, _, _ = Egcd(a, n)
    return inv % n

def CRT(A,M):
    N=1
    for i in M:
        N*=i
    ans=0
    for i in range(len(A)):
        ans+=A[i] * (N//M[i])*invmod(N//M[i],M[i])
    return ans%N
def low_e(C,N,e):
    x=CRT(C,N)
    return gmpy2.iroot(x, e)[0]

def main():
    n=int(input())
    e=int(input())
    C=[]
    N=[]
    for i in range(n):
        C.append(int(input()))
        N.append(int(input()))
    print(low_e(C,N,e))
if __name__ == '__main__':
    main()