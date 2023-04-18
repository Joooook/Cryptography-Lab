def quick_pow(a, b, N):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % N
        a = a * a % N
        b = b >> 1
    return ans%N


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def Nfactor(e,d,n):
    for i in range(1,n):
        k=e*d-1
        while k%2==0:
            k = k // 2
            x=quick_pow(i,k,n)
            if x>1 and gcd(x-1,n)>1:
                return gcd(x-1,n),n//gcd(x-1,n)

def main():
    e=int(input())
    d=int(input())
    n=int(input())
    ans=Nfactor(e,d,n)
    print(min(ans))
    print(max(ans))
if __name__ == '__main__':
    main()