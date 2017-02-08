# data pulled from https://en.wikipedia.org/wiki/Sorting_algorithm

# TODO: still need to add more here

sort_algos = {
    'quicksort': {
        'rt_best': 'nlogn',
        'rt_avg': 'nlogn',
        'rt_worst': 'n2',
        'mem_best': 'logn',
        'mem_avg': 'nlogn',
        'mem_worst': 'n',
        'stable': False,
    },
    'mergesort': {
        'rt_best': 'nlogn',
        'rt_avg': 'nlogn',
        'rt_worst': 'nlogn',
        'mem_best': 'n',
        'mem_avg': 'n',
        'mem_worst': 'n',
        'stable': True,
    },
    'heapsort': {
        'rt_best': 'nlogn',
        'rt_avg': 'nlogn',
        'rt_worst': 'nlogn',
        'mem_best': '1',
        'mem_avg': '1',
        'mem_worst': '1',
        'stable': False,
    },
    'insertionsort': {
        'rt_best': 'n',
        'rt_avg': 'n2',
        'rt_worst': 'n2',
        'mem_best': '1',
        'mem_avg': '1',
        'mem_worst': '1',
        'stable': True,
    },
    'introsort': {
        'rt_best': 'nlogn',
        'rt_avg': 'nlogn',
        'rt_worst': 'nlogn',
        'mem_best': 'logn',
        'mem_avg': 'logn',
        'mem_worst': 'logn',
        'stable': False,
    },
    'selectionsort': {
        'rt_best': 'n2',
        'rt_avg': 'n2',
        'rt_worst': 'n2',
        'mem_best': '1',
        'mem_avg': '1',
        'mem_worst': '1',
        'stable': False,
    },
    'timsort': {
        'rt_best': 'n',
        'rt_avg': 'nlogn',
        'rt_worst': 'nlogn',
        'mem_best': 'n',
        'mem_avg': 'n',
        'mem_worst': 'n',
        'stable': False,
    },
}