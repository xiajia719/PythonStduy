import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
a ='hello'
# 占位符
b = 'hello %s'%'你好'
c = 'hello %s 你好'%'你好'
e = '孙悟空1'
d = 'hello %s 你好 %s'%(e,'啊')
aa = 'hello %4s'%'你好' #4个占位符 不够的补空格
aa = 'hello %3.5s'%'你好孙悟空猪八戒' #3.5个占位符 长度限制在3-5之间
bb = 'hello %f'%123.2
bb = 'hello %.1f'%123.2
bb = 'hello %.2f'%123.2
bb = 'hello %d'%123.2112
print('a=' + a)
print(b)
print(c)
print(d)
print(aa)
print(bb)
# 格式化字符串
# 在格式化字符串中可以直接嵌入变量
s = f'hello'
ss = f'呵呵 {a}'
print(s)
print(ss)