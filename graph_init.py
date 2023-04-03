from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import GlobbingFilter
import os
import AES_expand

FILE_LIST=['AES_expand']

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    config.trace_filter = GlobbingFilter(include=[
        'AES_expand.*'
    ])
    for i in FILE_LIST:
        graphviz.output_file = 'graph\\'+i+'.png'
        with PyCallGraph(output=graphviz, config=config):
            getattr( AES_expand, 'main')()

