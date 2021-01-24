# author: leisurexi
# date: 2021/1/24
# file name: refcount.py
# Python 引用计数示例

import sys


def func(a):
    # 四次引用，a，Python 的函数调用栈，函数参数 和 getrefcount
    print(sys.getrefcount(a))


if __name__ == '__main__':
    a = []
    # 两次引用，一次来自 a，一次来自 getrefcount
    print(sys.getrefcount(a))
    func(a)
    # 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
    print(sys.getrefcount(a))
