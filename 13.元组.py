# 元组为不可变序列
# ()创建
t = ('1', '2', '3')
t = '1', '2', '3'
print(t)

t = ('1',)  # 如果只有一个元素要加 ,
print(t)

# tuple()创建
t = tuple(('1', '2', '3'))
print(t)

# 空元组创建
t = ()
t = tuple()

# 元组的遍历
t = ('1', '2', '3')
for i in t:
    print(i)
