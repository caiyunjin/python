# 查询，index没有抛异常，find显示-1
s = 'hello world'
print(s.index('lo'))  # 正向查询
print(s.find('lo'))
# print(s.rindex('k'))  # 逆向查询
print(s.rfind('k'))

# 大小写转换
a = s.upper()  # 小写转大写
print(a)

b = a.lower()  # 大写转小写
print(b)

s1 = 'hEllo'
c = s1.swapcase()  # 大小写互换
print(c)

d = c.capitalize()  # 首字母大写，其余小写
print(d)

e = d.title()  # 每个单词首字母大写，其余小写

# 内容对齐
s2 = 'hello world'
# 居中
print(s2.center(20, '*'))  # 宽度20，填充*，默认空格
# 左对齐
print(s2.ljust(20))
# 右对齐
print(s2.rjust(20))
# 右对齐，使用0填充
print(s2.zfill(20))  # 只能用0填充

# 替换
lst = s2.split()
print(lst)

s2 = 'hello|world|python'
print(s2)
print(s2.split(sep='|'))
print(s2.split(sep='|', maxsplit=1))
# 逆向
print(s2)
print(s2.rsplit(sep='|'))
print(s2.rsplit(sep='|', maxsplit=1))

# 判断标识符
'''
s.isidentifier() 判断是否合法标识符
s.isspace() 判断是否全部由空白字符组成（回车、换行、水平制表符）
s.isalpha() 判断是否全部由字母组成
s.isdecimal() 判断是否全部由十进制的数字组成
s.isnumeric() 判断是否全部由数字组成
s.isalnum() 判断是否全部由字母和数字组成'''

# 替换
s = 'hello world'
print(s.replace('hello', 'b'))
s1 = 'hello hello hello world'
print(s1.replace('hello', 'b', 2))  # 指定替换数量

# 添加
lst = ['hello', 'world', 'world']
print('|'.join(lst))
print(''.join(lst))
lst = ('hello', 'world', 'world')
print(''.join('lst'))
print('*'.join('python'))

# 切片与列表相同

# 格式化
# % 占位符
# 1
name = '张三'
age = 18
print('我叫%s,今年%d岁' % (name, age))

# 2
print('我叫{0},今年{1}岁'.format(name, age))

# 3
print(f'我叫{name},今年{age}岁')

#
print('%d' % 88)
print('%10d' % 88)  # 10 表示宽度
print('%.3f' % 3.14156)  # 3 表示小数点后三位
print('%10.3f' % 3.14156)
print('{0:.3}'.format(3.14156))  # 总共三位数
print('{0:.3f}'.format(3.14156))
print('{0:10.3f}'.format(3.14156))

# 编码
s = '张三'
print(s.encode(encoding='GBK'))  # gbk 编码中，一个中文占两个字节
print(s.encode(encoding='utf-8'))  # utf-8 编码中，一个中文占三个字节

# 解码
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte = s.encode(encoding='utf-8')
print(byte.decode(encoding='utf-8'))
