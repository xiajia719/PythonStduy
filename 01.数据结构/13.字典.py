import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 字典(dict)
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

# pop(key)  根据key删除指定的key-value  返回删除的value
# popitem() 随机删除字典中的一个键值对，一般都会删除最后一个 返回由删除的键值对构成的元组:(key,value)
# update() 将其他的字典中的键值对添加到当前字典中
# clear() 清空字典
# copy() 用于对字典浅复制 一个新字典 地址值不同 但是修改copy出来的字典 原字典也会变 
 
# 注意：  
# =========== (浅复制，只复制了字典本身,对于字典内部的可变序列，如字典内还有一个字典，则会随着改变)