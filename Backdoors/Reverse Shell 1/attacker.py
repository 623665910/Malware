import socket
import sys

#creating socket
def socket_create():
	try:
		global host,port,s
		host=''
		port=9999
		s=socket.socket()
	except socket.error as err:
		print("[!]Error in creating Socket!!")


#Bind socket to port
def socket_bind():
	try:
		global host,port,s
		print("[+]Binding Socket to port")
		s.bind((host,port))
		s.listen(5)
	except socket.error as err:
		print("[!]Error in Binding Socket")
		socket_bind()

#Accept connections
def socket_accept():
	connection,address=s.accept()
	print("[+]Connection has been established")
	print("IP:"+str(address[0]))
	print("Port:"+str(address[1]))
	send_commands(connection)
	connection.close()

def send_commands(connection):
	while True:
		command=raw_input()
		if command=='quit':
			connection.close()
			s.close()
			sys.exit()
		if len(str.encode(command))>0:
			connection.send(str.encode(command))
			client_response=str(connection.recv(1024))
			print(client_response)


def main():
	socket_create()
	socket_bind()
	socket_accept()

main()
