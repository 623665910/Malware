from ip_address import *
from directory import *
from whois import *
from robots_txt import *
from nmap import *
from domain_name import *


ROOT_DIR="Websites"
create_dir(ROOT_DIR)

def gather_info(website_name,url):
	domain_name=get_domain_name(url)
	ip_address=get_ip_address(domain_name)
	nmap=get_nmap('-F',ip_address)
	robots_txt=get_robots_txt(url)
	whois=get_whois(domain_name)
	create_report(website_name,url,domain_name,ip_address,nmap,robots_txt,whois)


def create_report(website_name,url,domain_name,ip_address,nmap,robots_txt,whois):
	project_directory=ROOT_DIR +'/'+website_name
	create_dir(project_directory)
	write_file(project_directory + '/full_url.txt',url)
	write_file(project_directory + '/domain_name.txt',domain_name)
	write_file(project_directory + '/ip_address.txt',ip_address)
	write_file(project_directory + '/nmap.txt',nmap)
	write_file(project_directory + '/robots.txt',robots_txt)
	write_file(project_directory + '/whois.txt',whois)

name=raw_input("Enter the name of Website to scan:")
url=raw_input("Enter the url(http://www.<domain>.com):")
gather_info(name,url)
