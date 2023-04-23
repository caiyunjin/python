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
