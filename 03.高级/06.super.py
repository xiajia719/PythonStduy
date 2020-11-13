import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 继承  面向对象的三大特性之一
#     通过继承我们可以使一个类获取到其他类中的属性和方法
# 在创建类的时候 如果省略了父类，则默认父类是object
class Animal():
  def __init__(self,name):
    self.name = name

class Dog(Animal):
  def __init__(self,name,age):
    # 希望可以直接调用父类的init方法来初始化父类中定义的属性
    # super() 可以用来获取当前类的父类，并且通过super()返回对象调用父类方法时，不需要传递self
    super().__init__(name)
    self._age = age
  
  @property
  def age(self):
    return self._age

  # @age.setter
  # def age(self,age):
  #   self._age = age

  # @property
  # def name(self):
  #   return self._name
  
  # @name.setter
  # def name(self,name):
  #   self._name = name

p = Animal('jack')

d = Dog('cling',23)

print(p.name,'p的name')