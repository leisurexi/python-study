# author: leisurexi
# date: 2021-01-17 20:08
# Python 对象的比较和拷贝

import copy


# 浅拷贝，是指重新分配一块内存，创建一个新的对象，里面的元素是原对象中子对象的引用。因此，如果原对象中的元素不可变，那倒无所谓；但如果元素可变，浅拷贝通常会带来一些副作用
def shallow_copy():
    l1 = [1, 2, 3]
    l2 = list(l1)
    l3 = l1[:]
    print('=======================浅拷贝=======================')
    print(l1 == l2)
    print(l1 is l2)
    print(l1 == l3)
    print(l1 is l3)
    s1 = set([1, 2, 3])
    s2 = set(s1)
    print(s1 == s2)
    print(s1 is s2)

    print('=======================copy 函数=======================')
    l4 = copy.copy(l1)
    print(l1 == l4)
    print(l1 is l4)

    # 对于元组，使用 tuple() 或者切片操作符':'不会创建一份浅拷贝，相反，它会返回一个指向相同元组的引用
    print('=======================元组拷贝=======================')
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t1 == t2)
    print(t1 is t2)


# 浅拷贝的副作用
def shallow_copy_side_effect():
    # 这里 l2 中的列表会改变，但是元组不会改变；因为列表是可变的，而元组是不可变的，修改元组会返回一个新的元组对象，l2并没有引用新的元组对象
    l1 = [[1, 2], (30, 40)]
    l2 = list(l1)
    print('=======================浅拷贝的副作用=======================')
    print(l1)
    print(l2)
    l1.append(100)
    l1[0].append(3)

    print(l1)
    print(l2)

    l1[1] += (50, 60)
    print(l1)
    print(l2)


# 深拷贝
def deep_copy():
    l1 = [[1, 2], (30, 40)]
    l2 = copy.deepcopy(l1)
    l1.append(100)
    l1[0].append(3)
    print('=======================深拷贝=======================')
    print(l1)
    print(l2)

    x = [1]
    x.append(x)
    y = copy.deepcopy(x)
    print(x)
    print(y)

    a = 1000
    b = copy.deepcopy(a)
    print(a is b)


if __name__ == '__main__':
    # Python 会缓存 -5 到 256 的一个整型数组，每次试图创建一个该范围内的数字都会从这个数组中返回引用，而不是重新开辟一块新的空间
    a = 10
    b = 10
    print(a == b)
    print(id(a))
    print(id(b))
    print(a is b)
    # 这里会相等是因为 Python 出于对性能的考虑，但凡是不可变对象，在同一个代码块中的对象，只有是值相同的对象，就不会重复创建，而是直接引用已经存在的对象
    c = 257
    d = 257
    print(c == d)
    print(id(c))
    print(id(d))
    print(c is d)

    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print(t1 == t2)

    t1[-1].append(5)
    print(t1 == t2)

    shallow_copy()

    shallow_copy_side_effect()

    deep_copy()
