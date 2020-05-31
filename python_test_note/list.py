# list 有序

# # 列表创建
# my_list = [1, 2, 4, 5, 6]
# print(my_list, type(my_list))
#
# my_list.append(3)
# print(my_list, type(my_list))
#
# a = my_list[3]
#
# print(a)
#
# b = len(my_list)
# print(b)

# # list切片 and 加乘
# my_list = [1, 2, 4, 5, 6]
# list_one = my_list[1:5:2]
# # [2, 5] <class 'list'> 4805512
# # [1, 2, 4, 5, 6] <class 'list'> 4805000
# print(list_one, type(list_one),id(list_one))
# print(my_list, type(my_list),id(my_list))
#
# list_two = my_list * 2 + list_one
# print(list_two)
#
# a = 2 in my_list
# print(a)
#
# b = min(my_list)
# print(b)

# my_list = [1,3,2,3,4,3,3,5,6]
# print(my_list.index(3,0,7))
# print(my_list.count(3))
# i = 1
# # for i in my_list.count(3):
# my_list.remove(3)
# print(my_list)
#
# # sequence　可变
# my_list[1]=8
# print(my_list)
# del my_list[1:5:2]
# print(my_list)
# my_list[0:0] = [123]
# print(my_list)
# my_list[0:5:2] =[1, 3, 4]
# print(my_list)
#
# c = 'hello'
# print(list(c))

# my_list = [1,3,2,3,4,3,3,5,6]
# my_list.insert(5, 123)  # 嵌入
# # [1, 3, 2, 3, 4, 123, 3, 3, 5, 6]
# my_list.extend(['a', 'b'])
# # [1, 3, 2, 3, 4, 123, 3, 3, 5, 6, 'a', 'b']
# # my_list.clear()
# # # []
# my_list.pop(2)
# # [1, 3, 3, 4, 123, 3, 3, 5, 6, 'a', 'b']
# my_list.remove(123)
# my_list.remove('a')
# my_list.remove('b')
# my_list.remove(3)
# my_list.reverse()
# my_list.sort(reverse=True)
# print(my_list)


# 遍历
# stus = [1,2,3,4,5,6]
# i = 0
# while i < len(stus):
#     print(stus[i])
#     i = i + 1

# for i in stus:
#     print(i)

# # range 生成序列,用于for循环
# for i in range(10):
#     print(i)
#
# r = range(10)
# r =range(0, 10, 2)
# for i in r:
#     print(i)
# print(r)

# # 元组 创建 and 解包
# my_tuple = ()
# my_tuple = (1, 2, 3, 4, 5,)
# print(my_tuple)
# tuple_one = (1,)
# # <class 'tuple'>
# tuple_one = (1)
# # <class 'int'>
# print(type(tuple_one))
#
# a, b, *c = my_tuple
# print(a, b, c)
# a, b, c = c, b, a
# print(a, b, c)
# # 1 2 3 4 5
# # 3 2 1
# r = my_tuple[1:4:2]
# print(r)

# 错误，元组不可变
# my_tuple[2] = 7
# print(my_tuple)
#
# # 字典dict
# d = dict(name='swk', age=18, gender= 'male')
# r = {'name': 'zbj', 'age': 28, 'gender': 'male'}
# print(d,r)
#
# my_list = [('name', 'swk'), ('age', 18)] #双值子序列
# print(dict(my_list))
#
# # 判断
# print('name' in d)
# print(d['age'])
# print(d.get('len', '默认值'))
#
# # 添加
# d['gender'] = 'female'
# d.setdefault('home','hgs')
# print(d)
#
# # 运算
# d.update(r)
# del d['age']
# d.popitem()
# d.pop('nam', 'default')
# print(d)
#
# # 浅复制
d = {'a': 1, 'b': 2, 'c': 3}
# b = d.copy()
# print(d, id(d))
# print(b, id(b))
#
# # 遍历
# D = d.keys()
#
# for i,j in d.items():
#     print(i, j, type(i))
# print(d.keys())
# print(d.values())
# list and dict 可变

# # 集合set
s = set([1, 2, 3, 4, 5])
D = set(d)
print(s,D)
# my_list = [[1,2],3,4]
# 加减复制更新
s.add(7.8)
s.update(D)
s.pop()
s.remove('b')
q = s.copy()
print(s, id(s))
print(q, id(q))

# # 集合运算
# s = {3, 4}
# D = {3, 4, 5, 6}
# result = s and D # result = s & D
# print(D)
# print(result)
# result = s ^ D #异或
# result = s < D
# print(result)



















































