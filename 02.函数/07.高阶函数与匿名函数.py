import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 高阶函数：参数是函数，或者返回一个函数的函数

# 如内置的filter()
def fn(num):
  if num % 2 == 0:
    return num
result = filter(fn,[1,2,3,4,5,6])
# 备注：filter函数返回的是一个可迭代的序列，需要list()转化为可见的列表
print(list(result))

# 匿名函数 lambda
#               lambda parameter_list: expression
result1 = filter(lambda num: num % 2 == 0,[1,2,3,4,5,6,7,8])
print(list(result1))

# map()  遍历用的高阶函数
result2 = map(lambda num: num + 1,[1,2,3,4,5,6])
print('map函数',list(result2))