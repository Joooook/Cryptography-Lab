from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
def add(a, b):
    return a ^ b


def sub(a, b):
    return a ^ b


def mod(a, poly):
    if a & 0x100 == 0x100:
        a = sub(a, poly)
    a &= 0xff
    return a


def mul(a, b):
    ans = 0
    while b > 0:
        if b & 0x01 == 0x01:
            ans = add(ans, a)
        a = a << 1
        a = mod(a, poly=0x11b)  # poly是给定多项式
        b = b >> 1
    return ans


def div(a, b):
    t = a
    ans = 0
    la = len(bin(a)[2:])
    lb = len(bin(b)[2:])
    while a >= b:
        rec = la - lb
        a = a ^ (b << rec)
        ans = ans | (1 << rec)
        la = len(bin(a)[2:])
    r = sub(t, mul(ans, b))
    return ans, r

def main():
    a, op, b = input().split()
    a = int(a, 16)
    b = int(b, 16)
    if op == '+':
        print('%02x' % add(a, b))
    elif op == '-':
        print('%02x' % sub(a, b))
    elif op == '*':
        print('%02x' % mul(a, b))
    elif op == '/':
        print('%02x %02x' % div(a, b))
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph/gfield_arithmetic.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()
