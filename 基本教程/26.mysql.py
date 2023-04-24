'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-24 16:37:30
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-24 17:54:47
FilePath: \python\基本教程\26.mysql.py
Description: 

'''
'''
1.大小写不敏感
2.单行或多行书写，末尾用 ; 结束
3.单行注释 空格--或 #
4.多行注释 /* */
'''

'''
1.查看数据库 show databases;
2.使用数据库 use 数据库名称;
3.创建数据库 create database 数据库名 [charset utf8](可选);
4.删除数据库 drop database 数据库名;
5.查看当前使用的数据库 select database();
'''

'''
1.查看表 show tables;
2.创建表 create table 表名(
            列名 列类型;
            列名 列类型;
                            )
3.删除表 drop table 表名;
'''

'''
1.单列插入 insert into 表名(列名) values(1),(2),...(N)；
2.全部插入 insert into 表名(列名,列名,列名) values(1,'张三',20),values(2,'李四',20)...(N)；
3.删除数据 delete from 表名 where 条件判断；（= > < 等操作符）
4.更新数据 update 表名 set 列=值 where 条件判断； #没有where 会全部修改成相同值
'''

# 基础语法
'''
1.查询 select 列,列 from 表名 where 条件判断；（全部列可用 * 代替）
2.分组聚合 select 字段|聚合函数（可多个） from 表名 where 条件判断 group by 列
                    sum(列) 求和
                    avg(列) 求平均值
                    min(列) 求最小值
                    max(列) 求最大值
                    count(列|*) 求数量
3.排序 select 字段|聚合函数（可多个） from 表名 where 条件判断 group by 列 order by 列 asc升序 desc降序
4.分页 select 字段|聚合函数（可多个） from 表名 where 条件判断 group by 列 order by 列 asc升序 desc降序 limit n[,m] 只写n只显示n条 n,m跳过前n条取m条
'''

from pymysql import Connection

conn = Connection(host='localhost', port=3306, user='root', passwd='a1986925')

cursor = conn.cursor()  # 获取游标对象
# 选择数据库
conn.select_db('world')
# 执行sql
cursor.execute('select * from city')
res = cursor.fetchall()
for i in res:
    print(i)

conn.close()
