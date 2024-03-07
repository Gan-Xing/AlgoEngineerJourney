
''' ============================面向对象编程============================ ''' 

def wash(name):
    print(f'{name}刷牙')
    print(f'{name}洗脸')  

def eat(name):
    print(f'{name}吃菜')
    print(f'{name}扒饭')  

def study(name):
    print(f'{name}看视频')
    print(f'{name}写代码') 

count_s = 0
stu1 = '张三'
age_s = 18
adres_s = '张家界'
print(f'大家好! 我是{stu1}, 今年{age_s}岁, 家住在{adres_s}, 欢迎大家有空来玩哦!')

count_s += 1
print(f'{stu1}起床')
wash(stu1)
eat(stu1)
print(f'{stu1}账号登录成功')
study(stu1)
eat(stu1)
study(stu1)
eat(stu1)
wash(stu1)
print(f'{stu1}睡觉')
print(f'当前统计的学生人数是: {count_s}')
def wash(name):
    print(f'{name}刷牙')
    print(f'{name}洗脸') 
    
def eat(name):
    print(f'{name}吃菜')
    print(f'{name}扒饭')  

def work(name):
    print(f'{name}授课')
    print(f'{name}答疑')
    print(f'{name}写代码')  
    
count_t = 0
tea1 = '老李'
age_t = 40
adres_t = '李家坡'
print(f'大家好! 我是{tea1}, 今年{age_t}岁, 家住在{adres_t}, 欢迎大家有空来玩哦!')
count_t += 1
print(f'{tea1}起床')
wash(tea1)
eat(tea1)
print(f'{tea1}今日打卡成功')
work(tea1)
eat(tea1)
work(tea1)
eat(tea1)
wash(tea1)
print(f'{tea1}睡觉')
print(f'当前统计的老师人数是: {count_t}')



class Student:
    s_count = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.show_time()
        Student.s_count += 1

    def show_time(self):
        print(f'大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来玩哦!')

    def get_up(self):
        print(f'{self.name}起床')

    def wash(self):
        print(f'{self.name}刷牙')
        print(f'{self.name}洗脸')

    def eat(self):
        print(f'{self.name}吃菜')
        print(f'{self.name}扒饭')

    def login_ID(self):
        print(f'{self.name}账号登录成功')

    def study(self):
        print(f'{self.name}看视频')
        print(f'{self.name}写代码')

    def sleep(self):
        print(f'{self.name}睡觉')

    @classmethod
    def publish(cls):
        print(f'当前统计的学生人数是: {cls.s_count}')

stu1 = Student('张三', 18, '张家界')
stu1.get_up()
stu1.wash()
stu1.eat()
stu1.login_ID()
stu1.study()
stu1.eat()
stu1.study()
stu1.eat()
stu1.wash()
stu1.sleep()
stu1.publish()

class Teacher:
    t_count = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.show_time()
        Teacher.t_count += 1

    def show_time(self):
        print(f'大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来玩哦!')

    def get_up(self):
        print(f'{self.name}起床')

    def wash(self):
        print(f'{self.name}刷牙')
        print(f'{self.name}洗脸')

    def eat(self):
        print(f'{self.name}吃菜')
        print(f'{self.name}扒饭')

    def clock_in(self):
        print(f'{self.name}今日打卡成功')

    def work(self):
        print(f'{self.name}授课')
        print(f'{self.name}答疑')
        print(f'{self.name}写代码')

    def sleep(self):
        print(f'{self.name}睡觉')

    @classmethod
    def publish(cls):
        print(f'当前统计的老师人数是: {cls.t_count}')

teacher1 = Teacher('老李', 40, '李家坡')
teacher1.get_up()
teacher1.wash()
teacher1.eat()
teacher1.clock_in()
teacher1.work()
teacher1.eat()
teacher1.work()
teacher1.eat()
teacher1.wash()
teacher1.sleep()
teacher1.publish()

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.show_time()

    def show_time(self):
        print(f'大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来玩哦!')

    def get_up(self):
        print(f'{self.name}起床')

    def wash(self):
        print(f'{self.name}刷牙')
        print(f'{self.name}洗脸')

    def eat(self):
        print(f'{self.name}吃菜')
        print(f'{self.name}扒饭')

    def sleep(self):
        print(f'{self.name}睡觉')

class Student(Person):
    s_count = 0

    def __init__(self, name, age, address, grade):
        self.grade = grade
        super(Student, self).__init__(name, age, address)
        Student.s_count += 1

    def login_ID(self):
        print(f'{self.name}账号登录成功')

    def study(self):
        print(f'{self.name}看视频')
        print(f'{self.name}写代码')

    @classmethod
    def publish(cls):
        print(f'当前统计的学生人数是: {cls.s_count}')

class Teacher(Person):
    t_count = 0

    def __init__(self, name, age, address, department):
        self.department = department
        super().__init__(name, age, address)
        Teacher.t_count += 1

    def clock_in(self):
        print(f'{self.name}今日打卡成功')

    def work(self):
        print(f'{self.name}授课')
        print(f'{self.name}答疑')
        print(f'{self.name}写代码')     
    
    @classmethod
    def publish(cls):
        print(f'当前统计的老师人数是: {cls.t_count} 人')  
        
stu1 = Student('张三', 15, '张家界', '九年级')
stu2 = Student('赵四', 10, '赵家村', '四年级')
Student.publish() 
tea1 = Teacher('老王', 38, '王家镇', '教学部')
tea2 = Teacher('老孙', 39, '孙家湾', '后勤部')
tea3 = Teacher('老李', 40, '李家坡', '科研部')
Teacher.publish()


# 类对象、实例对象、类属性、实例属性

"""
类, 类对象(通常用大驼峰法命名)
object是所有类的父类, 通常省略不写 
"""

class Student(object):     
    school = '深兰教育'  # 类属性(类变量)     
    def __init__(self, name, age):
        self.name = name  # 实例属性(实例变量)
        self.age = age

"""
魔术方法(特殊方法): 官方定义好的, 以两个下划线开头并且以两个下划线结尾的方法魔术方法特点: 一般不需要主动调用, 在满足特定条件时, 会被自动调用__new__称为构造方法, 用来创建实例对象, 并返回实例对象__init__称为初始化方法, 可以对实例对象进行属性定制, 没有返回值每当实例化时, 先自动调用魔术方法__new__(cls, *args, **kwargs), 把类对象(Student)作为实参传递给cls, 并把实例化时传入的其他实参('张三', age=28)分别传给*args, **kwargs, 然后__new__根据cls创建一个实例对象(obj), 并返回该实例对象(stu1=obj). 再自动调用魔术方法__init__(self, name, age), 把实例对象(obj)作为实参传递给self, 实例化时传入的其他实参('张三', age=28)分别传给name, age, 然后__init__再对实例对象(obj)进行属性定制(返回None, 相当于是对实例对象做inplace操作)  
"""
stu1 = Student('张三', age=28)
stu2 = Student('李四', 32) 
""" 调用实例属性: 只能用实例对象调用, 不能用类对象调用 """
print(stu1.name)
print(stu2.name) 
print(getattr(stu1, 'age'))
print(getattr(stu1, 'adres', '该实例属性不存在')) 
"""
调用类属性: 既可以用类对象调用(推荐), 也可以用实例对象调用
注意: 当实例属性和类属性同名时, 实例对象优先调用实例属性
"""
print(Student.school)
print(stu1.school)  # 本质: type(stu1).school
print(stu2.school)  # 本质: type(stu2).school print(getattr(Student, 'school'))
print(getattr(Student, 'adres', '该类属性不存在')) 
""" 修改实例属性: 只能用实例对象修改 """
stu1.age = 29
print(stu1.age) 
setattr(stu1, 'age', 27)
print(stu1.age) 
""" 修改类属性: 只能用类对象修改 """
Student.school = '深兰大学'
print(Student.school) 
setattr(Student, 'school', '深兰教育')
print(Student.school)

"""
动态定义实例属性: 当实例对象修改的属性不存在时, 则新增该实例属性
"""
stu1.school = 'ShenLanEdu'
print(stu1.school)  # 给stu1新增一个实例属性
print(Student.school)  # 类属性不变
setattr(stu2, 'adres', '威宁路')
print(stu2.adres)  # 给stu2新增一个实例属性

""" 动态定义类属性: 当类对象修改的属性不存在时, 则新增该类属性 """
Student.subject = 'AI'
print(Student.subject)  # 新增一个类属性
print(stu1.subject)
print(stu2.subject) 
setattr(Student, 'course', '人工智能')
print(Student.course)  # 新增一个类属性
print(stu1.course)
print(stu2.course) 

""" 删除属性: 可以用del语句 """
del stu1.age
delattr(stu1, 'name') 
del Student.school
delattr(Student, 'subject') 
""" 判定属性是否存在 """
print(hasattr(Student, 'school'))
print(hasattr(stu1, 'name'))
print(hasattr(stu2, 'age'))

 
