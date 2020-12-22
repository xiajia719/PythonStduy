import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 特殊方法也被称为魔术方法
# 都是以__开头和结尾的
# 一般不需要我们手动调用，需要在一些特殊情况下自动执行
class Special():
  def __init__(self,name):
    self.name = name
    print('init执行了')

  def __str__(self):
    return 'aaaaa'
  
  def __repr__(self):
    return 'hello'

# __init__  在创建对象的时候自动执行
p = Special('jack')

# __str__   打印对象的时候 实际上是在打印str方法的返回值
print(p)

# __repr__  对当前对象使用repr函数时调用:指定对象在交互模式中直接输出的结果，str是print函数的输出结果，repr是直接输入对象的结果
print(repr(p))

# __len__()  获取对象的长度
# __bool__(self)   对象转化为什么布尔值由此方法决定，通过bool指定对象转为为布尔值的结果