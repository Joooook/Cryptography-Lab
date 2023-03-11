from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import os
def Egcd(a, b):
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


def invmod(a, n):
    inv, _, _ = Egcd(a, n)
    return inv % n


def crt3(a, b):
    M = a[0] * a[1] * a[2]
    Mi = [M // i for i in a]
    t = [invmod(Mi[i], a[i]) for i in range(3)]
    ans = 0
    for i in range(3):
        ans += b[i] * t[i] * Mi[i]
    ans = ans + M * ((0 - ans) // M + 1)
    return ans


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(crt3(a, b))

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = os.path.basename(__file__)+'.png'
    with PyCallGraph(output=graphviz, config=config):
        main()
