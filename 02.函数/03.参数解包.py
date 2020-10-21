import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 传递实参时，也可以在序列类型的参数前添加*，这样他会自动将序列中的元素依次作为参数传递,要求序列中元素的个数必须与形参的个数一致，否则会报错

def fn(a,b,c):
  print(a,b,c)

# tup = (1,2,3)
# fn(*tup)
# tup = [3,2,1]
# fn(*tup)

# 对字典解包
dic = {'a':11,'b':22,'c':33}
fn(**dic) # 解出来的是value值