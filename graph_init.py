from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import GlobbingFilter
import os
import DES_weak_key

FILE_LIST=['DES_weak_key']

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    config.trace_filter = GlobbingFilter(include=[
        'DES_weak_key.*'
    ])
    for i in FILE_LIST:
        graphviz.output_file = 'graph\\'+i+'.png'
        with PyCallGraph(output=graphviz, config=config):
            getattr(DES_weak_key, 'main')()

