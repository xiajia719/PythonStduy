import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 命名空间指的是变量存储的位置，有全局命名空间和函数命名空间

# 可使用locals() 获取当前的命名空间，返回的是一个字典类型

a  = 20

def fn():
  b = 10
  print('函数内部',locals())

fn()
scope = locals()
scope['abc'] = 200
# 如果以字典的添加形式添加key-value,就相当于在全局中创建了一个全局变量abc,值为200
print('函数外部',scope)