# author: leisurexi
# date: 2021-01-12 22:45
# 字典和集合示例，字典是一组 key-value 对；而集合是一组无序的、唯一的元素集合

# 字典的创建
d1 = {'name': 'leisurexi', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'leisurexi', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'leisurexi'), ('age', 20), ('gender', 'male')])
d4 = dict(name='leisurexi', age=20, gender='male')
print(f'字典是否相等: {d1 == d2 == d3 == d4}')
d1['name'] = 'xidada'
print(f'字典是否相等: {d1 == d2 == d3 == d4}')
# print(f'访问不存在的元素: {d1["l"]}') # 此方式如果键不存在会抛出异常
print(f'访问不存在的元素，并提供默认值: {d1.get("l", "null")}')
print(f'判断某个键是否在字典内: {"name" in d1}')

d = {'b': 1, 'a': 2, 'c': 3}
# 根据字典键的升序排序
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
print(f'字典键根据升序排序: {d_sorted_by_key}')
# 根据字典值的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
print(f'字典值根据升序排序: {d_sorted_by_value}')

print("=====================================================================")

# 集合的创建
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(f'集合是否相等: {s1 == s2}')
print(f'判断某个键是否在集合内: {1 in s1}')
s = {3, 4, 2, 1}
print(f'集合元素进行升序排序: {sorted(s)}')
