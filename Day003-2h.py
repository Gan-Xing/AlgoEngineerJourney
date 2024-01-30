
''' =======================序列索引======================= '''
string = 'Hello 1牛3 Python' 
"""
正向索引和反向索引都可以使用
步长默认为1, 取连续的数据
"""
print(string[7: 11])  # '牛3 P'
print(string[-9: -5])  # '牛3 P'
print(string[7: -5])  # '牛3 P'
print(string[-9: 11])  # '牛3 P' 
""" 步长为2, 取数据时要隔一个再取 """
print(string[7: 14: 2])  # '牛 yh' 
""" 步长为3, 取数据时要隔两个再取 """
print(string[7: 14: 3])  # '牛Ph' 
""" 步长为负数, 表示从右往左取数据 """
print(string[10: 6: -1])  # 'P 3牛' 
""" 步长为-2, 表示从右往左隔一个取数据 """
print(string[13: 6: -2])  # 'hy 牛' 
""" 步长为正数, start没有指定, 默认为0 """
print(string[: 3])  # 'Hel'
print(string[0: 3]) 

""" 步长为负数, start没有指定, 默认为-1 """
print(string[: 12: -1])  # 'noh'
print(string[-1: 12: -1]) 
""" 步长为正数, end没有指定, 默认为len(string) """
print(string[13:])  # 'hon'
print(string[13:len(string)]) 
""" 步长为负数, end没有指定, 默认为-len(string)-1 """
print(string[2::-1])  # 'leH'
print(string[2:-len(string)-1:-1]) 
""" 把该序列复制一份 """
print(string[:]) 
""" 把该序列倒过来 """
print(string[::-1]) 
""" start到end是从左往右，但step表示从右往左 """
print(string[1: 3: -1])  # ''
""" 类比0维数据 """
item1 = 1
item2 = 2
item3 = 3
item4 = 4
item5 = 5
item6 = 6
item7 = 7
item8 = 8
item9 = 9 
""" 类比1维数据 """
lst1 = [item1, item2, item3]
lst2 = [item4, item5, item6]
lst3 = [item7, item8, item9]
# 对1维数据索引，结果为0维数据
print(lst1[0])  # 1
print(lst2[1])  # 5
print(lst3[2])  # 9
# 无论怎么切片，维度保持不变
print(lst1[::2])  # [1, 3]
print(lst2[1:2])  # [5]
print(lst3[::2][1:2])  # [9] 
""" 类比2维数据 """
lst4 = [lst1, lst2, lst3]
# 对2维数据索引，结果为1维数据
print(lst4[0])  # [1, 2, 3]
print(lst4[1])  # [4, 5, 6]
print(lst4[2])  # [7, 8, 9]
# 并且每索引一次，降低一次维度
print(lst4[0][1])  # 2
# 无论怎么切片，维度保持不变
print(lst4[::2])  # [[1, 2, 3], [7, 8, 9]]
print(lst4[1:2])  # [[4, 5, 6]]
print(lst4[::2][1:2])  # [[7, 8, 9]]

print(len('abcd'))
print(len([1, 2, 3, 4]))
print(len((1, 2, 3, 4)))


''' =======================del 语句======================= '''

lst1 = [567, 'hello', 456, [912, 923], 'world']
lst2 = lst1 
del lst1
print(lst2) 
del lst2[1]
print(lst2) 
del lst2[0], lst2[2]
print(lst2) 
del lst2[:3:2]
print(lst2) 
del lst2[0][1]
print(lst2) 
del lst2[:]
print(lst2)


'''  ======================= 作业2 ======================='''

lst1 = [3, 1, 2]
lst2 = [4, 5, 6]

# 程序实现: 把lst2中的元素添加到lst1中, 并对lst1进行降序排序
lst1.extend(lst2)
lst1.sort(reverse=True)
print(lst1)

lst1 = [1, 2]
lst2 = [3, 4]
lst3 = [5, 6]

# 程序实现: 把lst1, lst2作为元素添加到lst3中, 并求lst3的长度

lst3.append(lst1)
lst3.append(lst2)
# 将lst1和lst2作为元素添加到lst3中
lst3.append(lst1)
lst3.append(lst2)
# 求lst3的长度
length_of_lst3 = len(lst3)
print(length_of_lst3)


lst = [1, 3, 2, 6, 4]
#程序实现: 删除lst元素中的中位数（只考虑列表中元素个数为奇数的情况）
# 对列表进行排序
lst.sort()
# 找到中位数
median = lst[len(lst) // 2]
# 删除中位数
lst.remove(median)


lst = [1, 3, 2, 6, 1, 1, 41]
#程序实现: 求lst最后一个元素1的索引
lst = [1, 3, 2, 6, 1, 1, 41]

# 从列表末尾开始向前搜索
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 1:
        print("索引:", i)
        break



'''  ======================= 赋值 ======================= '''
str1 = 'abc'
str2 = 'cba'
print(f"id(str1): {id(str1)}")
print(f"id(str2): {id(str2)}")

a = 789
b = a
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

# 在交互式环境中
a = 789
b = 789
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

import copy

# 浅拷贝示例
print("浅拷贝示例:")
a = [789]
b = [789]
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

# 小整数对象池
a = 256
b = 256
print(f"\n小整数对象池:")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

# 可变数据的共享引用
a = [789]
b = a
b.append(456)
print(f"\n可变数据的共享引用:")
print(f"b: {b}")  # [789, 456]
print(f"a: {a}")  # [789, 456]

# 浅拷贝实例
data = (456, 'hello', (789,), ['world'])
new_data = copy.copy(data)
print(f"\n浅拷贝实例（元组）:")
print(f"id(data): {id(data)}")
print(f"id(new_data): {id(new_data)}")

data = [456, 'hello', (789,), ['world']]
new_data = copy.copy(data)
print(f"\n浅拷贝实例（列表）:")
print(f"id(data): {id(data)}")
print(f"id(new_data): {id(new_data)}")

print(f"id(data[0]): {id(data[0])}")
print(f"id(new_data[0]): {id(new_data[0])}")

print(f"id(data[1]): {id(data[1])}")
print(f"id(new_data[1]): {id(new_data[1])}")

print(f"id(data[2]): {id(data[2])}")
print(f"id(new_data[2]): {id(new_data[2])}")

print(f"id(data[3]): {id(data[3])}")
print(f"id(new_data[3]): {id(new_data[3])}")

# 深拷贝示例
data = [456, 'hello', (789,)]
new_data = copy.deepcopy(data)
print(f"\n深拷贝示例(列表中不存在可变成员):")
print(f"id(data): {id(data)}")
print(f"id(new_data): {id(new_data)}")
print(f"id(data[0]): {id(data[0])}")
print(f"id(new_data[0]): {id(new_data[0])}")
print(f"id(data[1]): {id(data[1])}")
print(f"id(new_data[1]): {id(new_data[1])}")
print(f"id(data[2]): {id(data[2])}")
print(f"id(new_data[2]): {id(new_data[2])}")

data = (456, 'hello', ['world'], (789, {}))
new_data = copy.deepcopy(data)
print(f"\n深拷贝示例（元组中包含可变元素）:")
print(f"id(data): {id(data)}")
print(f"id(new_data): {id(new_data)}")
print(f"id(data[0]): {id(data[0])}")
print(f"id(new_data[0]): {id(new_data[0])}")
print(f"id(data[1]): {id(data[1])}")
print(f"id(new_data[1]): {id(new_data[1])}")
print(f"id(data[2]): {id(data[2])}")
print(f"id(new_data[2]): {id(new_data[2])}")
print(f"id(data[3]): {id(data[3])}")
print(f"id(new_data[3]): {id(new_data[3])}")

data = [1, '原始值', [3, 4]]
new_data = copy.deepcopy(data)

# 修改前的 ID
print(f"原始 data[1] 的 ID: {id(data[1])}")
print(f"拷贝 new_data[1] 的 ID: {id(new_data[1])}")

# 修改 new_data[1]
new_data[1] = '新的值'

# 修改后的 ID
print(f"修改后 new_data[1] 的 ID: {id(new_data[1])}")


''' ===============================运算符&&优先级==============================='''
# 增强赋值和普通赋值的区别
lst1 = [1, 2]
lst2 = [3, 4, 5]
print(f"lst1 初始 id: {id(lst1)}")
lst1 += lst2  # inplace操作
print(f"lst1 增强赋值后 id: {id(lst1)}")
print(f"lst1 内容: {lst1}")

lst1 = [1, 2]
lst2 = [3, 4, 5]
print(f"\nlst1 重新赋值前 id: {id(lst1)}")
lst1 = lst1 + lst2  # 新建操作
print(f"lst1 重新赋值后 id: {id(lst1)}")
print(f"lst1 内容: {lst1}")

# 基本序列赋值
string = 'hello world'
print(f"\n字符串长度 + 5 = {len(string) + 5}")
print(f"string 的长度为: {len(string)}")

# 使用赋值表达式 (:=) 来捕获表达式的值
print(f"\n字符串长度 + 5 = {(length := len(string)) + 5}")
print(f"string 的长度为: {length}")

# 多目标赋值
a = b = c = 999
print(f"\na, b, c 同时赋值为 999:")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

a = b = c = [1, 2, 3]
print(f"\na, b, c 同时赋值为相同列表:")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
b.append(4)
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# 逻辑运算符和短路机制
a = 2
b = 'hello'
c = []
d = 0
print(f"\nc and a: {c and a}")  # []
print(f"a and c: {a and c}")  # []
print(f"d and c: {d and c}")  # 0
print(f"c and d: {c and d}")  # []
print(f"a and b: {a and b}")  # 'hello'
print(f"b and a: {b and a}")  # 2
print(f"a or c: {a or c}")  # 2
print(f"c or a: {c or a}")  # 2
print(f"b or a: {b or a}")  # 'hello'
print(f"a or b: {a or b}")  # 2
print(f"c or d: {c or d}")  # 0
print(f"d or c: {d or c}")  # []
print(f"not a: {not a}")  # False
print(f"not b: {not b}")  # False
print(f"not c: {not c}")  # True
print(f"not d: {not d}")  # True


# 成员运算符
tup = ('0', ' ', 'None', 'False', '[]')
print(f"\nall(tup): {all(tup)}")  # True
print(f"all([]): {all([])}")  # True

tup = (0, '', None, False, [])
print(f"\nany(tup): {any(tup)}")  # False
print(f"any([]): {any([])}")  # False

string = 'hello world'
print(f"'e' in string: {'e' in string}")
print(f"'lo' in string: {'lo' in string}")
print(f"'ol' not in string: {'ol' not in string}")

# 身份运算符
a = 256
b = 256
print(f"\na == b: {a == b}")
print(f"a is b: {a is b}")
print(f"id(a) == id(b): {id(a) == id(b)}")

a = 257
b = 257
print(f"\na == b: {a == b}")
print(f"a is b: {a is b}")
print(f"id(a) == id(b): {id(a) == id(b)}")

a = [257]
b = [257]
print(f"\na == b: {a == b}")
print(f"a is b: {a is b}")
print(f"id(a) == id(b): {id(a) == id(b)}")

# 位运算符
# "对应位"（Bitwise）是指两个数字在二进制形式下相同位置上的位。在进行位运算时，这些二进制位是逐位进行比较的。

# 以 `a = 5` 和 `b = 3` 为例，首先我们需要知道它们的二进制表示：

# - `a = 5` 的二进制表示是 `0101`。
# - `b = 3` 的二进制表示是 `0011`。

# 在这两个二进制数中，我们从右到左逐位进行比较和运算。对于按位与运算（`&`），只有当两个数字在某位都为1时，结果在那一位才为1，否则为0。

# - 第一位（最右边）：`1 & 1` 等于 `1`。
# - 第二位：`0 & 1` 等于 `0`。
# - 第三位：`1 & 0` 等于 `0`。
# - 第四位（最左边）：`0 & 0` 等于 `0`。

# 因此，`a & b` 的结果是 `0001`，即二进制的 `1`。所以 `result = a & b` 的值是 `1`。

# & 按位'与'：如果两个相应位都为1，则该位的结果为1，否则为0
# | 按位'或'：如果两个相应位至少有一个为1，则该位的结果为1，否则为0
# ^ 按位'异或'：只要两个相应位不同，该位的结果就为1
# ~ 按位'取反'：对每一位取反（包括符号位），~x 等于 -(x+1)
# << 按位'左移'：各个位全部左移若干位，右边补0，x << n 等于 x * 2 ** n
# >> 按位'右移'：各个位全部右移若干位，左边补对应的符号位值，x >> n 等于 x // 2

# 按位与运算
a = 5  # 0101
b = 3  # 0011
result = a & b  # 0001
print(f"5 & 3 = {result}")

# 按位或运算
result = a | b  # 0111
print(f"5 | 3 = {result}")

# 按位异或运算
result = a ^ b  # 0110
print(f"5 ^ 3 = {result}")

# 按位取反运算
result = ~a  # -(0101 + 1) = -(0110) = -6
print(f"~5 = {result}")

# 按位左移运算
result = a << 1  # 1010
print(f"5 << 1 = {result}")

# 按位右移运算
result = a >> 1  # 0010
print(f"5 >> 1 = {result}")




















