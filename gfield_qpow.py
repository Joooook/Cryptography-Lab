from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
def add(a, b):
    return a ^ b


def sub(a, b):
    return a ^ b


def mul(a, b, poly):
    ans = 0
    while b > 0:
        if b & 0x01 == 0x01:
            ans = add(ans, a)
        a = a << 1
        a = mod(a, poly)
        b = b >> 1
    ans = mod(ans, poly)
    return ans


def mod(a, poly):
    if a & 0x100 == 0x100:
        a = sub(a, poly)
    a &= 0xff
    return a


def quick_pow(a, b, poly):
    ans = 1
    while b:
        if b & 1:
            ans = mul(ans, a, poly)
        a = mul(a, a, poly)
        b = b >> 1
    return ans

def main():
    a, n = input().split()
    a = int(a, 16)
    n = int(n)
    poly = 0x11b
    print('%02x' % quick_pow(a, n, poly))
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph/gfield_qpow.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()
