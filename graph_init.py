from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import GlobbingFilter
import os
from Lab9 import SM3

FILE_LIST=['SM3']

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    config.trace_filter = GlobbingFilter(include=[
        'SM3.*'
    ])
    for i in FILE_LIST:
        graphviz.output_file = 'graph\\'+i+'.png'
        with PyCallGraph(output=graphviz, config=config):
            getattr(SM3, 'main')()

