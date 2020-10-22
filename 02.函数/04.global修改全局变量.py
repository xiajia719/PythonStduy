import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 使用global关键字,可在函数内部修改全局变量
a  = 20

def fn():
  global a
  a = 30
  print('函数内部',a)

fn()

print('函数外部',a)