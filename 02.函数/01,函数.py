import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 对象是内存中专门存储数据的一块区域
# 函数可以用来保存一些可执行的代码，并且可以在需要的时候对这些语句进行多次的调用
def fn():
  print('1')
  print('2')
  print('3')
fn()