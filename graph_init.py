from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import GlobbingFilter
import os
import hill_attack

FILE_LIST=['hill_attack']

if __name__ == '__main__':
    config = Config()
    graphviz = GraphvizOutput()
    config.trace_filter = GlobbingFilter(include=[
        'hill_attack.*'
    ])
    for i in FILE_LIST:
        graphviz.output_file = 'graph\\'+i+'.png'
        with PyCallGraph(output=graphviz, config=config):
            getattr(hill_attack, 'main')()

