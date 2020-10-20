import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 元组的解包就是讲元组中的值一一赋值给变量
obj = {
  'name':'孙悟空',
  'age':'18',
  'gender':'男'
}
print(obj['name'])

# dict 函数创建字典
a = dict(name='jack',age=18,gender='男')
print(a)

# len() 获取长度
print(len(a))

# in 检查字典中包含指定的键值  not in
print('name' in a)

# get 根据键获取字典中对应键的值  如果获取的不存在 返回none
print(a.get('name')) #jack
print(a.get('aaa','默认值'))  # 第二个参数，如果没获取到，返回参数值：'默认值'