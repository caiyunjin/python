# 常用的数据类型

# 整数-int-1，十进制（默认）、二进制（0b）、八进制（0o）、十六进制（0x）
# 可以表示 整数、负数、0
print('十进制', 1)
print('二进制', 0b10101111)
print('八进制', 0o175)
print('十六进制', 0x1EA)

# 浮点数-float-3.1415
from decimal import Decimal

n1 = 1.1
n2 = 2.2
print(n1 + n2)
print(Decimal("1.1") + Decimal("2.2"))

# 布尔类型-True(1)-False(0)
n1 = True
n2 = False
print(n1 + 1)
print(n2 + 1)

# 字符串类型
str1 = '哈哈'
str2 = '哈哈'
str3 = """哈
哈"""
str4 = '''哈
哈'''

print(str1)
print(str2)
print(str3)
print(str4)

# 类型转换 str() int() float()
name = '蔡佳诺'
age = 6

print('我叫' + name + ',' + '今年' + str(age) + '岁')
