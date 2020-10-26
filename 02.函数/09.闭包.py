import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 将函数作为返回值返回，也是一种高阶函数
def fn():
  def fn2():
    print('1111')
  return fn2

print(fn())  # <function fn.<locals>.fn2 at 0x000001DA870AFA60>

# 形成闭包的条件:
  # 1，函数嵌套 2.将内部函数作为返回值返回  3.内部函数必须要使用到外部函数的变量


# fn2 是在fn内部定义的，也不是全局函数,所以这个函数可以访问到fn内部的所有变量

# sum() 用来求一个列表中的和

# print(sum([1,2,3,5,6,7,8]))  #    32

# nums = [1,2,3,5,6,7,8]
# # 创建一个函数用来计算平均值
# def averager(n):
#   # 将n添加到列表中
#   nums.append(n)
#   return sum(nums)/len(nums)

# print(averager(10))  # 5.25