import socket
bufsize = 4096
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello UDP server"

client_socket.sendto(msg.encode(),('',PORT))
data, addr = client_socket.recvfrom(bufsize)
print("Server says:")
print(repr(data))
