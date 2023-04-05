from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import GlobbingFilter
import os
import SM4_CFB

FILE_LIST=['SM4_CFB']

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    config.trace_filter = GlobbingFilter(include=[
        'SM4_CFB.*'
    ])
    for i in FILE_LIST:
        graphviz.output_file = 'graph\\'+i+'.png'
        with PyCallGraph(output=graphviz, config=config):
            getattr( SM4_CFB, 'main')()

