# 第一种写法
a1 = int(input('数字一'))
a2 = int(input('数字二'))
if a1 >= a2:
    print(a1, '大于等于', a2)
else:
    print(a1, '小于', a2)

# 第二种写法
a1 = int(input('数字一'))
a2 = int(input('数字二'))
print(str(a1) + '大于等于' + str(a2) if a1 >= a2 else str(a1) + '小于' + str(a2))

# pass，占位符
a1 = int(input('数字一'))
a2 = int(input('数字二'))
if a1 >= a2:
    print(a1, '大于等于', a2)
else:
    pass
