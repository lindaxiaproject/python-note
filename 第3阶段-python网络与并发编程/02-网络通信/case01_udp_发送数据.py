#coding=utf-8
from socket import *
# 创建UDP类型的套接字
s = socket(AF_INET, SOCK_DGRAM)
# 准备接收方地址
addr = ('127.0.0.1',8888)
data = input("请输入：")
# 发送数据时，python3需要将字符串转换成byte
s.sendto(data.encode('gbk'), addr)
s.close()