#coding=utf-8
from socket import *
# 创建TCP类型的套接字
client_socket = socket(AF_INET, SOCK_STREAM)
# 绑定接收信息接口
client_socket.connect(('127.0.0.1',8899))
'''
    注意：
    1.tcp客户端已经链接好了服务器，所在在以后的数据发送中，不需要填写对方的ip、port ---> 打电话
    2.udp在发送数据时，因为没有之前的链接，所以需要在每次的发送各种，都需要填写接收方的ip和port -->写信

'''
client_socket.send("林大侠".encode("gbk"))
client_socket.close()