# author: leisurexi
# date: 2021-01-16 13:07
'''
最后给你留一个思考题。给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，
输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表。
attributes = ['name', 'dob', 'gender']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male'],
    ['nancy', '2001-02-01', 'female']
]
# expected output:
[
    {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
    {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
    {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}
]

 你能分别用一行和多行条件循环语句，来实现这个功能吗？

'''


# 多行条件循环实现
def condition_loop(attributes, values):
    l = []
    for value in values:
        l.append(dict(zip(attributes, value)))
    return l


# 简便方式实现
def simple_way(attributes, values):
    return [dict(zip(attributes, value)) for value in values]



if __name__ == '__main__':
    attributes = ['name', 'dob', 'gender']
    values = [
        ['jason', '2000-01-01', 'male'],
        ['mike', '1999-01-01', 'male'],
        ['nancy', '2001-02-01', 'female']
    ]

    l = condition_loop(attributes, values)
    print(l)

    l = simple_way(attributes, values)
    print(l)