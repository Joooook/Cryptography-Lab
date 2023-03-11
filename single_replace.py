def sr_decrypt(s, t1, t2):
    c = ''
    for i in s:
        c += t1[t2.find(i)]
    return c


def sr_encrypt(s, t1, t2):
    m = ''
    for i in s:
        m += t2[t1.find(i)]
    return m


def main():
    t1 = input().strip()
    t2 = input().strip()
    s = input().strip()
    op = int(input())
    if op == 0:
        print(sr_decrypt(s, t1, t2))
    elif op == 1:
        print(sr_encrypt(s, t1, t2))
