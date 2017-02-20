#!/usr/bin/python
'''
This is a project for studying datastructure performance
'''

import pprint
import random
import time
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

perf_metrics_translation = {
    'rt_best': 'runtime best case',
    'rt_avg': 'runtime average case',
    'rt_worst': 'runtime worst case',
    'mem_best': 'memory best case',
    'mem_avg': 'memory average case',
    'mem_worst': 'memory worst case',
    'stable': 'stability',
}

def debug(args, pretty=False):
    if pretty:
        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(sort_metrics)
    else:
        print(args)


sort_metrics = {metric:{} for metric in perf_metrics} # ex: {'nlogn': ['quicksort', 'mergesort'], 'n2': [...]}
print('sort_metrics: %s' % sort_metrics)
mem_comp = {}


def insert_into_dict(dname, algo_name, algo_data, metric_str):
    metric_data = algo_data[metric_str]
    if metric_data not in sort_metrics[metric_str]:
        sort_metrics[metric_str][metric_data] = []
    sort_metrics[metric_str][metric_data].append(algo_name)
    pass


def create_sort_metrics():
    for algo_name, algo_data in sort_algos.items():
        # classic case of writing the logic very explicitly then finding
        # commonality and making it generic
        for metric in perf_metrics:
            insert_into_dict(sort_metrics, algo_name, algo_data, metric)


def get_rand_perf_list():
    """ Get a random triple (metric, big_o, ans_list)
    """
    random.seed(int(time.time()))
    rand = random.randint(0, len(sort_metrics)-1)
    metric, metric_data = sort_metrics.items()[rand]

    rand = random.randint(0, len(metric_data)-1)
    big_o, ans_list = metric_data.items()[rand]

    return metric, big_o, ans_list


def is_perf_list_correct(metric=None, big_o=None, ans_list=None):
    """ Expects a space-separated list of sort algos
        e.g. 'timsort mergesort quicksort'
    """

    if metric is None or big_o is None or ans_list is None:
        raise Exception('Improper use of is_perf_list_correct()')

    '''
    print 'user response list: %s' % ans_list
    correct_response = sort_metrics[metric][big_o]
    print 'correct response: %s' % correct_response
    '''

    return sorted(ans_list) == sorted(sort_metrics[metric][big_o])

############ TODO THIS IS THE COMMAND LINE INTERFACE #########

def ask_questions():
    print('Please answer questions with a space-separated list of sort algos'
           ' e.g. timsort mergesort quicksort\nUse \'q\' or \'quit\' to exit\n')
    while 1:
        m, bo, ans = get_rand_perf_list()
        metric_readable = perf_metrics_translation[m]
        bool_or_complexity = str(bo) if type(bo) == bool else 'O(%s)' % bo
        print('What sorts have the following property: %s is %s? (ans: %s)' %
                (metric_readable, bool_or_complexity, ans))
        ans_list = raw_input().strip().split()
        if ans_list[0].lower() == 'q' or ans_list[0].lower() == 'quit':
            break

        print is_perf_list_correct(m, bo, ans_list)

############ END CLI #############


if __name__ == '__main__':
    create_sort_metrics()
    ask_questions()

