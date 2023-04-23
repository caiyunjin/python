class Stduent:  # 规范为类首字母为大写，也可不大写
    native_pace = '浙江'  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性，进行了一个赋值操作，将局部变量的name的值赋给实体属性
        self.__age = age  # 加两个下划线，不被类的外部使用

    # 在类之内称为方法
    # 实例方法
    def show(self):
        print(self.name, self.__age)

    # 静态方法
    @staticmethod
    def sleep():  # 使用staticmethod进行修饰，所以是静态方法
        print('睡')

    # 类方法
    @classmethod  # 使用classmethod进行修饰，所以是静态方法
    def run(cls):
        print('跑')


# 类之外定义的称为函数
def drink():
    print('喝')


# 封装，提高程序的安全性
stu1 = Stduent('张三', 20)
stu2 = Stduent('王婷', 30)

# 下面两种写法一样
stu1.show()  # 对象名.方法名()
Stduent.show(stu1)  # 类名.方法名(类的对象)
# 动态绑定，类之外绑定属性
stu1.gender = '男'  # 只为stu1动态绑定性别属性，stu2就不能使用

# 类外使用name、age
print(stu1.name)
# print(stu1.__age) 不可被使用，因为有__
print(stu1._Stduent__age)  # 如果非要访问，在类的外部可通过 _Student__age访问


# 继承，提高代码的复用性
class Person(object):  # Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age, end=' ')


class Student1(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teach_no):
        super().__init__(name, age)
        self.teach_no = teach_no

    def info(self):
        super().info()
        print(self.teach_no)


stu = Student1('张三', 20, '1001')
teacher = Teacher('李四', 30, 10)
stu.info()
teacher.info()


# 多态
class Animal(object):
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃饭')


def Fun(obj):
    obj.eat()


Fun(Cat())
Fun(Dog())
Fun(Person())

# 特殊方法和属性
print(dir(object))


# 类的浅拷贝和深拷贝
class Cpu:
    pass


class Disk:
    pass


class conputer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
cpu1 = Cpu()
cpu2 = cpu1

# 浅拷贝
disk = Disk()
conputer1 = conputer(cpu1, disk)
import copy

conputer2 = copy.copy(conputer1)

print(conputer1, conputer1.cpu, conputer1.disk)
print(conputer2, conputer2.cpu, conputer2.disk)

# 深拷贝
conputer3 = copy.deepcopy(conputer1)
print(conputer1, conputer1.cpu, conputer1.disk)
print(conputer3, conputer3.cpu, conputer3.disk)
