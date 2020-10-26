import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# sort() 该方法用来对列表中的元素进行排序
l = ['a','aa','b','bb','ccc','dddd','f']

# l.sort()
# print(l)  其实是在用 < 号比较   ['a', 'aa', 'b', 'bb', 'ccc', 'dddd', 'f']

# sort()方法可以接收一个关键字参数  key
#     key需要一个函数作为餐宿，当设置了函数作为参数，每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
# l.sort(key=len)
# print(l)  # ['a', 'b', 'f', 'aa', 'bb', 'ccc', 'dddd']


# sorted()  与sort用法基本一致，，但是可以对任意序列进行排序，返回值不同，返回一个新对象，不会影响原对象
aa = [1,'1','12','2121',233]
# print(sorted(aa))  #   '<' not supported between instances of 'str' and 'int'
print(sorted(aa,key=int))   #  [1, '1', '12', 233, '2121']