# coding: utf-8
from socket import *

HOST = 'localhost'  # 主机名
PORT = 21567  # 端口号 与服务器一致
BUFSIZE = 1024  # 缓冲区大小1K
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:  # 无限循环等待连接到来
    try:
        data = input('>')
        if not data:
            break
        udpCliSock.sendto(data.encode(), ADDR)  # 发送数据
        data, ADDR = udpCliSock.recvfrom(BUFSIZE)  # 接受数据
        if not data:
            break
        print('Server : ', data)

    except Exception as e:
        print('Error: ', e)

udpCliSock.close()  # 关闭客户端