# author: leisurexi
# date: 2021/1/24
# file name: circular_reference.py
# Python 循环引用

import os
import psutil
import gc


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f'{hint} memory used: {memory} MB')


def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)


if __name__ == '__main__':
    func()
    gc.collect()
    show_memory_info('finished')
