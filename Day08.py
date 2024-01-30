# # 可迭代对象 & 迭代器 & 生成器

# # 判断 Iterable、Iterator、Generator

# from typing import Iterable, Iterator, Generator 
# num1 = 123
# str1 = "abc"
# list1 = [1, 2, 3]
# tup1 = (1, 2, 3)
# dict1 = {"one": 1, "two": 2, "three": 3}
# set1 = {1, 2, 3} 
# """Python标准数据类型中, 除了number, 其他都是可迭代对象, 即可以用for循环来遍
# 历"""
# print(isinstance(num1, Iterable))  # False
# print(isinstance(str1, Iterable))  # True
# print(isinstance(list1, Iterable))  # True
# print(isinstance(tup1, Iterable))  # True
# print(isinstance(dict1, Iterable))  # True
# print(isinstance(set1, Iterable))  # True print(isinstance(num1, Iterator))  # False
# print(isinstance(str1, Iterator))  # False
# print(isinstance(list1, Iterator))  # False
# print(isinstance(tup1, Iterator))  # False
# print(isinstance(dict1, Iterator))  # False
# print(isinstance(set1, Iterator))  # False print(isinstance(num1, Generator))  # False
# print(isinstance(str1, Generator))  # False
# print(isinstance(list1, Generator))  # False
# print(isinstance(tup1, Generator))  # False
# print(isinstance(dict1, Generator))  # False
# print(isinstance(set1, Generator))  # False 

# """ range对象是可迭代对象 """
# range1 = range(4)
# print(isinstance(range1, Iterable)) 
# """ reversed对象是迭代器 """
# reversed1 = reversed([1, 3, 1, 4])
# print(isinstance(reversed1, Iterator)) 
# """ zip对象是迭代器 """
# zip1 = zip([1, 2, 3], ["one", "two", "three"])
# print(isinstance(zip1, Iterator)) 
# """ enumerate对象是迭代器 """
# enumerate1 = enumerate([1, 2, 3])
# print(isinstance(enumerate1, Iterator))



# # 可迭代对象
# # 支持迭代协议（有__iter__()方法）
# # 支持序列协议（有__getitem__()方法，且数字参数从0开始）

# num1 = 123
# str1 = "abc"
# list1 = [1, 2, 3]
# tup1 = (1, 2, 3)
# dict1 = {"one":1, "two":2, "three":3}
# set1 = {1, 2, 3}
# range1 = range(4)  

# """ str, list, tuple, dict, set, range对象都支持迭代协议, 所以他们都是可迭
# 代对象，而 number 对象既不支持迭代协议，也不支持序列协议，因此它不是可迭代对象 """

# print('__iter__' in dir(num1) or '__getitem__' in dir(num1))  # False
# print('__iter__' in dir(str1))
# print('__iter__' in dir(list1))
# print('__iter__' in dir(tup1))
# print('__iter__' in dir(dict1))
# print('__iter__' in dir(set1))
# print('__iter__' in dir(range1))

# # 自定义可迭代对象
# # 只要支持迭代协议或者序列协议即可

# from typing import Iterable  

# class MyObject1:
    
#     def __init__(self):
#         pass  
    
# mo1 = MyObject1()
# print(isinstance(mo1, Iterable))  # False: 既不支持迭代协议, 也不支持序列协议
# class MyObject2:
#     def __init__(self):
#         pass     
#     def __iter__(self):
#         pass  
# mo2 = MyObject2()
# print(isinstance(mo2, Iterable))  # True: 因为有__iter__()方法, 即支持迭代协议
# class MyObject3:
#     def __init__(self):
#         pass     
#     def __getitem__(self, index):
#         pass  

# mo3 = MyObject3()
# print(isinstance(mo3, Iterable))  # False 

# """
# mo3支持序列协议, 为何 isinstance 判断为 False 呢? 
# 注意: 使用 isinstance(obj, Iterable) 可以检测obj是否有__iter__()方法,
# 但是无法检测是否能够使用__getitem__()方法进行迭代
# """

# # 迭代器
# # 支持迭代器协议（注意区分迭代协议），即同时满足下面两个条件
# # 实现__iter__()方法
# # 实现__next__()方法

# reversed1 = reversed([1, 3, 1, 4])
# zip1 = zip([1, 2, 3], ["one", "two", "three"])
# enumerate1 = enumerate([1, 2, 3]) 




# print('__iter__' in dir(reversed1) and '__next__' in 
# dir(reversed1))
# print('__iter__' in dir(zip1) and '__next__' in dir(zip1))
# print('__iter__' in dir(enumerate1) and '__next__' in 
# dir(enumerate1))

# # 自己创建迭代器 只要支持迭代器协议即可

# from typing import Iterator
# class MyObject3:
    
#     def __init__(self):
#         pass     
#     def __iter__(self):
#         pass
#     def __next__(self):
#         pass

# mo3 = MyObject3()
# print(isinstance(mo3, Iterator))  # True: 支持迭代器协议

# # 迭代的逻辑
# # 迭代的时候，先找__iter__()方法，如果没有的话，再找__getitem__()方法

# # 如果有__iter__()方法：
# # ① 可迭代对象里的__iter__()方法返回一个迭代器，通过迭代器里的__next__()方法实现迭代
# # ② 迭代器里的__iter__()方法返回它本身（因为迭代器协议中包含了迭代协议，所以迭代器也一定是可迭代对象，可迭代对象的__iter__()方法要返回一个迭代器，所以只需要返回本身即可）
# # ③ 迭代器里的__next__()方法返回可迭代对象的下一项，如果没有下一项可返回，则抛出 StopIteration 异常


# """
# for语句在执行时会先调用可迭代对象的__iter__()方法, 得到该方法返回的迭代器对象,然后每循环一次, 该迭代器对象调用一次__next__()方法, 通过__next__()方法来逐一返回元素,当元素用尽时, __next__()方法将抛出StopIteration异常, 而for语句会捕获这个异常来break循环
# """

# """
# 除了for循环以外, 其他能够接收iterable参数的函数或方法大多都是基于类似原理,比如: list()、tuple()、set()、sum()等等 """

# """
# 迭代器也是可迭代对象, for语句在执行时会先调用迭代器的__iter__()方法,而迭代器的__iter__()方法正好返回迭代器对象本身, 后面过程就是一样的了"""


# # 如果只有__getitem__()方法：
# """
# for语句在执行时, 先找__iter__()方法, 没有找到, 则找__getitem__()方法, 然后每循环一次, 调用一次__getitem__()方法, 其中index参数从0开始, 无限递增+1, 当index超出iterable索引范围抛出IndexError, for语句会捕获这个异常来break循环,list()、tuple()、set()、sum()等也是基于类似原理
# """

# # 生成器
# # 生成器写法类似于标准的函数写法，不同点在于
# # 生成器用 yield 语句返回数据，而标准的函数用 return 语句返回数据
# # yield 语句返回数据之后会挂起函数的状态，并会记住上次执行语句时的所有数据值，方便每次在生成器调用__next__()方法时，从上次挂起的位置恢复继续执行，而 return 语句返回一次数据之后，函数就结束了

# from collections import Generator, Iterator

# def func():
#     print("The function body starts executing...")
#     return 2
#     print("The function body continues execution...")
#     return 4
#     print("ending...") 

# res = func()
# print(res)  

# def gen():
#     print("The function body starts executing...")
#     yield 2
#     print("The function body continues execution...")
#     yield 4
#     print("ending...")

# """
# 包含yield关键字的函数就是生成器函数, 调用生成器函数不会执行函数体代码,而是直接返回一个生成器对象, 调用__next__()方法才会开始执行函数体代码 """

# g = gen()  # 返回生成器对象
# print(isinstance(g, Generator))  # True
# print("__iter__" in dir(g) and "__next__" in dir(g))  # True: 生成器
# # 实现了迭代器协议
# print(isinstance(g, Iterator))  # True: 生成器一定也是迭代器
# """
# 生成器对象调用__next__()方法就会开始执行函数体代码, 遇到 yield 则把后面的数据返回, 然后挂起函数的状态, 直到下一次调用__next__()方法, 再从挂起的状态继续往后执行, __next__()方法如果没有可以返回的值, 会抛出StopIteration异常, 直到函数体执行完毕, 函数才算结束 """
# print(g.__next__())
# print(g.__next__()) 

# """ 从上一步挂起状态继续往后执行, 输出: ending...
# 此时__next__()没有可以返回的值, 抛出 StopIteration 异常
# 函数体执行完毕, 函数结束 """
# # print(g.__next__())  
# g2 = gen()  # g迭代完毕, 再建一个生成器
# """
# 生成器也是迭代器, 所以和迭代器逻辑是一样的, for语句在执行时会先调用__iter__()方法, 返回self, 然后每次循环时, self调用一次__next__()方法, 因为调用了该方法, 函数体就会开始执行, 执行到yield, 把后面的数据返回, 然后函数挂起, 当循环又调用__next__()方法时, 则从函数挂起处继续执行函数体, 而当没有 yield 时, 即没有返回数据时, __next__()方法将引发 StopIteration 异常, for语句会捕获这个异常来 break 循环 """
# for i in g2:
#     print(i)
    
# """ list()、tuple()、set()、sum()等也是基于类似原理 """
# print(list(g2))
# print(tuple(g2))
# print(set(g2))
# print(sum(g2))
# # 列表推导式
# list1 = [i for i in range(5)]
# print(type(list1))  # <class 'list'>
# print(sum(list1))  # 10
# print(sum(list1))  # 10  

# # 生成器表达式
# gt1 = (i for i in range(5))
# print(type(gt1))  # <class 'generator'> 
# """
# 这里gt1第二次sum结果为什么是0, 而上面的list1却不是?因为同一个gt1生成器对象, 第一次sum已经迭代完了, 而sum默认从0开始累加, 结果就为0.
# 而每次sum(list1)都会通过list的__iter__()方法返回新的迭代器, 并不是同一个 """
# print(sum(gt1))  # 10
# print(sum(gt1))  # 0 

# """ 生成器表达式如果立即被外层的函数使用, 可以省略圆括号, 
# 而不用写成 sum((i for i in range(5))) """
# print(sum(i for i in range(5)))  # 10

# # iter(object[,sentinel])
# # 返回一个迭代器对象
# # 如果没有第二个实参，object必须支持迭代协议（有__iter__()方法）或序列协议
# # （有__getitem__()方法，且数字参数从0开始）。如果它不支持这些协议，会触发
# # TypeError
# # 如果有第二个实参sentinel，那么object必须是可调用的（函数、方法、lambda匿
# # 名函数、 类以及实现了 __call__ ()方法的实例对象）。这种情况下生成的迭代器，
# # 每次迭代调用它的__next__()方法时都会不带实参地调用object，返回调用的结
# # 果，如果返回的结果是sentinel，则触发StopIteration
# str1 = "abc"
# list1 = [1, 2, 3]
# tup1 = (1, 2, 3)
# dict1 = {"one": 1, "two": 2, "three": 3}
# set1 = {1, 2, 3} 

# # str1、list1、tup1、dict1、set1 支持迭代协议
# print(iter(str1))
# print(iter(list1))
# print(iter(tup1))
# print(iter(dict1))
# print(iter(set1))

# class MyObject:
    
#     def __init__(self):
#         pass     
#     def __getitem__(self, index):
#         pass  
# # MyObject() 支持序列协议
# print(iter(MyObject()))

# class MyObject1:
    
#     def __init__(self):
#         self.num = 3     
#     def __call__(self):
#         self.num += 1
#         return self.num  
# """
# 有第二个参数 sentinel = 7, 且 MyObject1() 是可调用对象, 则每次迭代时
# 调用 MyObject1()() 即调用 __call__方法, 当结果为 sentinel 时, 
# 触发StopIteration, 被list捕获, 停止迭代 """

# call_iter = iter(MyObject1(), 8)
# print(call_iter)
# print(list(call_iter))  # [4, 5, 6]

# # next(iterator[, default])
# # 通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration

# str_iterator = iter("abcd")
# print(next(str_iterator))  # "a"
# print(next(str_iterator))  # "b"
# print(next(str_iterator))  # "c"
# print(next(str_iterator))  # "d"
# print(next(str_iterator, "ef"))  # 迭代耗尽, 返回 "ef"
# print(next(str_iterator))  # 迭代耗尽, 触发 StopIteration


# # 迭代器的优缺点
# # 迭代器优点:
# # 提供了一种不依赖索引的迭代取值方式

# # 节省内存，迭代器在内存中相当于只占一个数据的空间：因为每次取值上一条数据
# # 都会在内存释放，再加载当前的此条数据，而不需要一次性把所有数据加载到内存
# # 当中

# # 执行列表推导式：sum([i for i in range(10000000000)])  的内存使用情况
# # 16G 用满


# # 执行生成器表达式：sum(i for i in range(10000000000)) 的内存使用情况
# # 基本不用

# # 迭代器缺点:
# # 取值不如按照索引的方式灵活，不能取指定的某一个值，只能往后取，不能往前去
# # 除非取尽，否则无法获取迭代器的长度


# ''' =================================模块&包================================'''

# 模块可以被别的程序引入，以使用该模块中定义的变量和函数等功能
# 习惯上（但不强制要求）把所有 import 语句放在模块的开头
# 一个模块被另一个程序导入时，会执行该模块
# 一个模块只会被另一个程序导入一次

# 模块导入
# import module1[, module2[,... moduleN]]
# import module1 as alias1[, module2 as alias2[,... moduleN as aliasN]]
# from module import item1[, item2[,... itemN]]
# from module import item1 as alias1[, item2 as alias2[,... itemN as aliasN]]
# from module import *

# 注意：请慎用 from module import * ，很容易出现名称重复的情况，导致出现一些意外的问题
 
# 模块搜索路径 
 
# sys 模块的 path 变量包含了 Python 解释器自动查找所需模块的路径的列表
# 如果这些路径都找不到，则会报错：ModuleNotFoundError: No module named 'xxx'

import sys  
print(sys.path)

# __name__属性

# 每个模块都有一个__name__属性，当其值是 '__main__' 时，说明该模块自身在运行，否则说明该模块被导入，其值为模块名在完成一个模块的编写之前，我们一般会对模块中的功能进行测试，看看各项功能是否正常运行。对于这些测试的代码，我们希望只在直接运行这个py文件的时候
# 执行，而在用其他的程序导入这个模块的时候不要执行。这个时候就可以借助__name__属性来实现


# print('在该模块自身运行时会执行')
# print('在该模块被导入时也会执行')  
# if __name__ == '__main__':
#     print('在if语句下的程序块仅在该模块自身运行时才执行')
# else:
#     print('在else子句下的程序块在该模块自身运行时不会执行')
#     print('但是在被导入时, 会执行')

# 包的概念
# Python包实际上就是一个文件夹，只是该文件夹里面一定包含 __init__.py 模块
# 和文件夹一样，包里面还可以装其他的包

# 包的作用
# 避免相同命名冲突： 如果在同一个包里，是不允许两个模块命名相同的，但是如
# 果不在同一个包里，是可以的
# 模块分区： 把不同功能的模块归类到不同的包里，方便查询和修改。在比较大型
# 的项目中常常需要编写大量的模块，此时我们可以使用包来对这些模块进行管理

# 包的导入
# import package1[, package2[,... packageN]]
# import package1 as alias1[, package2 as alias2[,... packageN as aliasN]]
# from package import module1[, module2[,... moduleN]]
# from package import module1 as alias1[, module2 as alias2[,... moduleN as aliasN]
# from package.module import item1[, item2[,... itemN]]
# from package.module import item1 as alias1[, item2 as alias2[,... itemN as aliasN]]

# ''' =================================文件操作&路径操作================================'''
# # open(file, mode='r', encoding=None) 

# # file：文件路径（相对路径或绝对路径）
# # mode：文件打开的模式，默认为 'r' 模式
# # encoding：编码方式（只用在文本模式下），默认依赖平台，通常设置为 'UTF-8'
# # 打开 file 对应的文件，返回一个文件对象；如果该文件不能被打开，则引发 
# # OSError

# from typing import Iterator  
# file = open(r'./t01.txt', mode='a')
# file.write('hello world')
# file.write('\nhello China')
# file.write('\nhello Baby')
# file.close()  

# file = open(r'./t01.txt')
# print(isinstance(file, Iterator))
# # print(list(file))
# for i in file:
#     print(i)

# # mode 常用模式：
# # r 以只读方式打开文件。文件的指针将会放在文件的开头。
# # w 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原
# # 有内容会被删除。如果该文件不存在，创建新的文件再写入。
# # a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是
# # 说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写
# # 入。
# # + 如果要以读写模式打开，加上 + 即可，比如：r+、w+、x+、a+
# # b 默认为文本模式，如果要以二进制模式打开，加上 b 即可，比如：rb、rb+、wb、wb+

# # file 常用对象方法
    
# # file.read(size=-1) 
# # 从 file 中读取至多 size 个字符并返回
# # 如果 size 为负值或 None，则读取至 EOF（End Of File）

# with open(r"./t01.txt") as file:
#     print(file.read(5))
#     print(file.read(2))
#     print(file.read())

# # file.write(s)
# # 将字符串 s 写入到流并返回写入的字符数
# with open(r"./t01.txt", mode='a') as file:
#     num = file.write('\nhello baby')
#     print(num)

# # file.flush()
# # 刷新缓冲区，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要被动的等待缓冲区写入。一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法
    
# import time  
# file = open(r"./t01.txt", mode='a')
# file.write('\n123456789')
# time.sleep(5)  # 文件需要等到关闭文件时才会把数据从缓冲区写入文件
# file.close()  # 关闭文件，自动刷新缓冲区，数据才写入文件

# file = open(r"./t01.txt", mode='a')
# file.write('\n123456789')
# file.flush()  # 刷新缓冲区，数据立刻写入文件
# time.sleep(5)
# file.close()

# # file.close()
# # 刷新缓冲区并关闭该文件。如果文件已经关闭，则此方法无效
# # 文件关闭后，对文件的任何操作（如：读取或写入）都会引发 ValueError 

# file = open(r'./t01.txt')
# print(file.read())
# file.close()
# file.close()  # 多次调用该方法，只有第一个调用才会生效
# # file.read()  # 引发ValueError

# # file.writelines(lines)
# # lines：Iterable[str]
# # 向文件写入一个字符串序列，不会自动添加分隔符

# tup = ("a\n", 'bc\n', "def")
# with open(r"./t01.txt", mode="a+") as file:
#     file.writelines(tup)

# # file.readline(size=-1)
# # 从文件中读取并返回一行，如果指定了 size，将至多读取 size 个字符
# with open("./t01.txt") as file:
#     print(file.readline())
#     print(file.readline(1))
#     print(file.readline())

# # file.readlines(hint=-1)
# # 从文件中读取并返回包含多行的列表
# # hint：默认为 -1，代表读取所有行（也可以指定读取的字符数，如果要读取的字
# # 符数超过一行，则按照两行读取，超过两行则按照三行读取，依次类推）
    
# with open("./t01.txt") as file:
#     print(file.readlines()) 
# with open("./t01.txt") as file:
#     print(file.readlines(11))

# # with 语句
# # 这种写法如果在open之后close之前发生未知的异常，就不能确保打开的文件一定
# # 被正常关闭，这显然不是一个好的做法
# # file = open(r'./t01.txt', mode='w')
# # file.write('hello world')
# # ...
# # ...
# # file.close()
# # 所以可以使用下面这种写法，确保close一定会被执行
    
# # file = open(r'./t01.txt', mode='w')
# # try:
# #     file.write('hello world')
# #     ...
# #     ...
# # finally:
# #     file.close()

# # 用 with 语句将会是一种更加简洁、优雅的方式
# with open(r'./t01.txt', mode='w') as file:
#     file.write('hello world')

# # 路径操作
# # os.getcwd()
# # 返回表示当前工作目录的字符串

# import os 
# print(os.getcwd())

# # os.listdir(path)
# # 返回 path 指定的文件夹包含的文件或文件夹的名字的列表
# import os 
# li = os.listdir(os.getcwd())
# print(li)

# # os.makedirs(name, exist_ok=False)
# # 递归创建目录，并且还会自动创建到达最后一级目录所需要的中间目录
# # 如果 exist_ok 为 False (默认值)，则如果目标目录已存在将引发 FileExistsError
# import os 
# os.makedirs('./dir1/dir2/dir3', exist_ok=True)
# # 文件路径
# file_path = './dir1/dir2/dir3/a.txt'

# # 创建并打开文件进行写入
# with open(file_path, 'w') as file:
#     file.write('您好，这是一个测试文件。')

# # os.path.basename(path)
# # 返回路径 path 最后一级的名称，通常用来返回文件名
# print(os.path.basename(os.getcwd()))

# # os.path.dirname(path）
# # 返回路径 path 的目录名称
# print(os.path.dirname(os.getcwd()))

# # os.path.split(path)
# # 把路径分割成 dirname 和 basename，返回一个元组
# print(os.path.split(os.getcwd()))

# # os.path.splitext(path)
# # 把路径中的扩展名分割出来，返回一个元组
# print(os.path.splitext('./dir1/dir2/dir3/a.txt'))

# # os.path.exists(path)
# # path 路径存在则返回 True，不存在或失效则返回 False
# path = "./dir3/dir2/dir1/a.txt"
# if os.path.exists(path):
#     print("文件存在")
#     with open(path) as file:
#         print(file.read())
# else:
#     print("文件不存在")

# # os.path.isfile(path)
# # 判断路径是否为文件，返回 True 或 False
# print(os.path.isfile('./dir1/dir2/dir3/a.txt'))
# print(os.path.isfile("./dir3/dir2/dir1/a.txt"))
# print(os.path.isfile(os.getcwd()))

# # os.path.isdir(path)
# # 判断路径是否为目录，返回 True 或 False
# print(os.path.isdir('./dir1/dir2/dir3'))
# print(os.path.isdir("./dir3/dir2/dir1"))
# print(os.path.isdir(os.getcwd()))

# # os.path.join(path, *paths)
# # 智能地拼接一个或多个路径部分
# print(os.path.join("./dir3/dir2", "dir1/a.txt"))


# # json 格式 
# # 字符串可以很轻松地写入文件并从文件中读取出来，而其他类型（比如：字典）复杂的数据会变得相当麻烦，因为 read() 方法返回字符串。Python 允许你使用 json 格式，并提供了名为 json 的标准模块，它可以将 Python 数据结构转化为 json 格式的字符串（这个过程称之为序列化），也可以将 json 格式的字符串重建成 Python 数据结构（这个过程称之为反序列化）。json 是一个文本序列化格式，可直观阅读。注意：json 中的键值对的键，永远是 str 类型。当一个对象被转化为 json 时，字典中所有的键都会被强制转换为字符串，导致当字典被转换为 json 然后转换回字典时可能和原来不相等

# import json  
# info = {'name': 'Tom', 'age': 18, 1: 'one'}
# print(type(info), info) 
# with open("info.json", mode="w") as f:
#     info_str = json.dumps(info)  # 序列化
#     print(type(info_str), info_str)
#     f.write(info_str) 

# with open("info.json") as f:
#     content = f.read()
#     print(type(content), content)
#     res = json.loads(content)  # 反序列化
#     print(type(res), res)

# # pickle 格式 
# # pickle 是一个Python专用的二进制序列化格式，不可直观阅读

# import pickle  
# info = {'name': 'Tom', 'age': 18, 1: 'one'}
# print(type(info), info) 
# with open("info.pickle", mode="wb") as f:
#     info_byte = pickle.dumps(info)
#     print(type(info_byte), info_byte)
#     f.write(info_byte) 
# with open("info.pickle", mode="rb") as f:
#     content = f.read()
#     print(type(content), content)
#     res = pickle.loads(content)
#     print(type(res), res)

# # xml 格式
# # XML文件格式是纯文本格式。XML文档的第一句是声明语句，紧接着声明后面建立的第一个元素是根元素（有且只有一个），其他元素都是这个根元素的子元素，每个XML元素包括一个开始标签，一个结束标签，以及两个标签之间的内容，每个元素还可以存在对应的属性


# import xml.etree.ElementTree as ET  

# # 创建XML文件

# import xml.etree.ElementTree as ET

# # 创建根元素 <doc>
# root = ET.Element("doc")

# # 创建 <outputs>
# outputs = ET.SubElement(root, "outputs")

# # 创建 <object>
# object_elem = ET.SubElement(outputs, "object")

# # 创建 <item>
# item = ET.SubElement(object_elem, "item")

# # 创建第一个 <bndbox> 元素
# bndbox1 = ET.SubElement(item, "bndbox")
# ET.SubElement(bndbox1, "xmin").text = "0"
# ET.SubElement(bndbox1, "ymin").text = "0"
# ET.SubElement(bndbox1, "xmax").text = "0"
# ET.SubElement(bndbox1, "ymax").text = "0"

# # 创建第二个 <bndbox> 元素
# bndbox2 = ET.SubElement(item, "bndbox")
# ET.SubElement(bndbox2, "xmin").text = "10"
# ET.SubElement(bndbox2, "ymin").text = "20"
# ET.SubElement(bndbox2, "xmax").text = "30"
# ET.SubElement(bndbox2, "ymax").text = "40"

# # 构建树结构
# tree = ET.ElementTree(root)

# # 写入到 XML 文件
# tree.write("TestFile.xml", encoding='utf-8', xml_declaration=True)


# # 将xml文档解析为元素树
# tree = ET.parse(r"TestFile.xml")
# # 返回该树的根元素, 即 <doc>
# root = tree.getroot() 

# # 检查根元素的类型是否为 ET.Element
# print(f'Element 类型的实例: {type(root) is ET.Element}')  # 输出 True 如果根元素是 Element 类型的实例

# # 遍历找到所有 'outputs/object/item/bndbox' 路径下的元素
# for bndbox in root.findall('outputs/object/item/bndbox'):
#     # 打印 bndbox 元素的属性字典
#     print(f'bndbox 元素的属性: {bndbox.attrib}')  # 如果 bndbox 有属性则打印，否则打印空字典

#     # 分别打印每个坐标点的值
#     print(f'xmin: {bndbox.findtext("xmin")}')
#     print(f'ymin: {bndbox.findtext("ymin")}')
#     print(f'xmax: {bndbox.findtext("xmax")}')
#     print(f'ymax: {bndbox.findtext("ymax")}')

#     # 使用 find 方法获取特定子元素并打印其文本内容
#     print(f'xmin (使用 find): {bndbox.find("xmin").text}')
#     print(f'ymin (使用 find): {bndbox.find("ymin").text}')
#     print(f'xmax (使用 find): {bndbox.find("xmax").text}')
#     print(f'ymax (使用 find): {bndbox.find("ymax").text}')


# ''' =================================正则表达式================================'''

# GPT完成

