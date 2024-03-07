'''


import keyword  

print(keyword.kwlist)

import builtins

print(dir(builtins))
pi = 3.141592653  # 变量
PI = 3.141592653  # 约定为常量，本质还是变量

print('hello world')
print(1, 2, 3, sep='-', end='-456')
with open('./abc.txt', 'w') as f:
    # 把12345直接写入abc.txt文件
    # 控制台不会有输出结果
    print(12345, file=f)

import time  
"""
flush为False时, 每次循环执行的输出会被缓存, 而不会立即展示在终端,
等到循环执行完毕时, 才把缓存一次性输出在终端。
flush为True时, 每次循环都会刷新一次结果, 即每次输出都会立即展示在终端
"""
for i in range(20):
    print('.', end='', flush=True)
    time.sleep(0.5)  # 延迟0.3秒再往后执行

name = input('请输入你的姓名: ')
print(name, '你好, 很高兴认识你!')




'''
lst = [567, 'hello', 78.9, 'world', False] 
"""
修改某一个元素:
lst[index] = object
"""
lst[2] = 9.87
lst[3] = 'dlrow'
print(lst) 
"""
修改一个或者多个元素:
lst[start: end: step] = iterable
"""
# 修改一个元素, 1 => 1
lst[2:3] = [9.87] 
print(f"1{lst}")

# 修改一个元素, 1 => n
lst[2:3] = [7, 8, 9] 
print(f"2{lst}")

# 删除一个元素, 1 => 0
lst[2:3] = [] 
print(f"3{lst}")

# 修改多个连续的元素, n => n
lst[2:4] = [9.87, 'dlrow'] # 修改多个连续的元素, n => m
print(f"4{lst}")

# 修改多个连续的元素, n => m
lst[2:4] = [1, 2, 3]
print(f"5.1{lst}")
lst[1:4] = [1, 2] 
print(f"5.2{lst}")

# 删除多个连续的元素, n => 0
lst[1:4] = ['3434'] 
print(f"6{lst}")

# 修改多个非连续的元素, 只能 n => n
lst[1::2] = ['a','5555'] 
print(f"7{lst}")

# 插入一个元素
lst[0:0] = ['a']
print(f"8{lst}")
lst[1:1] = ['b']
print(f"9{lst}")
lst[len(lst):] = ['c'] 
print(f"10{lst}")

# 插入多个元素
lst[0:0] = ['a', 'b', 'c']
print(f"11{lst}")
lst[1:1] = ['d', 'f']
print(f"12{lst}")
lst[len(lst):] = ['x', 'y', 'z']
print(f"13{lst}")

print(list())
print(list("hello"))
print(list((1, 2, 3)))

# 字典作为一个iterable, 只有键参与迭代
print(list({1: 2, 3: 4}))
print(list({'a', 'b', 'c', 789, 456}))


lst = [1, 2, 3] 
lst.append(4)
print(f"13{lst}")

lst.append([5, 6])
print(f"14{lst}")

lst = [1, 2, 3] 
lst.extend([5, 6])
print(f"15{lst}")

lst = [1, 2, 3, 4]
lst.insert(1, ['a', 'b'])
print(f"16{lst}")

lst = [1, 2, -5, -3] # 升序排序
lst.sort()
print(f"17{lst}")

# 降序排序
lst.sort(reverse=True)
print(f"18{lst}")

"""
对lst中的元素按照绝对值的大小降序排序

把lst中的每个元素依次作为实参传递给key所指定的函数去调用, 即:
abs(1), abs(2), abs(-5), abs(-3)
返回值分别为: 1, 2, 5, 3
根据返回值的大小对原数据进行排序
"""

lst.sort(key=abs, reverse=True)
print(f"19{lst}")

lst = [1, 2, -5, -3] # 升序排序
print(f"20{sorted(lst)}") # 降序排序
print(f"21{sorted(lst, reverse=True)}") # 对lst中的元素按照绝对值的大小降序排序
print(f'22{sorted(lst, key=abs, reverse=True)}') # 对字符串排序
print(f"23{sorted('hello world')}")

lst = [1, 3, 5, 2]
lst.reverse()
print(f"24{lst}")

lst = [1, 3, 5, 2]
obj = reversed(lst)
print(f"25{list(obj)}") 

string = 'hello'
obj = reversed(string)
print(f"26{list(obj)}")

lst = [1, 2, 3, 2, '23', [2, 4]]
print(f"27 {lst.count(2)}")

lst = [1, 2, 3, 2, '23', [2, 4]]
print(f"28 {lst.index(2)}")

# print(f"29{lst.index(2, 4)}")  # ValueError

lst = [567, 'hello', True, False, 456]
print(f"30 {lst.pop(1)}")  # 'hello'
print(f"31 {lst.index(567)}")

lst = [1, 2, 4, 2, 3, 3] 
lst.remove(2)
print(f"32 {lst}")

lst.remove(2)
print(f"33 {lst}")

lst = [567, 'hello', True, False, 456]
new_lst = lst.copy()
print(f"34 {new_lst}")

lst = [567, 'hello', True, False, 456]
lst.clear()
print(f"35 {lst}")  # []

''' =======================元组======================= '''
# 空元组
tup = () # 元组中只有一个元素时, 逗号不能省略
tup = (789,) # 这不是元组，仍为数字789
tup = (789) # 封包
tup = 'China', 1997, 2000 
tup = ('China', 1997, 2000)
# 元组是不可变的, 但其中的可变成员仍然可以被改变
tup = (456, 'hello', ([789, 'world'],))
tup[-1][0][0] = 987
print(f"36 {tup}")
print(f"37 {tuple()}")
print(f"38 {tuple('hello')}")
print(f"39 {tuple([1, 2, 3])}")
# 字典作为一个iterable, 只有键参与迭代
print(f"40 {tuple({1: 2, 3: 4})}")
print(f"41 {tuple({'a', 'b', 'c', 789, 456})}")
tup = (1, 2, 3, 2, '23', [2, 4])
print(f"42 {tup.count(2)}")
tup = (1, 2, 3, 2, '23', [2, 4])
print(f"43 {tup.index(2)}")
# print(tup.index(2, 4))  # ValueError


''' =======================字典======================= '''
d = {'name': 'Tom', 'age': 28}
print(f"44 {d}")

d = {}  # d = dict()
d['name'] = 'Tom'
d['age'] = 26
print(f"45 {d}")

d = dict(name='Tom', age=28)
print(f"46 {d}")

d = dict([('name', 'Tom'), ('age', 28)])
print(f"47 {d}")

d = dict(zip(['name', 'age'], ['Tom', 28]))
print(f"48 {d}")

d1 = dict.fromkeys(('name', 'age', 'height'))
print(f"49 {d1}")

d2 = dict.fromkeys(('name', 'age', 'height'), 'abc')
print(f"50 {d2}")

print(f"51 {dict()}")

print(f"52 {dict(one=1, two=2, three=3)}")

print(f"53 {dict(zip(['one', 'two', 'three'], [1, 2, 3]))}")

print(f"54 {dict([('one', 1), ('two', 2), ('three', 3)])}")

obj = zip('abcd', [4, 5, 7, 1])
print(f"55 {list(obj)}")

obj = zip('abcd', [4, 5, 7])
print(f"56 {list(obj)}")

obj = zip('abcd')
print(f"57 {list(obj)}")

obj = zip()
print(f"58 {list(obj)}")

dic1 = dict.fromkeys(("name", "age", "gender"))
print(f"59 {dic1}")

dic2 = dict.fromkeys(("name", "age", "gender"), "I don't know!")
print(f"60 {dic2}")

d = {'Name': 'Tom', 'Age': 7, 'Class': 'First'}
print(f"61 {d['Name']}")
print(f"62 {d['Age']}")

# 如果指定的键不存在, 则报错
# print(f"63 {d['Gender']}") # 此行将会报错，因为 'Gender' 不在字典 d 中

d = {'Name': 'Tom', 'Age': 7, 'Class': 'First'}
# 修改指定键所对应的值
d['Name'] = 'Tony'
d['Age'] = 8
print(f"64 {d}")

# 如果指定的键不存在, 则新增该键值对
d['Gender'] = 'male'
print(f"65 {d}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
view_keys = d.keys()
print(f"66 {view_keys}")

# 修改字典
d['weight'] = 59
print(f"67 {view_keys}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
view_values = d.values()
print(f"68 {view_values}")

# 修改字典
d['weight'] = 59
print(f"69 {view_values}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
view_items = d.items()
print(f"70 {view_items}")

# 修改字典
d['weight'] = 59
print(f"71 {view_items}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
print(f"72 {d.get('age')}")
print(f"73 {d.get('weight')}")
print(f"74 {d.get('weight', '该键不存在')}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
d.update(age=18, weight=59)
d.update({'age': 18, 'weight': 59})
d.update(zip(['age', 'weight'], [18, 59]))
d.update([('age', 18), ('weight', 59)])
print(f"75 {d}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
print(f"76 {d.pop('height')}")
print(f"77 {d}")

print(f"78 {d.pop('weight', None)}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
print(f"79 {d.popitem()}")
print(f"80 {d}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
print(f"81 {d.setdefault('age')}")
print(f"82 {d.setdefault('weight')}")
print(f"83 {d}")

print(f"84 {d.setdefault('gender', 'male')}")
print(f"85 {d}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
new_d = d.copy()
print(f"86 {new_d}")

d = {'name': 'Tom', 'age': 15, 'height': 162}
d.clear()
print(f"87 {d}")



''' =======================集合======================= '''
# 空集合
s = set()
print(f"88 {s}")  # 空集合

d = {}  # d = dict()
print(f"89 {d}")  # 空字典

# 集合中不能存在可变的数据
s = {789, 456, "hello", (135,), 'world'}
print(f"90 {s}")

print(f"91 {set()}")
print(f"92 {set('hello')}")
print(f"93 {set([1, 2, 3])}")
print(f"94 {set((1, 2, 3))}")

# 字典作为一个iterable, 只有键参与迭代
print(f"95 {set({1: 2, 3: 4})}")

# 把iterable变成集合，就会自动去掉重复的元素
lst = [1, 2, 4, 5, 7, 7, 4, 5]
s = set(lst)
print(f"96 {list(s)}")

# 集合可以利用操作符做关系测试
a = set('abdefga')
b = set('abc')
c = set('aef')
print(f"97 {a >= b}")  # 判断a是否为b的父集
print(f"98 {c <= a}")  # 判断c是否是a的子集
print(f"99 {c < a}")   # 判断c是否是a的真子集
print(f"100 {a - b}")  # 返回a和b的差集
print(f"101 {b - a}")  # 返回b和a的差集
print(f"102 {a | b}")  # 返回a和b的并集
print(f"103 {a & b}")  # 返回a和b的交集
print(f"104 {a ^ b}")  # 返回a和b的对称差集

# 优先级: -  &  ^  |
print(f"105 {a - b | c ^ b & a}")

s = '12'
lst = [1, '2']
d = {1: '1', 2: '2'} 
set1 = {'1', '2', 1, 3}
set1.update(s, lst, d)
print(f"106 {set1}")

s = {1, 2, 3}
s.add("hello world")
print(f"107 {s}")

s = {1, 2, 3, 4} 
s.remove(3)
print(f"108 {s}")

s = {1, 2, 3, 4} 
s.discard(3)
s.discard(3)
s.discard(3)
print(f"109 {s}")

s = {'1', '2', 'hello', 789}
print(f"110 {s.pop()}")
print(f"111 {s}")

set1 = {'1', '2', 1, 3}
set2 = set1.copy()
print(f"112 {set2}")

s = {'1', '2', 'hello', 789}
s.clear()
print(f"113 {s}")

