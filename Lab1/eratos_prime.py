from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
def eratosthenes(n):
    primelist = [True] * (n + 1)
    primelist[0] = False
    primelist[1] = False
    for i in range(2, int((n + 1) ** 0.5) + 1):
        if primelist[i]:
            j = i * i
            while j <= n:
                primelist[j] = False
                j += i
    return [i for i in range(2, n + 1) if primelist[i]]


def main():
    n = int(input())
    print(' '.join(map(str, eratosthenes(n))))
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = '../graph/eratos_prime.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()