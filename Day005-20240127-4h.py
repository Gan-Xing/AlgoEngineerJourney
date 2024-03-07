# 循环控制语句  
     
# break
# 终止所在的循环

 
for _ in range(3):
    for _ in range(4):
        print('hello')
        break  

for _ in range(3):
    for _ in range(4):
        print('hello')
    break

# continue
# 跳过当前这次循环，继续到下一次循环
# 输出1-10之间的偶数
num = 1
while num <= 10:
    if num % 2:
        num += 1
        continue
    print(num)
    num += 1


# 列表推导式
lst = [x ** 2 for x in range(4)]
print(lst) 
# 类比
lst = []
for x in range(4):
    lst.append(x ** 2)
print(lst)  
lst = [x + y for x in range(5) if x % 2 for y in (1, 2, 3)]
print(lst) 
# 类比
lst = []
for x in range(5):
    if x % 2:
        for y in (1, 2, 3):
            lst.append(x + y)
print(lst)

# 字典推导式
d = {x: x**2 for x in range(4)}
print(d) 
# 类比
d = {}
for x in range(4):
    d[x] = x ** 2
print(d)  
d = {x: v for x in range(4) for v in range(9) if v % 2}
print(d) 
# 类比
d = {}
for x in range(4):
    for v in range(9):
        if v % 2:
            d[x] = v
print(d)


# 集合推导式
s = {x ** 2 for x in range(4)}
print(s) 
# 类比
s = set()
for x in range(4):
    s.add(x ** 2)
print(s)  
s = {x + y for x in range(5) if x % 2 for y in (1, 2, 3)}
print(s) 
# 类比
s = set()
for x in range(5):
    if x % 2:
        for y in (1, 2, 3):
            s.add(x + y)
print(s)


# 迭代
# lst = [1, 2, 3] 
# for i in lst:
#     lst.remove(i) 
#     print(lst)

lst = [1, 2, 3]
new_iter = lst.copy()
# new_iter = lst[:]
# new_iter = list(lst)
# new_iter = tuple(lst) 
for i in new_iter:
    lst.remove(i) 
    print(lst)


# 字典、集合在迭代时，不允许改变原数据的size
# d = {'name': 'Tom', 'age': 28, 'height': 177}
# for k in d:
#     print(d.pop(k))
#     print(d)  
    
# s = {'a', 'b', 'c', 'd', 'f'}
# for i in s:
#     s.remove(i)
#     print(s)

d = {'name': 'Tom', 'age': 28, 'height': 177}
new_iter = d.copy()
# new_iter = dict(d)
# new_iter = list(d)
# new_iter = tuple(d) 
for k in new_iter:
    print(d.pop(k))
    print(d)

s = {'a', 'b', 'c', 'd', 'f'}
new_iter = s.copy()
# new_iter = set(s)
# new_iter = list(s)
# new_iter = tuple(s) 

for i in new_iter:
    s.remove(i)
    print(s)


# pass 是一个关键字，表示一个空语句，当它被执行时，不做任何操作，通常用作占位符，在语法上需要语句但实际上不需要执行任何操作的情况下使用
score = float(input('你这次考试考了多少分? '))
if score >= 90:
    print('厉害!')
elif score >= 80:
    pass
elif score >= 70:
    print('良好!')
elif score >= 60:
    ...
else:
    print('不及格!')


''' =======================函数======================= '''

""" 自定义函数 """
def plus(num):
    print(num + 1)  

""" 调用函数 """
plus(2)  # 3
plus(5)  # 6 

"""
输出函数的引用，显示地址
f和plus指向同一个函数
"""

f = plus
print(plus)
print(f)
f(2)  # 3
f(5)  # 6

# 返回单个对象
def add1(left, right):
    res = left + right
    return res  

# 返回一个表达式
def add2(left, right):
    return left + right  

# 返回多个对象, 自动打包成一个元组
def add3(left, right):
    res1 = left + right
    res2 = left * right
    return res1, res2  

# 返回多个表达式
def add4(left, right):
    return left + right, left * right  

# return None
def add5(left, right):
    print(left + right)
    return  

# return None
def add6(left, right):
    pass  
print(add1(3, 4))
print(add2(3, 4))
print(add3(3, 4))
print(add4(3, 4))
print(add5(3, 4))
print(add6(3, 4))


# 文档注释

def div_mod(x, y):
    """
    Return the tuple (x//y, x%y).
    :param x: number(except complex)
    :param y: number(except complex)
    :return: (x//y, x%y)
    """
    div = x // y
    mod = x % y
    return div, mod  

# __doc__属性存放了文档注释
print(div_mod.__doc__)
print(divmod.__doc__)

# print(divmod.__doc__) 打印的是 Python 内置函数 divmod 的文档字符串。divmod 是 Python 的一个标准库函数，它接受两个数字作为参数，返回一个包含商和余数的元组。当你调用 print(divmod.__doc__) 时，它将显示 Python 官方为 divmod 函数编写的文档字符串。

# help 
# 启动内置的帮助系统
# 如果没有实参，解释器控制台里会启动交互式帮助系统
# 如果实参是一个字符串，则在模块、函数、类、方法、关键字或文档主题中搜索该
# 字符串，并在控制台上打印帮助信息
# 如果实参是其他任意对象，则会生成该对象的帮助页

help()  # 启动交互式帮助系统
help("keywords")  # 查看关键字
help(list)  # 生成list的帮助页

# abs
# x：可以是整数，浮点数，布尔型，复数。
# 返回一个数的绝对值，如果参数是一个复数，则返回它的模

print(abs(-6))  # 6，参数是整数
print(abs(6.9))   # 6.9，参数是浮点数
print(abs(3+4j))  # 5.0，参数是复数

# divmod(a, b)
# 返回一个元组 (a // b, a % b)

print(divmod(7, 3))  # (2, 1)
print(7 // 3, 7 % 3)
print(divmod(-9, 2))  # (-5, 1)
print(-9 // 2, -9 % 2)

# max(iterable[, key, default])  /  max(arg1, arg2, *args[, key])返回给定数据的最大值
print(max([3, 1, 2]))
print(max(3, 1, 2))
print(max('1', '2', '3', '10'))
print(max([], default=666))
print(max([1, 2, -3], key=abs))

# 1. `print(max([3, 1, 2]))`：
#    - 这个调用查找列表 `[3, 1, 2]` 中的最大值。
#    - 列表中的最大值是 3。
#    - 因此，打印结果是 `3`。

# 2. `print(max(3, 1, 2))`：
#    - 这个调用比较三个独立的参数 3, 1, 和 2。
#    - 其中最大的是 3。
#    - 所以，打印结果是 `3`。

# 3. `print(max('1', '2', '3', '10'))`：
#    - 这个调用比较四个字符串：'1', '2', '3', 和 '10'。
#    - 在 Python 中，字符串按照字典序进行比较，而不是按照数值大小。
#    - 字典序是按字符从左到右比较的，所以 '10' 会被视为小于 '2'（因为字符 '1' 小于 '2'）。
#    - 在 '1', '2', '3', '10' 中，按字典序最大的是 '3'。
#    - 因此，打印结果是 `'3'`。

# 4. `print(max([], default=666))`：
#    - 这个调用尝试在一个空列表 `[]` 中找到最大值。
#    - 由于列表是空的，没有元素可以比较，所以会返回 `default` 参数指定的值。
#    - `default` 设为 666。
#    - 所以，打印结果是 `666`。

# 5. `print(max([1, 2, -3], key=abs))`：
#    - 这个调用查找列表 `[1, 2, -3]` 中的最大值，但是使用 `abs` 函数作为键（key）来比较。
#    - `abs` 函数返回数的绝对值。
#    - 所以，列表中的元素按照它们的绝对值比较：`abs(1) = 1`, `abs(2) = 2`, `abs(-3) = 3`。
#    - 绝对值最大的是 `abs(-3)`，即 3。
#    - 因此，即使 -3 是负数，由于它的绝对值最大，所以原始值 `-3` 被认为是最大的。
#    - 所以，打印结果是 `-3`。

# min
print(min([3, 1, 2]))
print(min(3, 1, 2))
print(min('20', '2', '3', '10'))
print(min([], default=666))
print(min([-9, 2, -3], key=abs))

# pow(base, exp[, mod])
# 返回 base 的 exp 次幂
# 如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余
print(pow(-2, 3))  # -2**3 = -8
print(pow(-2, 3, 3))  # -2**3 % 3 = 1


# round(number [, ndigits])
# number：数字
# ndigits：保留的小数点位数
# 返回 number 四舍五入到小数点后 ndigits 位精度的值，如果 ndigits 被省略或为 
# None，则返回值为整数，否则返回值和 number 类型相同
# Python 的 round 函数采用的是「银行家舍入」（Banker's Rounding）规则，即当数字恰好在中间时，它会舍入到最近的偶数。

pi = 3.141592653
print(round(pi))
print(round(pi, ndigits=None))
print(round(pi, ndigits=1))
print(round(pi, ndigits=2))
print(round(pi, ndigits=3))
print(round(3.141592653, ndigits=0))
print(round(-3.141592653, ndigits=0))
print(round(0.141592653, ndigits=0))
print(round(-0.141592653, ndigits=0)) # 作为了解
print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(2.665, ndigits=2))
print(round(2.675, ndigits=2))

# sum(iterable,  start=0)
# 从 start 开始自左向右对 iterable 的元素求和，并返回

# 计算列表 [1, 2, 3] 中的元素之和
print(sum([1, 2, 3]))  # 结果是 1 + 2 + 3 = 6

# 计算列表 [1, 2, 3] 中的元素之和，并添加起始值 100
print(sum([1, 2, 3], start=100))  # 结果是 100 + 1 + 2 + 3 = 106

# 计算字典 {1: 2, 3: 4, 5: 6} 中的键的和，并添加起始值 100
# 注意，这里 sum 函数仅对字典的键进行求和
print(sum({1: 2, 3: 4, 5: 6}, start=100))  # 结果是 100 + 1 + 3 + 5 = 109

# 参数传递  
# 传不可变对象 & 传可变对象

def func(b):
    print(id(a), a)
    print(id(b), b)

a = 789
func(a)

a = [789]
func(a)  

def func(b):
    b.append(345) 

a = [789]
func(a)
print(a)


# 必需参数
# 必须接收一个实参，否则报错
# 实参通常可以传位置参数，也可以传关键字参数
def func(a, b):
    print(a - b) 

func(4, 3)  # 1
func(3, 4)  # -1
func(a=3, b=4)  # -1

def func(a, b):
    print(a - b)  
func(a=3, b=4)
func(3, b=4)

def func(a, b=4):
    print(a - b)  
func(3)
func(3, 5)

# 不定长参数
# *args：接收[0, +∞]个位置参数，贪婪的，将它们打包成一个元组，如果没有接收到实参，则为空元组。
# **kwargs：接收[0, +∞]个关键字参数，贪婪的，将它们打包成一个字典，如果没有接收到实参，则为空字典。必须放在所有形参的最后。

def func(*args):
    print(args)  
func()
func(3, 1, 4, 6)  

def func(**kwargs):
    print(kwargs)  
func()
func(a=3, b=2, c=4)  

def func(*args, **kwargs):
    print(args)
    print(kwargs)  
func()
func(1, 2, a=3, b=4)

# 特殊参数
# 默认情况下，实参的传递形式可以是位置参数或关键字参数
# 可以用 / 和 * 来限制参数的传递形式
# 其中 / 为仅限位置参数，限制在它之前的形参只能接收位置参数
# 其中 * 为仅限关键字参数，限制在它之后的形参只能接收关键字参数
# 这两个特殊参数只是为了限制参数的传递形式，不需要为它们传入实参
def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)
    pass  

func(1, 2, 3, kwd1=4, kwd2=5)
func(1, 2, pos_or_kwd=3, kwd1=4, kwd2=5)

# 匿名函数 
# 格式： lambda [arg1 [, arg2, ... argN]] : expression
# 匿名函数的参数可以有多个, 但是后面的 expression 只能有一个
# 匿名函数返回值就是 expression 的结果，而不需要 return 语句
# 匿名函数可以在需要函数对象的任何地方使用（如：赋值给变量、作为参数传入其
# 他函数等），因为匿名函数可以作为一个表达式，而不是一个结构化的代码块

# 创建一个匿名函数（lambda 函数）。使用 lambda 关键字来定义，这是一种简洁的函数定义方式，无需使用 def 语句。
# 在 lambda 关键字后面没有定义参数，表明这个函数不接受任何参数。
# 冒号（:）后面的表达式定义了函数的返回值。在这个例子中，函数返回一个字符串 'It just returns a string'

print((lambda: 'It just returns a string')())
f = lambda: 'It just returns a string'
print(f())  
(lambda x, y, z: print(x + y + z))(1, 2, 3)
f = lambda x, y, z: print(x + y + z)
f(1, 2, 3)  
def call_f(function, a, b, c):
    return function(a, b, c)  
print(call_f(lambda x, y, z: x + y + z, 1, 2, 3))

# 封包
# 将多个值同时赋值给一个变量时，Python 会自动将这些值封装成一个元组，这个特性称之为封包

tup = 345, 'hello', 789
print(tup)

# 解包
# 解包是针对可迭代对象的操作
# 在可迭代对象前面加一个星号（*），在字典对象前面加双星（**），这种解包方
# 式主要运用在函数传参的过程中
a, b, c = [4, 3, 'a']
print(a)  # 4
print(b)  # 3
print(c)  # 'a' 

a, *b, c = 'hello'
print(a)  # 'h'
print(b)  # ['e', 'l', 'l']
print(c)  # 'o' 

a, *b, c = 'he'
print(a)  # 'h'
print(b)  # []
print(c)  # 'e' 

*a, = 'hel'
print(a)  # ['h', 'e', 'l'] 

_, *b, _ = [4, 3, 5, 7]
print(b)  # [3, 5]

def func(a, b, c):
    print(a, b, c)  
"""
在函数传参时, *iterable可以将
该iterable解包成位置参数
"""
tup = (1, 2, 3)
func(*tup)

"""
在函数传参时, **dict可以将
该dict解包成关键字参数
"""
d = {'a': 1, 'b': 2, 'c': 3}
func(*d)
func(**d)


# 命名空间与作用域
list1 = [1, 2, 3, 4, 2, 2]
set1 = set(list1)
print(f'集合set1的内容: {set1}')  # 打印集合set1的内容
print(f'将集合set1转换为元组: {tuple(set1)}')  # 将集合set1转换为元组并打印
print(f'将集合set1转换为列表: {list(tuple(set1))}')  # 将集合set1转换为列表并打印

import builtins  
print(f'内置命名空间的内容: {dir(builtins)}')  # 打印内置命名空间的内容
print(f'当前全局命名空间的内容: {dir()}')  # 打印当前全局命名空间的内容
print(f'list对象的命名空间内容: {dir(list)}')  # 打印list对象的命名空间内容

def func1(arg1, arg2):
    num = 666
    print(f'func1的局部命名空间: {locals()}')  # 打印func1的局部命名空间

def func2(arg1, arg2):
    num = 777
    print(f'func2的局部命名空间: {locals()}')  # 打印func2的局部命名空间

num = 111
func1(222, 333)
func2(444, 555)

print(f'当前全局命名空间: {globals()}')  # 打印当前全局命名空间
# 在全局作用域, locals()等价于globals()
print(f'当前局部命名空间(等价于全局): {locals()}')  # 打印当前局部命名空间(等价于全局)
print(f'eval计算abs(-3): {eval("abs(-3)")}')  # 使用eval计算abs(-3)并打印
exec('print(f"exec执行abs(-3): {abs(-3)}")')  # 使用exec执行abs(-3)并打印


string = """
import random
num = random.randint(1, 10)
print(num)
"""
exec(string)


# 继续之前的代码

a = 1
b = 2 
def add():
    a = 3
    print(f'在局部作用域中计算a+b: {eval("a + b")}')  # 在局部作用域中计算a+b
    print(f'指定局部命名空间中a=4, b=5计算a+b: {eval("a + b", {"a": 4, "b": 5})}')  # 指定局部命名空间中a=4, b=5计算a+b
    print(f'指定全局命名空间a=6, b=7和局部命名空间a=8, b=9计算a+b: {eval("a + b", {"a": 6, "b": 7}, {"a": 8, "b": 9})}')  # 指定全局命名空间a=6, b=7和局部命名空间a=8, b=9计算a+b
    print(f'指定全局命名空间a=6, b=7和局部命名空间a=8, c=9计算a+b: {eval("a + b", {"a": 6, "b": 7}, {"a": 8, "c": 9})}')  # 指定全局命名空间a=6, b=7和局部命名空间a=8, c=9计算a+b
add()

def func():
    a = 2  # 局部变量
    b = 3  # 局部变量
    print(f'局部变量a+b的值: {a + b}')  # 局部作用域可以调用局部变量a,b
    print(f'全局变量d的值: {d}')  # 局部作用域可以调用全局变量d

d = 4  # 全局变量
func()

def outer():
    b = 2  # Enclosing变量b,c
    c = a + 3  # Enclosing可以调用全局变量a
    
    def inner():
        c = 5  # 局部变量c
        print(f'全局变量a的值: {a}')  # 局部作用域可以调用全局变量a
        print(f'Enclosing变量b的值: {b}')  # 局部作用域可以调用Enclosing变量b
        print(f'局部变量c的值: {c}')  # 优先调用自己作用域内的变量c，而不调用Enclosing变量c
        
    inner()  

a = 1  # 全局变量
outer()

def outer():
    a = c + 2  # Enclosing可以调用全局变量c     
    
    def inner():
        b = c + 3  # 局部作用域可以调用全局变量c
        print(f'Enclosing变量a+b的值: {a + b}')  # 局部作用域可以调用Enclosing变量a     
    inner()  

c = 1  # 全局变量
outer()
print(f'全局变量c: {c}')  # 打印全局变量c

# abs是内置函数、int是内置类，它们都在内建作用域builtins模块中
num1 = abs(-100)
num2 = int(3.141592653)
def outer():
    global a, b  # 声明当前作用域的a,b为全局变量
    a, b, c, d = 3, 4, 5, 6
    print(f'全局变量a, b: {a}, {b}')  # 打印全局变量a, b
    
    def inner():
        global a, b  # 声明当前作用域的a,b为全局变量
        nonlocal c, d  # 声明当前作用域的c,d为Enclosing变量
        a, b, c, d = 7, 8, 9, 0
        print(f'更改后的全局变量a, b和Enclosing变量c, d: {a}, {b}, {c}, {d}')  # 打印更改后的全局变量a, b和Enclosing变量c, d
    
    inner()
    print(f'Enclosing变量c, d: {c}, {d}')  # 打印Enclosing变量c, d

a, b = 1, 2
outer()
print(f'全局变量a, b: {a}, {b}')  # 打印全局变量a, b

def func():
    a = 6
    b = a + 1
    print(f'局部变量a+b: {b}')  # 打印局部变量a和b的和

a = 9
func()



# 常用高阶函数
# 定义：参数或返回值为其他函数的函数
# function：函数（function 必需能够接受1个实参），也可以为 None
# iterable：可迭代对象
# 将 iterable 中每个元素作为参数传递给函数，根据函数的返回结果进行判断 True 
# 或 False，将判断为 True 的 iterable 中的元素构建新的迭代器并返回
# 如果 function 为 None，直接判断 iterable 中元素 True 或 False，再返回为 True 
# 的元素构建的新的迭代器

# 思考：如果换成 lambda x: print(x-1) 会怎样?
# 常用高阶函数
object1 = filter(lambda x: x-1, [1, 2, 3, False, 4])
print(f'filter结果1: {list(object1)}')  # 打印filter结果1

object3 = filter(None, [1, 2, 0, 3, False, 4])
print(f'filter结果2: {list(object3)}')  # 打印filter结果2

# map(func, *iterables)
# func：函数（func 必需能够接收 iterables 个数的实参）iterables：可迭代对象
# 用 iterables 中的每个元素作为函数的参数来调用函数，以迭代器形式返回所有结
# 果当有多个 iterables 对象时，最短的 iterables 耗尽则函数停止

# map函数的应用
def square(a):
    return a**2 # 思考：如果改为 print(a**2) 会怎样? 
result = map(square, [1, 2, 3])
print(f'map结果1: {list(result)}')  # 打印map结果1

result = map(lambda a: a**2, [1, 2, 3])
print(f'map结果2: {list(result)}')  # 打印map结果2

result = list(map(float, ["1", "2", "3"]))
print(f'map结果3: {result}')  # 打印map结果3

result = list(map(lambda x, y, z: x+y+z, [1, 2, 3], [3, 2, 1], [1, 3, 2]))
print(f'map结果4: {result}')  # 打印map结果4

result = list(map(lambda x, y, z: x+y+z, [1, 2, 3], [3, 2, 1], [1, 3]))
print(f'map结果5: {result}')  # 打印map结果5

# reduce(function, iterable[, initial])

# function：函数（function 必需能够接收两个实参）
# iterable：可迭代对象
# initial：初始值
# 在 Python2 中 reduce() 是内置函数，而在Python3中 reduce() 函数是在functools
# 模块中的，所以在使用的时候需要先导入 functools 模块
# 在没有指定 initial 参数时，先把 iterable 的前两个元素作为参数调用函数，把这
# 次函数的结果以及iterable 的下一个元素又作为参数再调用函数，以此类推
# 在指定 initial 参数时，先把 initial 值和 iterable 的第一个元素作为参数调用函
# 数，把这次函数的结果以及 iterable 的下一个元素又作为参数再调用函数，以此类
# 推
# 如果 iterable 为空，返回 initial ，此时如果没有指定 initial，则报错
# 如果 iterable 只有一个元素且没有指定 initial，返回该元素
from functools import reduce

def add(m, n):
    s = m + n
    return s   # 如果改为 print(s) 会怎样?
# 过程：[(1+2)+3]+4 = 10
result = reduce(add, [1, 2, 3, 4])
print(f'使用reduce函数累加结果: {result}')  # 使用reduce函数进行累加并打印结果

# 过程：2*[2*(2*5+1)+2]+3 = 51
result = reduce(lambda x, y: 2*x + y, [1, 2, 3], 5)
print(f'使用reduce和lambda表达式计算结果: {result}')  # 使用reduce和lambda表达式计算结果并打印

# iterable为空，返回initial
result = reduce(lambda x, y: 10*x + 2*y, [], 123)
print(f'iterable为空时reduce的结果: {result}')  # 当iterable为空时reduce的结果

# iterable只有一个元素且没有指定 initial，返回该元素
result = reduce(lambda x, y: 10*x + 2*y, [123])
print(f'iterable只有一个元素时reduce的结果: {result}')  # 当iterable只有一个元素时reduce的结果

# 过程：10*2 + 2*123 = 266
result = reduce(lambda x, y: 10*x + 2*y, [123], 2)
print(f'使用reduce和lambda表达式计算结果: {result}')  # 使用reduce和lambda表达式计算结果并打印
