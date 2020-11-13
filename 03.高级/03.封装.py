import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 封装是面向对象的三大特性之一
# 封装的意思：  隐藏对象中一些不希望被外界所访问到的属性或方法
# 如何获取（修改）对象中的属性？    getter/setter
# 特点：
  # 1.隐藏了属性名，使使用者无法随意的修改对象中的属性
  # 2.属性不能修改为任意的值（比如年龄属性不能赋值为负数），很好的控制了属性是只读的
  # 3.如果希望属性是只读的，可以去掉setter方法，如果希望属性不能被外部访问，则可以去掉getter方法
  # 4.使用setter方法设置属性，可以对属性值进行验证，确保赋的是正确的值
  # 5.可以在用户调用setter与getter方法时做其他的一些操作，比如记录修改或查询操作。

class Person():
  def __init__(self,name):
    self.__name = name
  
  def get_name(self):
    return self.__name

  def set_name(self,name):
    self.__name = name

# 可以为对象的属性使用双下划线开头， __xxx 
# 双下划线开头的属性是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问  
# 这种方式一般不用 ！！！！！！！！(实际上是将名字改为了 _类名__属性名 )
#       print(p._Person__name)  # cling

p = Person('cling')
# print(p.__name)  # 'Person' object has no attribute '__name'
print(p.get_name())  

# 一般使用一个_就可以了,表明这是私有属性 (防君子不防小人)
class Person2():
  def __init__(self,name):
    self._name = name
  
  def get_name(self):
    return self._name

  def set_name(self,name):
    self._name = name

p2 = Person2('jack')
# print(p2._name)
print(p2.get_name())