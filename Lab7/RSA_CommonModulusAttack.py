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
def quick_pow(a, b, N):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % N
        a = a * a % N
        b = b >> 1
    return ans%N
def invmod(a, n):
    inv, _, _ = Egcd(a, n)
    return inv % n

def CMA(E,C,N):
    s0,s1,_=Egcd(E[0],E[1])
    if s0<0:
        C[0]=invmod(C[0],N)
        s0=-s0
    if s1<0:
        C[1]=invmod(C[1],N)
        s1=-s1
    return (quick_pow(C[0], s0, N) * quick_pow(C[1], s1, N)) % N

def main():
    n=2
    E=[]
    C=[]
    for i in range(n):
        E.append(int(input()))
    for i in range(n):
        C.append(int(input()))
    N=int(input())
    print(CMA(E,C,N))

if __name__ == '__main__':
    main()

