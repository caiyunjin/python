'''
r 以只读模式打开文件，文件的指针将放在文件的起始位置
w 以只写模式打开文件，如果文件不存在则创建，如果存在则覆盖原内容，文件指针在文件的起始位置
a 以追加模式打开文件，如果文件不存在则创建，文件指针在文件起始位置，如果文件存在，则在文件末尾追加内容
b 以二进制方式打开文件，不能单独使用，需要与其它模式一起，rb或wb
+ 以读写方式打开文件，不能单独使用，需要与其它模式一起，a+
'''
file = open('text.txt', 'r')
print(file.readlines())
file.close()

file = open('b.txt', 'w')
file.write('hello')
file.close()

# 二进制文件，mp3文件，jpg图片，doc文档等
src_file = open('logo.png', 'rb')
target_file = open('copylogo.png', 'wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()

# 常用方法
'''
read([size]) 读取size个字节或字符的内容。若省略[size],则返回全部内容。
readline() 读取一行内容
readlines() 每一行都作为独立的字符串对象，并将这些对象放入列表
write(str) 将字符串str内容写入文件
writelines(s_list) 将字符串列表s_list内容写入文件，不添加换行符
seek(offset[,whence]) 把文件指针移动到新的位置，offset表示相对于whence的位置
                      offset：为正，正向读取。为负，逆向读取
                      whence：
                      0.表示从文件开头开始（默认）
                      1.表示从文件末尾开始
                      2.表示从文件末尾开始
tell() 返回文件指针的当前位置
flush() 把缓冲区的内容写入文件，但不关闭文件
close() 把缓冲区的内容写入文件，同时关闭文件
'''
