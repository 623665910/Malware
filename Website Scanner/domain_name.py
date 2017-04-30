from tld import get_tld

def get_domain_name(url):
	print("[+]Acquiring Domain name")
	try:
		domain_name=get_tld(url)
		return domain_name
	except:
		print("[!]COuld not get Domain Name!!")