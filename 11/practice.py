# author: leisurexi
# date: 2021-01-16 16:16
# 这种继承方式，叫做菱形继承，BC 继承了 A，然后 D 继承了 BC，创造一个 D 的对象。那么，构造函数调用顺序又是怎样的呢？


class A:
    def __init__(self):
        print('A init')


class B(A):
    def __init__(self):
        print('B init')
        super().__init__()


class C(A):
    def __init__(self):
        print('C init')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D init')
        super().__init__()


if __name__ == '__main__':
    d = D()
