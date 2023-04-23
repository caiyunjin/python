# 捕获BUG并输出
# try except
try:
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('请输入数字')

# try except else
try:
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    result = a / b
    print('结果为：', result)
except BaseException as e:
    print(e)
else:
    print('结果为：', result)

# try except else finally
try:
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    result = a / b
    print('结果为：', result)
except BaseException as e:
    print(e)
else:
    print('结果为：', result)
finally:  # 有无出错都执行
    print('谢谢您的参与')

# 打印异常
import traceback

try:
    print(1 / 0)
except:
    traceback.print_exc()
