from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import os
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


def affine_encrypt(s, k, b):
    if k % 13 == 0 or k % 2 == 0:
        return 0, ''
    c = ''
    for i in s:
        c += chr(((ord(i) - ord('a')) * k + b) % 26 + ord('a'))
    return 1, c


def affine_decrypt(s, k, b):
    if k % 13 == 0 or k % 2 == 0:
        return 0, ''
    m = ''
    inv = invmod(k,26)
    for i in s:
        m += chr(((ord(i) - b - ord('a')) * inv) % 26 + ord('a'))
    return 1, m


def main():
    k, b = map(int, input().strip().split())
    s = input().strip()
    op = int(input())
    if op == 0:
        suc, ans = affine_decrypt(s, k, b)
        if suc:
            print(ans)
        else:
            print('invalid key')
    elif op == 1:
        suc, ans = affine_encrypt(s, k, b)
        if suc:
            print(ans)
        else:
            print('invalid key')
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    print(os.path.basename(__file__))
    graphviz.output_file = 'graph\\'+os.path.basename(__file__)+'.png'
    with PyCallGraph(output=graphviz, config=config):
        main()