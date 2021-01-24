# author: leisurexi
# date: 2021/1/24
# file name: multi_process_practice.py
# 练习题的多进程版本

import multiprocessing
import time


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    print(f'numbers: {numbers}')
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print(f'Calculation takes {end_time - start_time} seconds')


if __name__ == '__main__':
    main()
