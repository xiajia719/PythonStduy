import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
s1 = {1,2,3,4,10}
s2 = {5,6,7,8,10}

# & 交集
result1 = s1 & s2
print(result1) # {10}

# | 并集运算
result2 = s1 | s2
print(result2) # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# - 差集运算  只在a 集合中有， b集合没有的
result3 = s1 - s2 
print(result3) # {1, 2, 3, 4}

# ^ 亦或集运算  只在一个一个集合中出现的元素，排除相同的
result5 = s1 ^ s2 
print(result5) # {1, 2, 3, 4}

# <= 检查一个集合是否是另一个集合的子集
# ------->如果a的元组全部都在b中出现，那么a集合就是b集合的子集，b集合是a集合的超集
result6 = s1 <= s2 
print(result6) # False

# < 检查一个集合是否是另一个集合的真子集（a集合全都在b中出现，且b中还有a没有的元素）
# ------->如果a的元组全部都在b中出现，且b中还有a没有的元素，那么a集合就是b集合的真子集，b集合是a集合的真超集
result = {1,2,3} < {1,2,3} # false
result = {1,2,3} < {1,2,3,4} # true

# >=  检查一个集合是否是另一个集合的超集
# >  检查一个集合是否是另一个集合的真超集