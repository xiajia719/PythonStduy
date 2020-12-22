import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码

# 读取模式 
# t读取文本文件 b读取二进制文件
file_name1 = r'C:\Users\56849\Desktop\lakers.jpg'
with open(file_name1,'rb') as file_obj:
  new_name = 'new.jpg'
  with open(new_name, 'wb') as new_obj:

    # 定义每次读取的字节
    chunk = 1024 * 100

    while True:
      # 从已有对象中读取文件
      content = file_obj.read(chunk)

      if not content:
        break
      
      new_obj.write(content)