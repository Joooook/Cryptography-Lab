import hashlib

import gmpy2


def sign(a, k, q, x, M):
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    S1 = gmpy2.powmod(a, k, q)
    S2 = (gmpy2.invert(k, q - 1) * (m - x * S1)) % (q - 1)
    return S1, S2


def verify(a, q, M, S1, S2, y):
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    V1 = gmpy2.powmod(a, m, q)
    V2 = (gmpy2.powmod(y, S1, q) * gmpy2.powmod(S1, S2, q)) % q
    return V1 == V2


def main():
    q = int(input())
    a = int(input())
    M = input()
    Mode = input()
    if Mode == 'Sign':
        x = int(input())
        k = int(input())
        S = sign(a, k, q, x, M)
        print(S[0], S[1])
    elif Mode == 'Vrfy':
        y = int(input())
        S = input().split()
        print(verify(a, q, M, int(S[0]), int(S[1]), y))


if __name__ == '__main__':
    main()
