# author: leisurexi
# date: 2021/1/24
# file name: thread_unsafe.py
# Python 线程不安全示例

import threading

n = 0


def foo():
    global n
    for i in range(50000):
        n += 1


if __name__ == '__main__':
    thread1 = threading.Thread(target=foo)
    thread2 = threading.Thread(target=foo)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(n)
