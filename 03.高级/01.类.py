import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 类也是一个对象，是用来创建一个对象的对象
# 定义一个简单的类
# 使用class 关键字定义类，语法跟函数很像
# class 类名([父类])  类名使用大驼峰
class MyClass(object):
  """
  docstring
  """
  pass
# print(MyClass) # <class '__main__.MyClass'>  在主文件main里的一个类:MyClass

# 使用MyClass创建一个对象   类似调用函数的形式
mc = MyClass()
mc2 = MyClass()  
mc3 = MyClass()  


#  mc是一个对象( id=内存分配，type=<class MyClass>,value='' )
# mc  mc2 mc3都是MyClass的实例，都是一类对象,可使用isinstance()检查一个对象是否是一个类的实例

print(isinstance(mc,MyClass))   #True


# print(mc)  # <__main__.MyClass object at 0x000001C321F0DDD8>