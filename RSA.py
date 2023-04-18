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
def quick_pow(a, b, N):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % N
        a = a * a % N
        b = b >> 1
    return ans
def CRT(A,M):
    N=1
    for i in M:
        N*=i
    ans=0
    for i in range(len(A)):
        ans+=A[i] * (N//M[i])*invmod(N//M[i],M[i])
    return ans%N
def RSA_encrypt(p,q,e,m):
    return quick_pow(m,e,p*q)

def RSA_decrypt(p,q,e,c):
    d=invmod(e,(p-1)*(q-1))
    return CRT([quick_pow(c,d%(p-1),p),quick_pow(c,d%(q-1),q)],[p,q])

def main():
    p=int(input())
    q=int(input())
    e=int(input())
    m=int(input())
    op=int(input())
    if op==0:
        print(RSA_decrypt(p,q,e,m))
    elif op==1:
        print(RSA_encrypt(p,q,e,m))
if __name__ == '__main__':
    main()