# 创建列表第一种方式
lst = ['a', '1', '2']

# 创建列表第二种方式
lst2 = list(['a', 'l', '2'])

# 索引
print(lst.index('a'))
print(lst.index('1'))
print(lst.index('2'))

print(lst[2])
print(lst[-3])

# 查询 列表名[start:stop:step]
# 从左到右 0 开始，从右到左 -1 开始
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lst3[1:4:1])

print(lst3[1:4:])  # 默认step为1
print(lst3[:4:1])  # 默认start为1
print(lst3[1::1])  # 默认stop为0

# 元素的判断 in、not in
# 元素的遍历 for in

# 元素增加
lst.append('a')  # 添加到列表末尾
print(lst)
lst.extend(lst2)  # 将另一个列表的元素添加到末尾
print(lst)
lst.insert(0, 1)  # 指定位置添加 0 位置添加 1
print(lst)

lst[1:] = lst3  # 切掉部分用另一个列表替换
print(lst)

# 元素删除
lst = ['a', '1', '2', '3']
lst.remove('2')  # 如果有重复，只删除第一个
print(lst)
lst.pop(1)  # 根据索引删除
print(lst)
lst.pop()  # 没有参数，删除末位
print(lst)
lst2.clear()  # 清空列表
del lst2  # 删除列表

# 元素修改
lst = ['a', '1', '2', '3']
lst[0] = 100
print(lst)
lst[1:3] = [4, 5, 6, 7, 8]
print(lst)

# 元素排序
lst = ['4', '1', '2', '3']
lst.sort()  # 升序
print(lst)
lst.sort(reverse=True)  # 降序
print(lst)
new_lst = sorted(lst)  # 产生一个新列表，不改变原列表
print(new_lst)

lst = ['4', '1', '2', '3']
desc_list = sorted(lst, reverse=True)  # 降序
print(lst)
print(desc_list)

# 列表生成式
lst = [i for i in range(1, 10)]
print(lst)
