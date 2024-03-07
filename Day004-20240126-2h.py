age = float(input('请问你今年多少岁? '))
if age >= 18:
    print('你已经成年了!')


age = float(input('请问你今年多少岁? '))
if age >= 18:
    print('你已经成年了!')
else:
    print('你还未成年!')


score = float(input('你这次考试考了多少分? '))
if score >= 90:
    print('厉害!')
elif score >= 80:
    print('优秀!')
elif score >= 70:
    print('良好!')
elif score >= 60:
    print('及格!')
else:
    print('不及格!')
    
age = float(input('请问你今年多少岁? '))
print('你已经成年了!') if age >= 18 else print('你还未成年!')  
score = float(input('你这次考试考了多少分? '))
print('厉害!') if score >= 90 else \
print('优秀!') if score >= 80 else \
print('良好!') if score >= 70 else \
print('及格!') if score >= 60 else \
print('不及格!')  

age = float(input('请问你今年多少岁? '))
if age >= 18:
    ans = input('可以出示您的身份证吗(Y/N): ')
    if ans == 'Y':
        print('身份核对正确, 请尽情冲浪吧!')
    else:
        print('成年人需要凭身份证上网!')
else:
    print('未成年人禁止出入网吧!')


num = 5 
if num > 0:
    print('a')
elif num > 1:
    print('b')
elif num > 2:
    print('c')
if num > 3:
    print('d')
if num > 4:
    print('f')
if num > 5:
    print('g')
else:
    print('h')

if 1:
    print('hello world') 
if None:
    print('hello world')
import random  
res = {0: '石头', 1: '剪刀', 2: '布'} 
computer = random.randint(0, 2)
player = int(input('请出拳(0-石头、1-剪刀、2-布): ')) # 出拳展示
print(f'电脑出拳: {res[computer]}\n玩家出拳: {res[player]}') # 胜负判定

if computer == player:
    print('平局!')
elif player-computer in (-1, 2):
    print('玩家胜!')
else:
    print('电脑胜!')

import random  

# 打印一个0到1之间的随机浮点数
print(random.random()) 

# 打印一个2到4之间的随机整数（包括2和4）
print(random.randint(2, 4)) 

# 打印一个2.5到3.5之间的随机浮点数
print(random.uniform(2.5, 3.5))

# 打印一个2.5到3.5之间的随机浮点数
# 注意：对于random.uniform来说，参数的顺序不重要
print(random.uniform(3.5, 2.5)) 

# 从列表[3, 4, 1, 7]中随机选择一个元素并打印
print(random.choice([3, 4, 1, 7])) 

# 从元组('a', 'c', 'f', 'd', 'b')中随机选择3个元素组成的样本并打印
print(random.sample(('a', 'c', 'f', 'd', 'b'), 3)) 

# 对列表[1, 2, 3, 4, 5]进行随机洗牌，然后打印洗牌后的列表
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst) 

# 打印一个从1到10（不包括10），步长为2（即奇数）的随机数
print(random.randrange(1, 10, 2)) 

# 演示设置随机数生成器的种子的效果
# 如果不设置种子，每次生成的随机数都会不同
print(random.random()) 

# 使用10作为随机数生成器的种子
random.seed(10)
print('seed10:', random.random()) 

# 使用7作为随机数生成器的种子
random.seed(7)
print('seed7:', random.random()) 

# 再次使用10作为随机数生成器的种子
random.seed(10)
print('seed10:', random.random())


# 循环语句
# while 循环
# 打印从1到100的数字
num = 1
while num <= 100:
    print(num)
    num += 1

num = 1
while True:
    print(num)
    num += 1
    if num > 100:
        break

num = 1
while num <= 100:
    print(num)
    num += 1
else:
    print('🐕')  

num = 1
while True:
    print(num)
    num += 1
    if num > 100:
        break
else:
    print('🐕')

# 实现九九乘法表
right = 1
while right <= 9:
    left = 1
    while left <= right:
        print(f'{left}x{right}={left*right}', end='\t')
        left += 1
    print()
    right += 1

# for 循环
lst = ['d', 'c', 'k', 'a']
# 获取元素
for i in lst:
    print(i) # 获取索引

for i in range(len(lst)):
    print(i) # 获取索引和元素

for index, item in enumerate(lst):
    print(index, item)

lst = [4, 1, 5, 7, 2]
for i in lst:
    print(i)
    if i > 5:
        break
else:
    print('🐕')  

lst = [4, 1, 5, 7, 2]
for i in lst:
    print(i)
    if i > 7:
        break
else:
    print('🐕')

print(list(range(4)))  # [0, 1, 2, 3]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(1, 8, 2)))  # [1, 3, 5, 7]
print(list(range(8, 1, -2)))  # [8, 6, 4, 2] 
rg = range(1, 8, 2)
print(len(rg))  # 4
print(rg[2])  # 5
print(rg[::2])  # range(1, 9, 4)
lst = ['d', 'c', 'k', 'a']
print(list(enumerate(lst)))
print(tuple(enumerate(lst))) 
for i in enumerate(lst):
    print(i)

