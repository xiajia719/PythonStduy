import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 继承  面向对象的三大特性之一
#     通过继承我们可以使一个类获取到其他类中的属性和方法
# 在创建类的时候 如果省略了父类，则默认父类是object

# 定义一个类 有run跟sleep两个方法
class Animal():
  def run(self):
    print('running')

  def sleep(self):
    print('sleeping~~~~')

a = Animal()
a.run()

# 定义一个类 有run跟sleep,bark三个方法
class Dog(Animal): #父类/超类/基类/super
  def bark(self):
    print('汪汪汪')

# Animal跟Dog都有run跟sleep方法

d = Dog()
d.run() # running 也可以调用父类中的run方法

# 通过isinstance检查对象是不是一个类的实例
result = isinstance(d,Dog)
result2 = isinstance(d,Animal)
result3 = isinstance(d,object)
print(result) # True
print(result2) # True
print(result3) # True

#   issubclass 检查一个类是不是另外一个类的子类
print(issubclass(Dog,Animal)) #True
print(issubclass(Dog,object)) #True
print(issubclass(Animal,Dog)) #False