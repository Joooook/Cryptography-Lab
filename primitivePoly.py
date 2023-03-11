from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
def sub(a, b):
    return a ^ b


def add(a, b):
    return a ^ b


def mul(a, b):  # 有限域乘法
    ans = 0
    while b > 0:
        if b & 0x01 == 0x01:
            ans = add(ans, a)
        a = a << 1
        b = b >> 1
    return ans


def div(a, b):
    ans = 0
    la = len(bin(a)[2:])
    lb = len(bin(b)[2:])
    while la >= lb:
        rec = la - lb
        a = a ^ (b << rec)
        ans = ans | (1 << rec)
        la = len(bin(a)[2:])
    return ans, a


def gf_eratosthenes(n):  # 筛选n次不可约多项式
    max = 1 << (n + 1)
    primelist = [True] * max
    primelist[0] = False
    primelist[1] = False
    for i in range(2, 1 << (n // 2 + 1)):
        if primelist[i]:
            k = i
            j = mul(i, k)
            while j < max:
                primelist[j] = False
                k += 1
                j = mul(i, k)
    return [i for i in range(1, max) if primelist[i] and len(bin(i)[2:]) == n + 1]

def main():
    n = 8
    primepoly = gf_eratosthenes(n)
    m = 2 ** n - 1
    for i in primepoly:
        if div((1 << m) + 1, i)[1] == 0:
            primitive = True
            for q in range(n + 1, m):
                if div((1 << q) + 1, i)[1] == 0:
                    primitive = False
                    break
            if primitive:
                print(bin(i)[2:], end=' ')
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph/primitivePoly.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()
