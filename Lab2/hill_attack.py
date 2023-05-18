import re


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


def matrix_det(n, mat):  # 求行列式
    det = 0
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    for i in range(n):
        tmp = []
        for j in range(n - 1):
            tmp.append([mat[j + 1][k] for k in range(n) if k != i])
        det += ((-1) ** i) * mat[0][i] * matrix_det(n - 1, tmp)
    return det % 26


def matrix_adj(n, mat):  # 求伴随矩阵
    adj = []
    for i in range(n):
        line = []
        for j in range(n):
            tmp = []
            for p in range(n):
                if p != j:
                    tmp.append([mat[p][q] for q in range(n) if q != i])
            det = matrix_det(n - 1, tmp)
            line.append(((-1) ** (i + j)) * det % 26)
        adj.append(line)
    return adj


def matrix_mul(a, b):
    ans = []
    for i in range(len(a)):
        line = []
        for j in range(len(b[0])):
            line.append(0)
        ans.append(line)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for m in range(len(a[0])):
                ans[i][j] = (ans[i][j] + a[i][m] * b[m][j]) % 26
    return ans


def matrix_inv(n, mat):  # 用伴随矩阵求矩阵逆
    invdet = invmod(matrix_det(n, mat), 26)  # 求行列式的逆
    adjmat = matrix_adj(n, mat)
    inv = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(adjmat[i][j] * invdet % 26)
        inv.append(line)
    return inv


def hill_attack(n, m, c):
    mList = re.findall(r'.{' + str(n) + '}', m)
    cList = re.findall(r'.{' + str(n) + '}', c)
    for i in range(len(mList) - n):
        mMat = []
        cMat = []
        for j in range(n):
            mMat.append([ord(k) - ord('a') for k in mList[i + j]])      #将明文和密文取出一部分拼接成n阶矩阵
            cMat.append([ord(k) - ord('a') for k in cList[i + j]])
        det = matrix_det(n, mMat)
        if det != 0 and det % 2 != 0 and det % 13 != 0:         #要考虑这个矩阵是否有逆矩阵
            key = matrix_mul(matrix_inv(n, mMat), cMat)
            return True, key
    return False, []


def main():
    n = int(input())
    m = input().strip()
    c = input().strip()
    key=hill_attack(n, m, c)[1]
    for i in key:
        for j in i:
            print(j,end=' ')
        print('')
