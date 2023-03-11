def fence_decrypt(n,s):
    m=''
    fence=[]
    line=[]
    if len(s)%n==0:
        gap = (len(s) // n)
    else:
        gap = (len(s) // n) + 1
    for i in range(len(s)):
        line.append(s[i])
        if len(line)==gap:
            fence.append(line)
            line=[]
            if i == (len(s) % n) * gap - 1:
                gap -= 1
    for i in range(gap):
        for j in fence:
            m+=j[i]
    for i in range(len(s)%n):
        m+=fence[i][gap]
    return m


def fence_encrypt(n,s):
    gap = (len(s) // n) + 1
    c = [''] * (gap + 1) * n
    for i in range(len(s)):
        c[(i%n)*gap+i//n]=s[i]
    return ''.join(c)

def main():
    key = int(input().strip())
    s = input().strip()
    op = int(input())
    if op == 0:
        print(fence_decrypt(key, s))
    elif op == 1:
        print(fence_encrypt(key, s))
