import os

def get_nmap(options,ip):
	print("[+]Scanning for Nmap Results")
	try:
		command="nmap "+options+" "+ip
		process=os.popen(command)
		scan_result=str(process.read())
		return scan_result
	except:
		print("[!]Unable to Retreive Nmap Results")