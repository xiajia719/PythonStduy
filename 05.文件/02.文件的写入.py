# import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

file_name = 'demo1.txt'
# mode='r' 只读 ===========   
# 'w' 可写（会覆盖原文件） 
# 'a'  追加内容  
# '+' 表示操作符增加功能（例如： r+ 可读又可写，文件不存在会报错） 
# 'x' 文件存在则报错，不存在则创建并写入  
with open(file_name,'a',encoding='utf-8') as file_obj:
  r = file_obj.write('1111\n') # 该方法会返回写入字符的个数
  print(r)

# 读取模式 
# t读取文本文件 b读取二进制文件
file_name1 = r'C:\Users\56849\Desktop\lakers.jpg'
with open(file_name1,'rb') as file_obj:
  r = file_obj.read() # 该方法会返回写入字符的个数
  # 读取文本文件时，size是以字符为单位，读取二进制文件时，size是以字节为单位
  print(r)