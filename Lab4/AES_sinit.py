def add(a, b):
    return a ^ b


def sub(a, b):
    return a ^ b


def mod(a, N):
    k = 1 << len(bin(N)[2:]) - 1
    if a & k == k:
        a = sub(a, N)
    return a


def mul(a, b):
    ans = 0
    while b > 0:
        if b & 0x01 == 0x01:
            ans = add(ans, a)
        a = a << 1
        a = mod(a, N=0x11b)  # poly是给定多项式
        b = b >> 1
    return ans


def div(a, b):
    ans = 0
    la = len(bin(a)[2:])
    lb = len(bin(b)[2:])
    while a >= b:
        rec = la - lb
        a = a ^ (b << rec)
        ans = ans | (1 << rec)
        la = len(bin(a)[2:])
    return ans, a


def Egcd(a, b, poly):
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while b != 0:
        q, gcd = div(a, b)
        a = b
        b = gcd
        x = sub(s0, mul(s1, q))
        s0 = s1
        s1 = x
        y = sub(t0, mul(t1, q))
        t0 = t1
        t1 = y
    gcd = a
    return s0, t0, gcd


def invmod(a, poly):
    return Egcd(a, poly, poly)[0]

def bit(byte,i):
    return (byte>>i)&1

def init_zero_matrix(l,r):
    mat=[]
    for i in range(l):
        line=[]
        for j in range(r):
            line.append(0)
        mat.append(line)
    return mat
def init_matrix(l,r):
    mat=[]
    for i in range(l):
        line=[]
        for j in range(r):
            line.append(i<<4|j)
        mat.append(line)
    return mat
def inv_element_matrix(mat):
    iEMat=[]
    for i in range(len(mat)):
        line=[]
        for j in range(len(mat[0])):
            line.append(invmod(mat[i][j],0x11b))
        iEMat.append(line)
    return iEMat
def sub_matrix(mat):
    sMat = []
    c=0x63
    for i in range(len(mat)):
        line = []
        for j in range(len(mat[0])):
            byte=mat[i][j]
            newByte=0
            for k in range(8):
                newByte=newByte | ( (bit(byte,k)^bit(byte,(k+4)%8)^bit(byte,(k+5)%8)^bit(byte,(k+6)%8)^bit(byte,(k+7)%8)^bit(c,k))<<k )
            line.append(newByte)
        sMat.append(line)
    return sMat
def inv_matrix(mat):
    iMat=init_zero_matrix(16,16)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            byte=mat[i][j]
            iMat[byte>>4][byte&0xF]=i<<4 | j
    return iMat

def output_matrix(mat):
    for i in mat:
        for j in i:
            print('0x' + hex(j)[2:].rjust(2, '0'), end=' ')
        print()
    return

def main():
    mat=init_matrix(16,16)
    output_matrix(mat)
    invmat=inv_element_matrix(mat)
    output_matrix(invmat)
    submat = sub_matrix(invmat)
    output_matrix(submat)
    invS = inv_matrix(submat)
    output_matrix(invS)

if __name__ == '__main__':
    main()