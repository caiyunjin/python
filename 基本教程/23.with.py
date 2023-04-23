# with（上下文管理器），不论什么原因跳出with语句，都能确保文件正确关闭，来达到释放资源的目的
with open('text.txt', 'r') as f:
    print(f.read())
