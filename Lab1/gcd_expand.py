import random
from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

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
    if gcd < 0:
        x = -x
        y = -y
        gcd = -gcd
    gap_x = d // gcd
    gap_y = c // gcd
    x += ((0 - x) // gap_x + 1) * gap_x
    y -= ((0 - x) // gap_x + 1) * gap_y
    return x, y, gcd

def main():
    a, b = map(int, input().split())
    print(" ".join(map(str, Egcd(a, b))))
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = '../graph/gcd_expand.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()