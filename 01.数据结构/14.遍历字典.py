import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

obj = {
  'name':'孙悟空',
  'age':'18',
  'gender':'男'
}

# 遍历字典  keys()  返回一个序列，保存有字典的所有键
a = obj.keys()
for key in a:
  print(key)

# values() 返回一个序列，保存有字典的所有值
b = obj.values()
for key in b:
  print(key)

# items() 返回字典中的所有的项
c = obj.items()
for key,value in c:
  print(key,value)
# print(obj.items()) dict_items([('name', '孙悟空'), ('age', '18'), ('gender', '男')])

# print(a)