import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
s ='''谁知盘中餐，粒粒皆辛苦'''
a ='\u0070'
print(s)
print(a)