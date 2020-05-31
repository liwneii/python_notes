# function
# # 默认值,前面带*号实参必须以关键字参数输入
# def run(*, vate:int, time:int, position = 10):
#     new_position = vate * time + position
#     return new_position
#
# print('the new position is ', run(time=2,vate=3))
# #
# # 关键字参数
# def run(vate, time, position = 10):
#     new_position = vate * time + position
#     return new_position
#
# print(run(vate=1, time=7))
#
# print(type(run))

# # 不定长参数
# def sum(doubles,*all):
#     n = 0
#     for i in all:
#         n = n + i
#     result = doubles * n
#     print(result)
# sum(5,2,3,4,8)

# # 存储为字典
# def fn3(**a):
#     print('a=', a, type(a))
#
# fn3(b=1,c=2,d=3)

# # 参数的解包
# def fn4(a,b,c):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#
# t = (1, 2, 4,)
# print(fn4(*t))

# def sum(doubles,*all):
#     n = 0
#     for i in all:
#         n = n + i
#     result = doubles * n
#     print(result)
#     return result
#
# result = sum(5,2,3,4,8)
# print(type(result))
# print(sum(5,2,3,4,8))
# print(sum)
# print(id(sum))

# # help 无括号
# help(sum)
# help(print)

# # 文档字符串，__doc__ 说明
# def sum(doubles,*all):
#     '''
#     :param doubles:
#     :param all:
#     :return:
#     '''
#     n = 0
#     for i in all:
#         n = n + i
#     result = doubles * n
#     print(result)
#     return result
#
# print(sum.__doc__)

# 作用域(scope)
# def fn():
#     a = 10
#     print('a=',a)
#
# a = 20
# print('a=', a)
# fn()  # 调用时产生作用域
# print('a=', a)

# def fn2():  # 函数定义嵌套
#     global b  # 定义为全局变量
#     b = 10
#     a = 20
#     def fn3():
#         a = 40
#         print(a)
#     fn3()
# fn2()
#
# def fn3(): #与函数中的fn3()无关

# 命名空间(namespace)：存储变量
# 每一个作用域都有其命名空间（字典）

# #locals()用来获取当前作用域的命名空间
# print(locals())
# '''{'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000000268DFC8>,
#   '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
#   '__file__': 'D:/anaconda/envs/correl/manim/test/function.py', '__cached__': None}
# '''
# print(globals())

# # 10的阶乘
# i = int(input('请输入任意正整数'))
# j = 0
# n = 1
# while j < i:
#     j = j + 1
#     n = n * j
# print(n)
# # 递归
# def fn(num):
#     if num == 1:
#         return num
#     else:
#         return fn(num-1) * num
#
# i = int(input('请输入任意正整数'))
# result = fn(i)
# print(result)


# def fn(str, i):
#
#     if str[0] == str[-1] and len(str[0:i]) < 1:
#         return True
#     elif str[0] == str[-1]:
#         print(str[0:i])
#         i = i - 1
#         return fn(str[1:i], i)
#     else:
#         return False
#
# my_str = input('请输入回文字符串')
# i = len(my_str) - 1
# result = fn(my_str, i)
#
# print(result)

# # 高阶函数
# # 函数作为参数传递
# li = [1, 2, 3, 4, 5, 6, 7]
#
# # 子函数1
# def func1(num):
#     if num < 4:
#         return True
#
# # 子函数2
# def func2(num):
#     if num % 2 == 0:
#         return True
#
# # 主函数
# def fn(func, lst):
#     '''
#     fn()
#     :param lst:要进行筛选的列表
#     :return:
#     '''
#     new_list = []
#     for n in lst:
#         if func(n):
#             new_list.append(n)
#     return new_list
#
# print(fn(func1, li))
# print(fn(func2, li))

# # filter函数 and map函数
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
#
# fn1 = lambda n: n % 2 == 0
# fn2 = lambda n: n < 5 # 最好放在局部作用域中
# result = filter(fn2, lst)
#
# print(list(result))
# r =map(fn1, lst)
# print(list(r))
# # [1, 2, 3, 4]
# # [False, True, False, True, False, True, False, True]

# # sort function
# l = ['bb', 'aaaa', 'c', 'ddddddd']
# l.sort()
# print(l)
# l.sort(key=len)
# print(l)
# # ['aaaa', 'bb', 'c', 'ddddddd']
# # ['c', 'bb', 'aaaa', 'ddddddd']

# def make_averager():
#     nums = []
#     def averager(n):
#         nums.append(n)
#         return sum(nums)/len(nums)
#
#     return averager
#
# averager =make_averager()
#
# print(averager(10))
# print(averager(20))

# 装饰器引入(ocp princple)
# def fn1():
#     print('我是fn1')
#
# def add(a, b):
#     # print('starting')
#     print(a + b)
#     return a + b
#     # print('stopped')
#
# def mul(a, b):
#     return a * b

# # result = add(3, 5)
# # print(result)
# def fn(func, a, b):
#     print('starting')
#     r = func(a, b)
#     print('stopped')
#     return r
#
# print(fn(add, 3, 5))
# print(fn(mul, 3, 5))

# def begin_end(func):
#
#     def new_function(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('stop')
#         return result
#     return new_function
#
# # add = begin_end(add) # equal to @begin_end
# @begin_end
# def add(a, b):
#     # print('starting')
#     print(a + b)
#     return a + b
#
# result = add(3, 5)
# print(result)


# def begin_end(func, *args, **kwargs):
#
#     print('start')
#     result = func(*args, **kwargs)
#     print('stop')
#     return result
#
# f = begin_end(add, 3, 5)
















