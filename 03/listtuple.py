# author: leisurexi
# date: 2021-01-11 23:25
# 列表和元组示例，列表和元素都是一个可以放置任意数据类型的有序集合

# 列表是动态的，长度大小不固定，可以随意地添加、删除或者改变元素
lists = [1, 2, 3, "hello"]
lists[2] = 20
lists.append(5)
print(f'列表添加和修改元素后: {lists}')
lists.remove(1)
print(f'列表删除元素后: {lists}')
# -1 代表最后一个元素，-2 代表倒数第二个元素以此类推
print(f'列表负数索引: {lists[-1]}')
# 切片包前不包后
print(f'列表切片: {lists[1:3]}')

# 元组是静态的，长度大小固定，无法增加、删除或者改变元素
tuple = (1, 2, 6)
# tuple[2] = 20  # 此处会抛出异常

# 给元组添加一个元素，实际上是创建了一个新的元祖，然后将原先的4个元素一次填充进去
tuple = tuple + (5,)
print(f'元组添加元素后: {tuple}')
print(f'元组负数索引: {tuple[-1]}')
# 切片包前不包后
print(f'元组切片: {tuple[1:3]}')
# 元组反转，reversed 函数返回一个倒转后的迭代器，用 list 函数转换为列表
print(f'元组反转后: {list(reversed(tuple))}')
# 返回排序好的新列表
print(f'元组排序后: {sorted(tuple)}')
print(tuple)

# 思考题：以下2中方式在效率上有什么区别？
'''
    区别主要在于list()是一个function call，Python的function call会创建stack，
    并且进行一系列参数检查的操作，比较expensive，反观[]是一个内置的C函数，可以直接被调用，因此效率高。
'''
# 创建空列表
# option A
empty_list = list()
print(empty_list.__sizeof__())
# option B
empty_list = []
print(empty_list.__sizeof__())
