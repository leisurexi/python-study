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
    list_1 = [i for i in range(1000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(1000000))
    show_memory_info('after generator initated')
    print(sum(list_2))
    show_memory_info('after sum called')


def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1


gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print(f'next_1 = {next_1}, next_3 = {next_3}')
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)


def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


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

    # test_iterator()
    # test_generator()

    # get_sum(8)

    print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))
    print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))