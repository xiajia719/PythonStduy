import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
arr = ['孙悟空','猪八戒','唐僧','沙和尚']

for i in arr:
  print(i)

# for循环除了创建方式以外，其余的都和while一样，包括else，break，continue都可以使用