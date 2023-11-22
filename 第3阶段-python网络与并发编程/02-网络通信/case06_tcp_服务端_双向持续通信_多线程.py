# coding=utf-8
from socket import *
from threading import Thread
'''
    双向通信socket之服务器端
        读取客户端发送的数据，将内容输出到控制台
        将控制台输入的信息发送到客户端
'''
def recv_data():
    while True:
        redata = tcp_client_socket.recv(1024).decode("gbk")
        print(f'收到客户端信息:{redata}')
        if redata == 'end':
            break

def send_data():
    while True:
        msg = input('>')
        tcp_client_socket.send(msg.encode('gbk'))

if __name__ == '__main__':
    # 创建TCP类型的套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定接收信息接口
    tcp_server_socket.bind(('127.0.0.1', 8888))
    tcp_server_socket.listen(5)
    print("服务端已经启动，等待客户端链接！")
    # 接收客户端链接
    tcp_client_socket, host = tcp_server_socket.accept()
    print("1个客户端建立链接成功！")

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    tcp_client_socket.close()
    tcp_server_socket.close()