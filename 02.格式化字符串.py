import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
a ='hello'
b ='\u0070'
print('a=' + a)
print(b)