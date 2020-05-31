# 面向对象oop
# a=1
# class Myclass():
#     pass
# mc = Myclass()
# print(mc, type(mc), id(mc))
# print(isinstance(mc,Myclass))
# print(isinstance(a,Myclass))
# # <__main__.Myclass object at 0x00000000026D2948> <class '__main__.Myclass'> 40708424
# # True
# # False
#
# print(id(Myclass), type(Myclass))
# # 1652712 <class 'type'>
#
# mc.name ='swk'
# print(mc.name)

# class Person:
#     # name = 'swk' #类中定义的变量（属性）可在对象中使用
#     # 一般方法保存在类中，属性保存在实例中
#     print('exe data')
#     def __init__(self, name):  #特殊方法无需自己调用,特殊时候自己调用
#         print('executive')
#         self.name = name
#
#     def say_hello(self):
#         print('hello %s' %self.name)
#
# p1 = Person('zbj')
# # p1.name = 'zbj'
# p1.say_hello()
#
# # p2 = Person()
# # p2.name = 'swk'
# # p2.say_hello()
#
# print(p1.name)

# class Dog:
#     '''
#     represent class of dog
#     '''
#     acount_legs = 4
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def run(self):
#         print('%s 快乐奔跑' % self.name)
#
#     def jump(self):
#         pass
#
# dog = Dog('ww', '8', 'male')
# dog.run()
# dog.name = 'qq'
# dog.run()

# # 封装
# class Dog:
#     '''
#     represent class of dog
#     '''
#     acount_legs = 4
#
#     def __init__(self, name, age, gender):
#         self._name = name
#         self._age = age
#         self._gender = gender
#
#     def get_name(self):
#         print('用户查询了name属性')
#         return self._name
#
#     def set_name(self, name): # 如果希望属性仅可读，则去掉set方法
#         print('用户修改了name属性')
#         self._name = name
#
#     def run(self):
#         print('%s 快乐奔跑' % self._name)
#
#     def jump(self):
#         pass
#
# dog = Dog('ww', '8', 'male')
# dog.run()
# dog.set_name('qq')
# dog.run()
# # ww 快乐奔跑
# # 用户修改了name属性
# # qq 快乐奔跑

# class Rectangle:
#     '''
#     表示矩形的类
#     '''
#     def __init__(self, width,height):
#         self._width = width
#         self._height = height
#         self._area = self._height * self._width
#
#     def get_width(self):
#         return self._width
#     def get_height(self):
#         return self._height
#
#     def set_width(self, width):
#         self._width = width
#     def set_height(self, height):
#         self._height = height
#
#     # def set_area(self):
#     def get_area(self):
#         return self._area
#
# area = Rectangle(5,7)
# area.name = 1
# print(area.name)
# print(area.get_area())

# # @property
# class Person:
#     def __init__(self,name):
#         self._name = name
#
#
#     @property
#     def name(self):
#         return self._name
#
# p = Person('zbj')
# print(p.name)

# # 继承 and 重写
# class Animal:
#     def __init__(self, name):
#         self._name = name
#
#     def run(self):
#         print(self._name, 'run~~')
#
#     def sleep(self):
#         print(self._name, 'sleep~~')
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
# class Dog(Animal):
#
#     def __init__(self, name, age):
#         super().__init__(name)
#         self._age = age
#
#     def bark(self):
#         print(self._name, 'bark~~')
#
#     @property
#     def age(self):
#         print('age is', self._age)
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
# d =Dog('ww', '18')
# d.run()
# d.age = 28
# print(d.name, d.age)
# print(Dog.__base__)
# #
# # ww run~~
# # age is 28
# # ww 28
# # <class '__main__.Animal'>

# # 多态
# class A:
#     def __init__(self,name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
# class B:
#     def __init__(self,name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
# a = A('swk')
# b = B('zbj')
#
# def say_hello(obj):
#     print('hello %s'%obj.name)
#
# say_hello(a)


# class A:
#     # 类属性
#     count = 0
#
# a = A()
# a.count = 10  # 实例属性
# print(A.count)

# 抛出异常

def add(a, b):
    if a < 0 or b < 0:
        raise Exception('error')

    r = a + b
    return r

r =add(1, -2)









 





























