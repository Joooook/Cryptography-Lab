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

def main():
    a, b, c = map(int, input().split())
    print(quick_pow(a, b, c))
if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph/quick_pow.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()