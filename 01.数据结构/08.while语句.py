import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# num  = 1
# total = 0
# while num <= 100 :
#   if num % 2 != 0 :
#     total += num
#   num += 2
# print(total)
num = 1
count = 0
total = 0
while num < 100 :
  if num % 7 == 0 :
    total += num
    count += 1
  num += 1
print(count,total)