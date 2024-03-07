# 与属性操作相关的内置函数

# delattr(object, name)

class Person:
    
    eat = "rice"     
    def __init__(self, age):
        self.age = age  

p = Person(18)
print(Person.eat)

""" 等价于 del Person.eat """
delattr(Person, "eat")  # 删除类属性eat
# print(Person.eat)  
print(p.age)

""" 等价于 del p.eat """
delattr(p, "age")  # 删除实例属性age
# print(p.age)

# getattr(object, name[, default])

class Person:
    
    eat = "rice"     
    def __init__(self, age):
        self.age = age  
        
p = Person(18) 
""" 等价于 Person.eat """
print(getattr(Person, "eat")) 
""" 等价于 p.age """
print(getattr(p, "age")) 
print(getattr(p, "height", 178))
# print(getattr(p, "height"))
class Person:
    
    eat = "rice"     
    def __init__(self, age):
        self.age = age  
        
p = Person(18)
print(hasattr(Person, "eat"))  # True
print(hasattr(p, "eat"))  # True
print(hasattr(p, "age"))  # True
print(hasattr(p, "height"))  # False


# setattr(object, name, value)
class Person:
    
    eat = "rice"     
    def __init__(self, age):
        self.age = age  
        
p = Person(18)
setattr(Person, "eat", "noodles")
print(Person.eat) 
setattr(Person, "drink", "water")
print(Person.drink) 
setattr(p, "age", 29)
print(p.age) 
setattr(p, "height", 178)
print(p.height)

# 类方法、对象方法、静态方法
class Student:     
    school = '深兰教育'     
    def __init__(self, name):
        self.name = name

    def study(self, course):
            print(f'{self.name}在学习{course}课!')    
        
    @classmethod  # 类方法装饰器
    def study(cls, course):
        print(f'{cls.school}的学生在学习{course}课!')
        print(f'{Student.school}的学生在学习{course}课!')     
    
    # @staticmethod  # 静态方法装饰器
    # def study(course):
    #     print(f'{Student.school}的学生在学习{course}课!')

stu1 = Student('张三')
stu2 = Student('李四')

"""
调用对象方法: 通常用实例对象去调用, 用类对象调用时需要主动给self传实参 """
stu1.study('Python')
stu2.study('机器学习')
# Student.study(stu1, 'Python')  # Python 还会隐式地将类 Student 本身作为第一个参数传递给 study 方法，这导致了三个参数被传递：Student, stu1, 'Python'。这就是为什么会报错说方法接收到了 3 个位置参数，而不是预期的 2 个。
# Student.study(stu2, '机器学习')
""" 调用类方法: 既可以用类对象调用(推荐), 也可以用实例对象调用 """
Student.study('Python')
stu1.study('Python')  # 本质: type(stu1).study('公开')
stu2.study('Python')  # 本质: type(stu1).study('公开') 

""" 调用静态方法: 既可以用类对象调用(推荐), 也可以用实例对象调用 """
Student.study('Python')
stu1.study('Python')
stu2.study('Python')

class A:
    
    var1 = 123     
    @classmethod
    def func1(cls):
        print(cls.var1)
    
    @staticmethod
    def func2():
        print(A.var1)

class B(A):
     var1 = 321  

A.func1()
A.func2()
B.func1()
B.func2()

# 特殊方法（魔术方法）
# __init__(self [, ...])
class Ex:
    def __init__(self, arg1, arg2):
        print(f"__init__被调用, arg1:{arg1}, arg2:{arg2}")  
     
Ex("a", "b")

# __call__(self [, ...])

class Ex:    
    def __call__(self, arg1, arg2):
        print(f"__call__被调用, arg1:{arg1}, arg2:{arg2}")  

e = Ex()
e("a", "b")

# __getitem__(self, item)
class Ex:     
    def __init__(self, seq):
        self.seq = seq     
    
    def __getitem__(self, item):
        return self.seq[item]  
    
e = Ex([3, 4, 1, 7])
print(e[2])
print(e[::2]) 

for i in e:
    print(i)

# __len__(self)
class Ex:     
    def __len__(self):
        return 1234  

e = Ex()
print(len(e))

# __str__(self)_    /    _repr__(self)
class Ex:     
    def __str__(self):
        return "__str__被调用"     
    
    # def __repr__(self):
    #     return "__repr__被调用"  

e = Ex()
print(str(e))
print(f"{e}")
print(e)  # print会转成字符串再输出

# 面向对象三大特性
# 在属性名或方法名前面加两个下划线开头, 声明为私有属性或私有方法
# 私有属性或私有方法只能在该类的内部调用, 不能在类的外部直接调用
# 可以提供一个非私有方法在类的外部间接访问私有属性或私有方法
# 就算是继承关系，子类也无法直接访问父类的私有属性和私有方法

class Person:     
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        if age <= 0:
            self.__age = "年龄必须大于0"  # 私有属性
        else:
            self.__age = age  # 私有属性
     # 利用非私有方法访问私有属性
    def show_info(self):
        print(f"姓名:{self.__name}\n年龄:{self.__age}")     # 私有方法
    def __sleep(self):
        print("我要睡觉了, 晚安!")     # 利用非私有方法调用私有方法
    def sleep(self):
        self.__sleep()

# 私有属性或私有方法只能在该类的内部调用
ps = Person("赵六", 26)
ps.show_info()
ps.sleep() 

# 不能在类的外部直接调用
# print(ps.__name) # 不可调用
# print(ps.__age) # 不可调用
# ps.__sleep() # 不可调用

class Person:     
    __school = "调用__school成功"  # 私有属性
    school = "调用school成功"  # 非私有属性

    def __sleep(self):  # 私有方法
        print("调用__sleep成功")

    def sleep(self):  # 非私有方法
        print("调用sleep成功")

class Student(Person):
    pass  

stu = Student()
print(Student.school)
stu.sleep()  # 非私有方法在类的外部间接调用私有方法

# 就算是继承关系，子类也无法直接访问父类的私有属性和私有方法
# print(Student.__school) # 不可调用
# stu.__sleep() # 不可调用
 
class A:     
    def __func(self):
        print('执行func')     
    def call_func(self):
        self.__func()  

class B(A):
    pass  

b = B()
# 子类调用父类的非私有方法, 间接调用父类的私有方法
b.call_func()

# 继承
# 所有的类都默认继承 object，只是一般不用写出来
# 子类继承父类后，会拥有父类中所有的非私有属性和方法
# 继承的作用：从子类来看，继承可以简化代码；从父类来看，子类是对父类功能的扩充
# class A(object) 每一个类默认继承 class object
class A:  
    pass  

# class B(A, object) 每一个类默认继承 class object
class B(A):
    pass

# 单继承 
# 多重继承


# 继承顺序
# 单继承查找顺序：先找自己的，再去找父类，再去找父类的父类，依此类推
# 多重继承查找顺序：先找自己的，再按照从左往右的顺序依次找父类的
# 当继承比较复杂时，可以使用__mro__属性查看搜索顺序

# 方法重写
# 在继承中，当父类方法的功能不能满足需求时，可以在子类重写父类的方法

# super()
# super是内置的类,  可以调用指定类的父类（超类）
# 适用场景：在子类重写父类方法后，想再使用父类的该方法

class Animal:     
    def eat(self):
        print("吃东西")  

class Cat(Animal):     
    def eat(self):
        print("吃鱼")

class Ragdoll(Cat):     
    def eat(self):
        print("喝咖啡")

rd = Ragdoll()
rd.eat()  # rd调用Ragdoll类中的对象方法
super(Ragdoll, rd).eat()  # rd调用Ragdoll父类的对象方法
super(Cat, rd).eat()  # rd调用Cat父类的对象方法

c = Cat()
c.eat()  # c调用Cat类中的对象方法
super(Cat, c).eat()  # c调用Cat父类的对象方法

# 继承中的__init__方法

class A:     
    def __init__(self, name):
        self.name = name
        self.Q()   
            
    def E(self):
            print('E方法被调用')   

    def Q(self):
            print(self.name, 'Q方法被调用')  

class B(A):
    pass

b = B('张三')  # 实例化,调用初始化方法,B没有则调用父类中的初始化方法,初始化方法中调用了Q方法
b.E()  # 调用父类的E方法
b.Q()  # 调用父类的Q方法

class C(A):     
    def __init__(self, name):
        self.names = name  

c = C('赵六')  # 实例化, 优先调用C中初始化方法
''' 虽然可以调用父类的Q方法, 但是因为Q方法中的self.name没有定义, 因为A的初始化方法没有被调用, 所以报错。解决方案: 先通过c调用一次A的初始化方法 或者 把C类中的self.names改为self.name 
'''
# c.Q()  # 报错
class D(A):
    def __init__(self, name):
        super(D, self).__init__('李四')
        self.name = name    

d = D('王五')  # 实例化, 先调用D的初始化方法, super方法调用父类的初始化方法, 父类的初始化方法中调用Q方法
d.Q()  # 调用父类的Q方法


# isinstance(object, classinfo)
class A:
    pass  
class B(A):
    pass  
class C(A):
    pass     
a = A()
b = B()
c = C()
print(isinstance(a, A))  # True
print(type(a) == A)  # True
print(isinstance(b, A))  # True，考虑继承
print(type(b) == A)  # False，type不考虑继承
print(isinstance(c, A))  # True，考虑继承
print(type(c) == A)  # False，type不考虑继承
print(isinstance(c, (B, A)))  # True，c是A子类的实例

# issubclass(class, classinfo)
print(issubclass(B, A))  # True
print(issubclass(C, A))  # True
print(issubclass(A, A))  # True，类会被视作其自身的子类
print(issubclass(C, (B, A)))  # True

# 多态性

class Apple:
    def change(self):
        return '啊~ 我变成了苹果汁!'  
class Banana:
    def change(self):
        return '啊~ 我变成了香蕉汁!'  
class Mango:
    def change(self):
        return '啊~ 我变成了芒果汁!'  
class Juicer:
    def work(self, fruit):
        print(fruit.change()) 

"""
三个内容不同的change方法使用相同的名字命名,
只要改变change的调用对象, 就可以调用不同内容的方法
"""
a = Apple()
b = Banana()
m = Mango()
j = Juicer()
j.work(a)
j.work(b)
j.work(m)

'''==============================错误异常=============================='''
# 内置异常
import builtins  
print(dir(builtins))

# try ... except ...
# try ... except ... 嵌套
# try ... except ... else ...
# try ... except ... as ...
# try ... finally ...
# 抛出异常
# raise 语句可以主动的抛出异常
# raise 后面可以是 异常实例 / 异常类 / 没有内容

# assert 断言
# assert 用于判断一个表达式，在表达式为 False 的时候触发 AssertionError 异常
# assert expression 等价于 if not expression: raise AssertionError
# assert expression [, arguments] 
# 等价于：if not expression: raise AssertionError(arguments)

num = int(input("请输入一个整数: "))
assert num != 1
print("断言条件为True, 用户没有输入1")


'''==============================闭包&装饰器=============================='''
# 在函数嵌套（函数里面再定义函数）的前提下
# 内部函数使用了外部函数的变量（参数）
# 外部函数的返回值是内部函数的引用

""" 自定义函数都会有一个__closure__属性, 如果不是闭包函数, 则返回None
如果是则返回一个由cell对象组成的元组, 每个cell对象的cell_contents属性就是外部
函数保存的变量 """

# 装饰器
# 装饰器，顾名思义就是起装饰作用的，不改变原来函数作用的，只是在原来函数上增加些额
# 外的功能。
# 装饰器并不是编码必须性，不使用装饰器也完全可以，很多时候使用它是为了：
# 使代码更加优雅，结构更加清晰
# 将实现特定的功能代码封装成装饰器，提高代码复用率

import time 

def timer(func):     
    def wrapper(sleep_time):
        t1 = time.time()
        func(sleep_time)
        t2 = time.time()
        cost_time = t2 - t1 
        print(f"花费时间：{cost_time}秒")     
    return wrapper

@timer  # 这个装饰器就是函数  
def function(sleep_time):
    time.sleep(sleep_time)

function(3)

import time  

def interaction(name):
    def wrapper(func):
        
        def deco(work_time):
            # print("deco函数被调用")
            print(f"{name}, 你好, 请把要洗的衣物放进来!")
            func(work_time)
            print(f"{name}, 我帮你把衣物洗好了, 快来拿!")         
        return deco     
    return wrapper  

@interaction("张三")
def washer(work_time):
    time.sleep(work_time)
    print("嘀嘀嘀...")

washer(3)


import time

class Timer:     
    def __init__(self, func):
        self.func = func
    
    def __call__(self, sleep_time):
        t1 = time.time()
        self.func(sleep_time)
        t2 = time.time()
        cost_time = t2 - t1 
        print(f"花费时间：{cost_time}秒")

@Timer  # 这个装饰器就是类
def function(sleep_time):
    time.sleep(sleep_time)

function(3)

import time

class Interaction:     
    def __init__(self, name):
        self.name = name     
    def __call__(self, func):
        def deco(work_time):
            print(f"{self.name}, 你好, 请把要洗的衣物放进来!")
            func(work_time)
            print(f"{self.name}, 我帮你把衣物洗好了, 快来拿!")
        return deco

@Interaction("张三")
def washer(work_time):
    time.sleep(work_time)
    print("嘀嘀嘀...")

washer(3)

# 多个装饰器
# ...

# 内置装饰器
# @classmethod 将类中的方法装饰为类方法
# @staticmethod 将类中的方法装饰为静态方法
# @property 将类中的方法装饰为只读属性