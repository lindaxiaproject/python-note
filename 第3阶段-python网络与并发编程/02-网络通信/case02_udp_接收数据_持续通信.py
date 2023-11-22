#coding=utf-8
from socket import *
# 创建UDP类型的套接字
s = socket(AF_INET, SOCK_DGRAM)
# 绑定接收信息接口
s.bind(('127.0.0.1',8888))
print("等待接收数据.....")
while True:
    # 1024表示本次接收的最大字节数
    recv_data = s.recvfrom(1024)
    recv_content =recv_data[0].decode('gbk')
    print(f"收到远程信息:{recv_content} ,from {recv_data[1]}")
    if recv_content == "88":
        print("结束聊天！")
        break
s.close()