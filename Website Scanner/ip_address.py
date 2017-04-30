import socket

def get_ip_address(domain_name):
	print("[+]Obtaining IP Address")
	try:
		ip_address=socket.gethostbyname(domain_name)
		return ip_address
	except:
		print("[!]Unable to get IP Address")