# print('引入的module模块')
a = 10
b = 20
_c = 30  # 通过_定义的变量  是私有的,外界访问不到 
def moduleFnc():
  print('这是moduleFnc函数')

class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age