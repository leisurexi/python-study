# author: leisurexi
# date: 2021/1/24
# file name: refcount.py
# Python 中的对象引用计数

import sys

if __name__ == '__main__':
    a = []
    b = a
    print(sys.getrefcount(a))
