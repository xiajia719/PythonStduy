import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

import module as test # 输出 module
# print(test.a)   通过模块名.属性名访问
# test.moduleFnc()  这是moduleFnc函数
p = test.Person('孙悟空','15')
print(p.name) # 孙悟空 