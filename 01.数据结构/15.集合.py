import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
# 集合(set)
# ====>集合与列表非常相似
# ====>不同点：
#           1,集合中只能存储不可变对象
#           2,集合中存储的对象是无序的
#           3,集合中不能出现重复的元素

# 如何创建集合

# 1,使用{}。
s = {1,2,3,4}
# print(type(s)) <class 'set'>

# 2,使用set()
ss = set('123') #{'1', '3', '2'}/{'2', '1', '3'}/....
# ss = set({'a':'1','b':'2'})  # 传字典 只会保存key
print(ss)

# in  not in  检查元素
# en() 查看长度
# add()  向集合中添加元素
# update()  将一个集合中的元素添加当前集合中  参数为集合,元组，字典(只加了key)等序列
# pop()  随机删除一个集合中的元素 一般情况下都是删除第一个，但不是绝对。返回删除的元素
# remove() 删除集合中的指定元素 无返回值，None
# clear() 清空集合
# copy()  对集合进行浅复制