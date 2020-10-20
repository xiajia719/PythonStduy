import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 通过range()可以创建一个执行指定次数的for循环
for i in range(10):
  print(i)