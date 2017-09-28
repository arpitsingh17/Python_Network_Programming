import sys
import socket

if __name__ == '__main__':
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	except socket.error:
		print ("Failed")

		sys.exit()

	print ('socket created')

	target_host = "www.python.org"
	target_port = 80

	try:
		sock.connect((target_host,int(target_port)))
		print('Socket connected')

	#sock.shutdown(2)
	except socket.error:
		print("Failed to connect")
