import os

def get_whois(domain_name):
	print("[+]Scanning for Whois Data")
	try:
		command="whois "+ domain_name
		process=os.popen(command)
		result=str(process.read())
		return result
	except:
		print("[!]Unable to get Whois Data")