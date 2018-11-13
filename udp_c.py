import socket
byte = 1024
# 两个端口要保持一致
port = 28601
host = "192.168.0.255"
addr = (host, port)
# lsof -i udp:port
# kill pid
# 创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定
sock.bind(addr)
print("waiting to receive messages...")

while True:
    (data, addr) = sock.recvfrom(byte)
    text = data
    if text == 'exit':
        break
    else:
        # print('The client at {} says {!r}'.format(addr, text))
        print(addr,text)
        text = 'Your data was {}bytes long'.format(len(data))
        data = text.encode('GBK')
        # sock.sendto(data, addr)

# 关闭套接字
sock.close()
