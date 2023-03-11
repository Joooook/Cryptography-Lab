import random
from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput



def quick_pow(a, b, N):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % N
        a = a * a % N
        b = b >> 1
    return ans


def millerRabinTest(n, iter_num):
    if n == 2:
        return True
    if n & 1 == 0 or n == 1:
        return False

    m = n - 1
    s = 0
    while m & 1 == 0:
        m = m >> 1
        s += 1
    for i in range(iter_num):
        b = quick_pow(random.randint(2, n - 1), m, n)
        if b == 1 or b == n - 1:
            continue
        for j in range(s - 1):
            b = quick_pow(b, 2, n)
            if b == n - 1:
                break
        else:
            return False
    return True

def main():
    if millerRabinTest(int(input()), 20):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph/miller_rabin.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()
