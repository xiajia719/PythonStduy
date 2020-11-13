import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 多重继承  开发时避免使用多重继承，代码复杂不好维护
# ！！！！！！！！！！！！！！！！！如果继承的多个父类有重名的方法，前面的会覆盖到后面的比如C继承的A会覆盖B的同名方法！！！！！！！！！！！！！！！！！！！
#  类名.__bases__ 这个属性可以用来获取当前类的所有父类，返回的是一个元组
class A(object):
  pass
class B(object):
  pass

# class C(A):
#   pass

# print(C.__bases__) # (<class '__main__.A'>,)

class C(A,B):
  pass

print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)