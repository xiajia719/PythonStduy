import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# int()  float() str() bool()
a = False
# a = float(a) # 0.0

# bool()  所有表示空性的对象都会转换为False,其余的转换为True
# '' None 0 