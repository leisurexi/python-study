# author: leisurexi
# date: 2021-01-16 14:49
# 匿名函数（lambda）示例

from functools import reduce

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x * 2, l)
    print(list(new_list))

    new_list = filter(lambda x: x % 2 == 0, l)
    print(list(new_list))

    new_list = reduce(lambda x, y: x * y, l)
    print(new_list)