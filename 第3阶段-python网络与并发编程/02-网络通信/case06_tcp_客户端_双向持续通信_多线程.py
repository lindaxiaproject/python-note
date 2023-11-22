#coding=utf-8
from socket import *
from threading import Thread
'''
双向通信Socket之客户端
    将控制台输入的信息发送给服务端
    读取服务端的数据，将内容输出到控制台
'''

def recv_data():
    while True:
        redata = tcp_client_socket.recv(1024).decode("gbk")
        print(f'\n收到服务端信息:{redata}')
        if redata == 'end':
            break

def send_data():
    while True:
        msg = input('>')
        tcp_client_socket.send(msg.encode('gbk'))
        if msg == 'end':
            break

if __name__ == '__main__':
    # 创建客户端socket对象
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定接收信息接口
    tcp_client_socket.connect(('127.0.0.1', 8888))
    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    tcp_client_socket.close()