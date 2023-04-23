# 字典键不可重复，值可重复，元素是无序的
# 使用{}创建
scores = {'张三': 100, '李四': 99, '王五': 98}
print(scores)

# 使用dict()创建
Name1 = dict(name='张六', age='20')
print(Name1)

# 获取字典的元素
print(scores['张三'])  # 如果不存在则报错
print(scores.get('张三'))  # 如果不存在则显示 None

# 字典增加元素
scores['王八'] = 95
print(scores)

# 字典删减元素
del scores['张三']
print(scores)

# 字典清空元素
scores.clear()

# 获取所有键
scores = {'张三': 100, '李四': 99, '王五': 98}
keys = scores.keys()
print(keys)

# 获取所有值
values = scores.values()
print(values)

# 获取所有键值对
items = scores.items()
print(items)

# 字典元素的遍历
for item in scores:
    print(item)

# 字典生成式创建
items = ['Fruits', 'Books', 'Others']
prices = ['1', '2', '3']
d = {item.upper(): prices for item, prices in zip(items, prices)}
print(d)
