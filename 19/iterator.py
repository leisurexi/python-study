# author: leisurexi
# date: 2021-01-20 22:43
# 迭代器和生成器

import os
import psutil


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f'{hint} memory used: {memory} MB')


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initated')
    print(sum(list_2))
    show_memory_info('after sum called')


if __name__ == '__main__':
    # params = [
    #     1234,
    #     '1234',
    #     [1, 2, 3, 4],
    #     set([1, 2, 3, 4]),
    #     {1: 1, 2: 2, 3: 3, 4: 4},
    #     (1, 2, 3, 4)
    # ]
    #
    # for param in params:
    #     print(f'{param} is iterable? {is_iterable(param)}')

    test_iterator()
    test_generator()

