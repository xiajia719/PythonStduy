# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

file_name = 'demo.txt'
# # 打开文件
file_obj = open(file_name)
# # 读取文件
# content = file_obj.read()
# # 关闭文件
# file_obj.close()

# with  as 语句   自动关闭文件
try 
  with open(file_name) as file_obj:
    print(file_obj.read())
except
  print(1111)