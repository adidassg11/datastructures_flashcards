import sort_utils

def ask_questions():
    print('Please answer questions with a space-separated list of sort algos'
           ' e.g. timsort mergesort quicksort\nUse \'q\' or \'quit\' to exit\n')
    while 1:
        m, bo, ans = sort_utils.get_rand_perf_list()
        metric_readable = sort_utils.perf_metrics_translation[m]
        bool_or_complexity = str(bo) if type(bo) == bool else 'O(%s)' % bo
        print('What sorts have the following property: %s is %s? (ans: %s)' %
                (metric_readable, bool_or_complexity, ans))
        ans_list = raw_input().strip().split()
        if ans_list[0].lower() == 'q' or ans_list[0].lower() == 'quit':
            break

        print sort_utils.is_perf_list_correct(m, bo, ans_list)

