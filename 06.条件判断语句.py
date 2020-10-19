import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
num = 100
if num > 10 :
  print(num,'嘿嘿')
  print('嘿嘿'，num)

a = 20
if num > 10 :
  print('大于10')
elif num > 20 :
  print('大于20')
elif num > 30 :
  print('大于30')
elif num > 40 :
  print('大于40')
else :
  print('谁也大不了')