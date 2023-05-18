import re


def Egcd(a, b): # 扩展欧几里得算法
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


def invmod(a, n):           # 利用扩展欧几里得算法求逆元
    inv, _, _ = Egcd(a, n)
    return inv % n


def matrix_det(n, mat):  # 递归法求行列式
    det = 0
    if n == 2:          # 递归到二维矩阵的时候直接计算
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    for i in range(n):              # 矩阵第一行展开
        tmp = []
        for j in range(n - 1):      # 求取余子式
            for k in range(n):
                if k != i:          # 划去第1行和第i列
                    tmp.append([mat[j + 1][k]])
        det += ((-1) ** i) * mat[0][i] * matrix_det(n - 1, tmp) #矩阵按第一行展开求行列式
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


def matrix_mul(a, b): #矩阵模乘
    ans = []
    for i in range(len(a)): #初始化0矩阵
        line = []
        for j in range(len(b[0])):
            line.append(0)
        ans.append(line)
    for i in range(len(a)): #开始乘法运算
        for j in range(len(b[0])):
            for m in range(len(a[0])):
                ans[i][j] = (ans[i][j] + a[i][m] * b[m][j]) % 26
    return ans


def matrix_inv(n, mat):  # 用伴随矩阵求矩阵逆
    invdet = invmod(matrix_det(n, mat), 26)  # 求矩阵行列式的逆
    adjmat = matrix_adj(n, mat) # 求矩阵的伴随矩阵
    inv = []
    for i in range(n):      # 将矩阵行列式的逆模乘矩阵的伴随矩阵
        line=[]
        for j in range(n):
            line.append ( adjmat[i][j] * invdet % 26)
        inv.append(line)
    return inv


def hill_decrypt(n, key, s):    # hill密码解密
    c = re.findall(r'.{'+str(n)+'}', s) #先将字符串分成n个一组
    inv = matrix_inv(n, key)        # 求取密钥矩阵的逆矩阵
    m = ''
    for i in c: #遍历每组串
        for j in i:
            mat = [[ord(j) - ord('a') ]]  #将串变成矩阵
        for j in matrix_mul(mat, inv)[0]:
            m += ''.join([chr(j + ord('a')) ]) #将解密后的串拼接起来
    return m


def hill_encrypt(n, key, s):    #hill密码加密
    m = re.findall(r'.{'+str(n)+'}', s)  #先将字符串分成n个一组
    c = ''
    for i in m: #遍历每组串
        for j in i:
            mat = [[ord(j) - ord('a') ]] #将串变成矩阵
        for j in matrix_mul(mat, key)[0]:
            c += ''.join([chr(j + ord('a'))]) #将加密后的串拼接起来
    return c


def main():
    n = int(input())
    key = []
    for i in range(n):                  #输入key矩阵
        key.append(list(map(int, input().split())))
    s = input().strip()
    op = int(input())
    if op == 0:
        print(hill_decrypt(n, key, s))
    elif op == 1:
        print(hill_encrypt(n, key, s))
