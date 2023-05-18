def matrix_decrypt(n, key,s):
    m = [''] * len(s)
    gap = len(s) // n
    for i in range(len(s)):
        m[key.find(str(i//gap+1))+(i%gap)*n] = s[i]
    return ''.join(m)


def matrix_encrypt(n, key,s):
    c=['']*len(s)
    gap=len(s)//n
    for i in range(len(s)):
        c[(int(key[i%n])-1)*gap+i//n]=s[i]
    return ''.join(c)


def main():
    n=int(input())
    key = input().strip()
    s = input().strip()
    op = int(input())
    if op == 0:
        print(matrix_decrypt(n, key,s))
    elif op == 1:
        print(matrix_encrypt(n, key,s))
