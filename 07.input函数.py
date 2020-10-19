import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码
num = input('请输入用户名：')
# input返回的结果全是字符串
if num == 'admin' :
  print('欢迎光临')
else :
  print('用户名错误！')