# # 循环控制语句  
     
# # break
# # 终止所在的循环

 
# for _ in range(3):
#     for _ in range(4):
#         print('hello')
#         break  

# for _ in range(3):
#     for _ in range(4):
#         print('hello')
#     break

# # continue
# # 跳过当前这次循环，继续到下一次循环
# # 输出1-10之间的偶数
# num = 1
# while num <= 10:
#     if num % 2:
#         num += 1
#         continue
#     print(num)
#     num += 1


# # 列表推导式
# lst = [x ** 2 for x in range(4)]
# print(lst) 
# # 类比
# lst = []
# for x in range(4):
#     lst.append(x ** 2)
# print(lst)  
# lst = [x + y for x in range(5) if x % 2 for y in (1, 2, 3)]
# print(lst) 
# # 类比
# lst = []
# for x in range(5):
#     if x % 2:
#         for y in (1, 2, 3):
#             lst.append(x + y)
# print(lst)

# # 字典推导式
# d = {x: x**2 for x in range(4)}
# print(d) 
# # 类比
# d = {}
# for x in range(4):
#     d[x] = x ** 2
# print(d)  
# d = {x: v for x in range(4) for v in range(9) if v % 2}
# print(d) 
# # 类比
# d = {}
# for x in range(4):
#     for v in range(9):
#         if v % 2:
#             d[x] = v
# print(d)


# # 集合推导式
# s = {x ** 2 for x in range(4)}
# print(s) 
# # 类比
# s = set()
# for x in range(4):
#     s.add(x ** 2)
# print(s)  
# s = {x + y for x in range(5) if x % 2 for y in (1, 2, 3)}
# print(s) 
# # 类比
# s = set()
# for x in range(5):
#     if x % 2:
#         for y in (1, 2, 3):
#             s.add(x + y)
# print(s)


# # 迭代
# # lst = [1, 2, 3] 
# # for i in lst:
# #     lst.remove(i) 
# #     print(lst)

# lst = [1, 2, 3]
# new_iter = lst.copy()
# # new_iter = lst[:]
# # new_iter = list(lst)
# # new_iter = tuple(lst) 
# for i in new_iter:
#     lst.remove(i) 
#     print(lst)


# # 字典、集合在迭代时，不允许改变原数据的size
# # d = {'name': 'Tom', 'age': 28, 'height': 177}
# # for k in d:
# #     print(d.pop(k))
# #     print(d)  
    
# # s = {'a', 'b', 'c', 'd', 'f'}
# # for i in s:
# #     s.remove(i)
# #     print(s)

# d = {'name': 'Tom', 'age': 28, 'height': 177}
# new_iter = d.copy()
# # new_iter = dict(d)
# # new_iter = list(d)
# # new_iter = tuple(d) 
# for k in new_iter:
#     print(d.pop(k))
#     print(d)

# s = {'a', 'b', 'c', 'd', 'f'}
# new_iter = s.copy()
# # new_iter = set(s)
# # new_iter = list(s)
# # new_iter = tuple(s) 

# for i in new_iter:
#     s.remove(i)
#     print(s)


# # pass 是一个关键字，表示一个空语句，当它被执行时，不做任何操作，通常用作占位符，在语法上需要语句但实际上不需要执行任何操作的情况下使用
# score = float(input('你这次考试考了多少分? '))
# if score >= 90:
#     print('厉害!')
# elif score >= 80:
#     pass
# elif score >= 70:
#     print('良好!')
# elif score >= 60:
#     ...
# else:
#     print('不及格!')