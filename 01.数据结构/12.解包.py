import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 元组的解包就是讲元组中的值一一赋值给变量
tup = (1,2)
a,b = tup
a,b = 12,34
a,b = ['aa','bb']
print(a,b)