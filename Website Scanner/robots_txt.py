import codecs
import urllib2

def get_robots_txt(url):
	print("[+]Getting Robots.txt")
	if url.endswith('/'):
		path=url
	else:
		path=url+"/"
	try:
		req=urllib2.Request(path+"robots.txt",data=None)
		response=urllib2.urlopen(req)
		page=response.read()
		page=page.encode('utf8')
		return page
	except:
		print("Could not retrieve Robots.txt!!")