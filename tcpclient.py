import socket

HOST = 'localhost'
PORT = 12345
BUFSIZ = 256

if __name__ == '__main__':
	client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host =  HOST
	port =  PORT

	sock_addr = (host, int(port))
	client_sock.connect(sock_addr)

	payload ='GET TIME'
	try:
		while True:
			client_sock.send(payload.encode('utf-8'))
			data = client_sock.recv(BUFSIZ)
			print(repr(data))
			more = raw_input("Want to send more data to server[y/n]:")
			if more == 'y':
				print("test line 23")
				payload = raw_input("Enter payload: ")
			elif more == 'n':
				break

	except KeyboardInterrupt:
		print("   Exited by user")

	client_sock.close()
