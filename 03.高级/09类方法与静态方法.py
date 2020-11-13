import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
class Person():

  # 通过@classmethod修饰的方法，是类方法，类与实例对象都可以调用，第一个参数是cls（当前的类对象），默认传递
  @classmethod
  def test_01(cls):
    print('这是一个类方法')

  # 通过@staticmethod修饰的方法属于静态方法,不需要指定任何参数，可以通过类与实例去调用
  # 静态方法基本上是一个和当前类无关的方法，他只是一个保存到当前类中的方法
  # 静态方法一般都是一些工具方法，和当前类无关
  @staticmethod
  def test_02():
    print('这是一个静态方法')

p = Person()
p.test_01() 
Person.test_01()

p.test_02() 
Person.test_02()