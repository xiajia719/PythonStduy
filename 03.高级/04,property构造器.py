import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 装饰器(property)
class Person():
  def __init__(self,name,age):
    self._name = name
    self._age = age

  
  # property装饰器用来将getter方法转换为对象的属性,添加为property装饰器以后，我们就可以像调用属性一样使用get方法了
  # 使用property装饰的方法，必须和属性名是一样的
  @property
  def name(self):
    return self._name
  
  # setter方法的装饰器： @属性名.setter
  @name.setter
  def name(self,name):
    self._name = name

  @property
  def age(self):
    return self._age
  
  # setter方法的装饰器： @属性名.setter
  @age.setter
  def age(self,age):
    self._age = age

p = Person('cling')

# 调用了装饰器的getter方法
print(p.name) # cling

# 调用了装饰器的setter方法
p.name = 'hacker'

print(p.name) # hacker