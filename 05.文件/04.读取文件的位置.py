import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码


# seek() 可以修改当前读取的位置
#   第一个参数：要切换的位置
#   第二个参数：计算位置方式
# 