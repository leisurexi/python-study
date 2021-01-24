# author: leisurexi
# date: 2021/1/24
# file name: garbage_collection.py
# Python 垃圾回收

import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f'{hint} memory used: {memory} MB')


def func():
    show_memory_info('initial')
    # global a
    a = [i for i in range(10000000)]
    show_memory_info('after a created')
    return a


if __name__ == '__main__':
    a = func()
    # func()
    show_memory_info('finished')
