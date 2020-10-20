import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 可变序列
#     list(列表)
# 不可变序列
#     字符串(str)
#     元组(tuple)

# 字符串
string = 'hello'
print(string[1])

# 元组
tup = ('hello','nihao')
print(tup[0])

# 列表(list)
li = ['你好','孙悟空','猪八戒']
# del li[1]
# print(li[1:])
# 给切片赋值时必须传递一个序列
# li[0:1] = 'hello'
# string = list(string)

# append() 向尾部增加元素
li.append('沙和尚')

# insert 向某个位置插入元素 参数：插入的位置;插入的元素
li.insert(0,'白骨精')

# extend 插入一个序列
li.extend('123')

# clear()  只能用于可变序列
# li.clear()

# pop 根据索引删除元素,返回删除的元素 不传删除最后一个
# li.pop(1)

# remove 根据指定值,如果删除的值有多个，删除第一个，没有返回值 返回none 不传报错
li.remove('1')

# reverse() 反转序列
# sort() 排序 默认升序  如果需要降序 传第一个reverse=True作为参数
print(li)