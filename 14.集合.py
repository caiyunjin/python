# 集合是没有值的字典,无序,如果有重复元素则删除
# {}创建
t = {
    1,
    2,
    2,
    3,
    4,
    1,
}
print(t)

# set()创建
t = set(range(6))
print(t)

# 空集合
t = set()
print(t)

# 元素判断 in、not in
# 元素的增加
t.add(99)  # 增加一个
print(t)
t.update({54, 55})  # 增加至少一个
print(t)

# 元素的删除
t.remove(55)  # 一次删除一个元素，元素不存在抛出异常
print(t)
t.discard(1000)  # 一次删除一个元素，元素不存在不抛出异常
t.pop()  # 删除任意一个元素
print(t)
t.clear()  # 清空元素

# 集合间的关系 == 集合是否相等
s1 = {1, 2, 3, 4}
s2 = {2, 1, 3, 4}
print(s1 == s2)

# 子集
s1 = {1, 2, 3, 4}
s2 = {2, 1, 3, 4, 5}
print(s1.issubset(s2))

# 超集
print(s2.issuperset(s1))

# 交集判断
s1 = {1, 2, 3, 4, 6}
s2 = {2, 1, 3, 4, 5}
print(s1.isdisjoint(s2))  # 结果false，表示有交集

# 交集
print(s1.intersection(s2))
print(s1 & s2)

# 并集
print(s1.union(s2))
print(s1 | s2)

# 差集
print(s1.difference(s2))
print(s1 - s2)

# 对称差集
print(s1.symmetric_difference(s2))

# 元组不可变，所以没有生成式
