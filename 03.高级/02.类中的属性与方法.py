import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# ================================== self
class MyClass(object):
  def fnc(self):
    print(self.name)

#  class里定义的方法，默认第一个参数是调用方法的实例本身，可以访问到当前调用方法的实例的属性
mc = MyClass()
mc.name = '猪八戒'
# mc.fnc()

# ================================== init
# 在类中可以定义一些特殊方法（魔术方法） 以__开头，以__结尾
# 特殊的方法会在特殊的时刻自动调用
# 调用类创建对象时，类后面的所有属性都会传递给init函数
class myClass2():
  def __init__(self,name):
    self.name = name
    print('当前实例的name是 %s'%self.name)

p1 = myClass2('孙悟空')
