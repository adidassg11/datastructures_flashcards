#!/usr/bin/python
'''
This is a project for studying datastructure performance
'''

import pprint
from sort_algos import sort_algos

perf_metrics = [
    'rt_best',
    'rt_avg',
    'rt_worst',
    'mem_best',
    'mem_avg',
    'mem_worst',
    'stable',
]

def debug(args, pretty=False):
    if pretty:
        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(rt_comp)
    else:
        print(args)

rt_comp = {metric:{} for metric in perf_metrics} # ex: {'nlogn': ['quicksort', 'mergesort'], 'n2': [...]}
print('rt_comp: %s' % rt_comp)
mem_comp = {}

def insert_into_dict(dname, algo_name, algo_data, metric_str):
    metric_data = algo_data[metric_str]
    if metric_data not in rt_comp[metric_str]:
        rt_comp[metric_str][metric_data] = []
    rt_comp[metric_str][metric_data].append(algo_name)
    pass

def create_rt_comp():
    for algo in sort_algos.items():
        # classic case of writing the logic very explicitly then finding
        # commonality and making it generic
        for metric in perf_metrics:
            insert_into_dict(rt_comp, algo[0], algo[1], metric)

    debug(rt_comp, True)

def create_mem_comp():
    pass

create_rt_comp()

