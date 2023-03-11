from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
def add(a, b):
    return a ^ b


def sub(a, b):
    return a ^ b


def mod(a, N):
    k = 1 << len(bin(N)[2:])-1
    if a & k == k:
        a = sub(a, N)
    a &= 0xff
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
    t = a
    ans = 0
    la = len(bin(a)[2:])
    lb = len(bin(b)[2:])
    while a>=b:
        rec = la - lb
        a = a ^ (b << rec)
        ans = ans | (1 << rec)
        la = len(bin(a)[2:])
    r = sub(t, mul(ans, b))
    return ans, r


def Egcd(c, d, poly):
    a=c
    b=d
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    q, _ = div(a, b)
    while sub(a, mul(q, b)) != 0:
        gcd = sub(a, mul(q, b))
        a = b
        b = gcd
        x = sub(s0, mul(s1, q))
        s0 = s1
        s1 = x
        y = sub(t0, mul(t1, q))
        t0 = t1
        t1 = y
        q, _ = div(a, b)
    gcd = b
    return x, y, gcd

def main():
    a, b = input().split()
    a = int(a, 16)
    b = int(b, 16)
    poly = 0x11b
    print('%02x %02x %02x' % Egcd(a, b, poly))
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph/gfield_egcd.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()

