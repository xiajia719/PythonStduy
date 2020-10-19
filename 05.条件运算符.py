import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 获取a,b,c的最大值
a = 30
b = 200
c = 50
# print(a) if a > b and a > c else print(b) if b > c else print(c) # 不推荐这样写
# and 两个必须都是true  有一个为false 执行后面的代码

(print(a) if a > c else print(c)) if a > b else (print(b) if b > c else print(c))