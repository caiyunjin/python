# 算数运算符
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(1 // 1)  # 整除
print(1 % 1)  # 取余
print(1**1)  # 幂运算 1的1次方
print(9 // -4)  # 一正一负向下quzheng
print(9 % -4)  # 余数=被除数-除数*商
print(-9 % 4)

# 赋值运算符，从右到左
a = b = c = 1  # 链式赋值
a += 1  # a=a+1
a -= 1  # a=a-1
a *= 1  # a=a*1 int
a /= 1  # a=a/1 float
a //= 1  # a=a//1 float
a %= 1  # a=a%1 float

# 解包运算符
a, b, c = 1, 2, 3  # 变量个数=数值个数
print(a, b, c)
a, b, c = b, a, c  # 交换赋值
print(a, b, c)

# 比较运算符，结果为bool类型
a = 1
b = 2
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)  # ==比较值 a is b、a is not b比较标识
print(a != b)

# 布尔运算符
a = True
b = False
print(a and b)
print(a or b)
print(not a)  # 取反

s = 'hello world'
print('w' in s)
print('w' not in s)

# 位运算符
print(4 & 8)  # 按位与，同为1为1
print(4 | 8)  # 按位或，同为0为0
print(4 << 1)  # 向左移动一位，相当于乘以2
print(4 >> 1)  # 向右移动一位，相当于除以2

# 运算符优先级 算术运算 > 位运算 > 比较运算 > 布尔运算 > 赋值运算
