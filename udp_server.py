import socket

bufsize = 4096
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',12345))
while True:
    data, addr = server_socket.recvfrom(bufsize)
    resp = "UDP server sending data"
    server_socket.sendto(resp,addr)
    print(repr(data))
