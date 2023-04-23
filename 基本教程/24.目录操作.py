# OS模块与操作系统相关
import os

'''
os.system('notepad.exe')  # 打开记事本

# 直接调用执行文件
os.startfile('D:\\...\....exe')

print(os.getcwd())  # 当前文件路径
lst = os.listdir()  # 获取当前目录下所有文件
os.mkdir()  # 创建目录
os.makedirs('A/B/C')  # 创建多级目录
os.rmdir()  # 删除目录
os.removedirs('A/B/C')  # 删除多级目录
os.chdir()  # 设置当前工作目录
'''
# os.path
import os.path

os.path.exists()
os.path.isfile()
os.path.isdir()
os.path.islink()
os.path.lexists()
os.path.isabs()
os.path.join()
os.path.split()
os.path.abspath()
os.path.relpath()
os.path.normcase()
os.path.normpath()
os.path.dirname()
os.path.basename()
os.path.splitext()
os.path.commonprefix()
os.path.commonsuffix()
os.path.getsize()
os.path.getatime()
os.path.getmtime()
os.path.getctime()
os.path.walk()
os.path.splitdrive()
