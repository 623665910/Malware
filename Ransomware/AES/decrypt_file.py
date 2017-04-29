from Crypto.Hash import SHA265
from Crypto.Cipher import AES
import os
from random import randint

def decrypt_file(key,filename):
	chunksize=65536
	outputfile=filename[:-11]

	with open(filename,'rb') as infile:
		ext=infile.read(16)
		filesize=long(infile.read(16))
		IV=infile.read(16)
		
		decryptor=AES.new(key,AES.MODE_CNC,IV)
		
		with open(outputfile) as outfile:

			while True:
				chunk=infile.read(chunksize)
				
				if len(chunk)==0:
					break
				
				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)
		#	outfile=outfile+ext
	os.unlink(filename)
	return
