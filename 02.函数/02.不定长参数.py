import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 使用*将传过来的参数放置一个元组中(装包)

def fn(*nums):
  print(nums) # (1, 2, 3)

fn(1,2,3)

# 注意，带*的参数只能使用一个，可以与其他参数混合使用，元组的分配规则
# 如果带*的参数没有写在最后面，那么后面的传参,必须要使用关键字传参
def fn2(*a,b,c):
  pass
fn2(1,2,3,b=4,c=5)  # a :(1,2,3), b:4, c,5

# **  处理关键字传参，关键字传参也会被**的形参捕获