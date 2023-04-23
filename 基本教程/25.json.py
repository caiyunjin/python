# json(字符串)是轻量级的数据存储，不同语言之间的中转数据格式
# json格式是列表（内部嵌套字典）或字典
'''
{'name': 'admin','age':18}
[{'name': 'admin','age':18},{'name': 'admin','age':18}]
'''
import json

# 字典转换为JSON
data = [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 18}, {'name': '王五', 'age': 18}]

json_str = json.dumps(data, ensure_ascii=False)  # 中文需要 ensure_ascii=False
print(type(json_str))
print(json_str)

# JSON转换为python数据类型
s = '[{"name": "张三", "age": 18}, {"name": "李四", "age": 18}, {"name": "王五", "age": 18}]'

data = json.loads(s)
print(data)
