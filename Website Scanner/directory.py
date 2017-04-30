import os

def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		print("[+]Created a new Directory")
	else:
		print("[!]Directory already present")
def write_file(path,data):
	f=open(path,'w')
	f.write(data)
	f.close()