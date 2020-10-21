import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
a ='123'
b = 123
# type()
print(type(a)) # <class 'str'>
print(type(b)) # <class 'int'>