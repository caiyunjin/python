# 定义函数
def calc(a, b):  # a、b 形式参数
    c = a + b
    return c


# 位置实参
result = calc(10, 20)  # 10,20 实参
print(result)
# 关键字实参
result = calc(b=10, a=20)  # 10,20 实参
print(result)

# 不可变对象在函数体的修改不会响应实参


'''
1.如果函数没有返回值 return可以省略不写
2.返回值如果是一个，直接返回类型
3.返回值如果是多个，返回结果为元组
'''


def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            even.append(i)
        else:
            odd.append(i)
    return odd, even


lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(fun(lst))


def fun(a, b=10):  # 指定默认
    print(a, b)


fun(100)
fun(100, 20)  # 覆盖默认


# 个数可变的位置参数，元组
def fun(*args):
    print(args)


fun(10)
fun(10, 20)


# 个数可变的关键字参数，字典
def fun(**args):
    print(args)


fun(a=10)
fun(a=10, b=20)


# 结合 位置参数在前
def fun(*args1, **a):
    pass


#
def fun(a, b, c):
    print(a)
    print(b)
    print(c)


fun(10, 20, 30)
lst = [11, 22, 33]
fun(*lst)  # 将列表中的每个元素都转换为位置实参
fun(a=100, b=200, c=300)  # 关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)  # 将字典中的键值对都转换为关键字实参


# 函数内部局部变量，函数外全局变量
def fun(a, b):
    c = a + b  # c 为局部变量
    print(c)


#
name = 'caiyunjin'  # 全局变量


def fun():
    print(name)


fun()

# 递归函数，缺点：占用内存多，效率低下 优点：思路代码简单


def fun(n):
    if n == 1:
        return 1
    else:
        return n * fun1(n - 1)


print(fun(6))


# 斐波那契数列
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))