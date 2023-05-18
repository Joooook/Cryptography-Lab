import gmpy2
def Egcd(c, d):
    a = c
    b = d
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while a % b != 0:
        gcd = a % b
        q = a // b
        a = b
        b = gcd
        x = s0 - s1 * q
        s0 = s1
        s1 = x
        y = t0 - t1 * q
        t0 = t1
        t1 = y
    gcd = b
    return x, y, gcd


def invmod(a, m):
    return Egcd(a, m)[0] % m


def continued_fraction_list(x, y):  # 求连分数表
    continued_fraction = []
    while y:
        continued_fraction.append(x // y)
        x, y = y, x % y
    return continued_fraction


def convergents(x, y):  # 求渐进分数
    A = continued_fraction_list(x, y)
    convergents_fraction = []
    for i in range(len(A)):#求解各项渐进分数
        k = A[i]
        d = 1
        for j in range(i-1,-1,-1):#递推向上
            k,d=A[j]*k+d,k
        convergents_fraction.append((k, d))
    return convergents_fraction


def solve(a, b, c):  # 解二次方程
    dlt = gmpy2.isqrt(b * b - 4 * a * c)
    x1, x2 = (-b + dlt) // (2 * a), (-b - dlt) // (2 * a)
    return x1, x2


def wiener_attack(e, n):
    for (k,d) in convergents(e, n):
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        p, q = solve(1, n - phi + 1, n)
        if p * q == n:
            p, q = abs(int(p)), abs(int(q))
            d = invmod(e, (p - 1) * (q - 1))
            if p > q:
                p, q = q, p
            return d, p, q


def main():
    e = int(input())
    n = int(input())
    d, p, q = wiener_attack(e, n)
    print(p)
    print(q)
    print(d)
if __name__ == '__main__':
    main()