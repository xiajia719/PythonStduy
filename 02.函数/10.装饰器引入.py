import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 通过装饰器来扩展函数的功能 
# 就是创建一个新韩淑，传入要装饰的函数，再返回一个新函数  
# @ + 装饰器函数名  代表下方的函数被装饰器函数所装饰


@装饰器函数
def say_hello():
  print('hello')

say_hello()