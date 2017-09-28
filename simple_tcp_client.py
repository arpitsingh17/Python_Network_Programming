import sys
import socket

if __name__ == '__main__':
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	except socket.error:
		print ("Failed")

		sys.exit()

	print ('socket created')

	target_host = "www.sjsu.edu"
	target_port = 80
	BUFSIZ = 4096
	sock.connect((target_host,target_port))

	while True:
		data = 'GET / HTTP/1.0\r\n\r\n'
		if not data:
			break
		sock.send(data.encode('utf-8'))
		data = sock.recv(BUFSIZ)
		if not data:
			break
		print(data.decode('utf-8'))

	sock.close()
