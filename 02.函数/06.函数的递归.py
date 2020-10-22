import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 题：求任意数的阶乘
def getJC(num):
  for i in range(1,num):
    num *= i
  return num

print(getJC(10))

# 递归就是函数内部，再次调用函数本身，一层一层的调用就是递归
# def fn():
#   fn()
# 原理：
    # 10! = 10 * 9!     9! = 9 * 8! 。。。。。
def getJC1(num):
  if num == 1:
    return 1
  return num * getJC1(num - 1)
print(getJC1(10))

# 练习1，创建一个函数power，来对任意数字做幂运算 n ** i
def power(n,i):
  if i == 1:
    return n
  return n * power(n,i-1)
result = power(3,4)
print('练习1',result)

# 练习2  创建一个函数，检查一个任意的字符串是否是回文字符串，如果是 返回true，如果不是返回false
# def isHWStr(string):
#   if len(string) < 2:
#     return True
#   arr = list(string)
#   if arr[0] == arr[-1]:
#     if len(arr) == 2 :
#       return True
#     else:
#       length = len(arr)
#       newArr = arr[1:length-1]
#       isHWStr(string)
#   else:
#       return False

# 练习2  创建一个函数，检查一个任意的字符串是否是回文字符串，如果是 返回true，如果不是返回false
def isHWStr(s):
  if len(s) < 2:
    return True
  elif s[0] != s[-1]:
    return False
  return isHWStr(s[1:-1])
print('练习2',isHWStr('abba'))