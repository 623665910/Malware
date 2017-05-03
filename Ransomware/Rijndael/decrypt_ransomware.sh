#! /bin/bash

#Author : Vasisht Duddu(@vduddu)

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
echo "Decrypting: "; echo $filename
ccrypt -f -q -d $filename -K $secret_key
done
cd $pwd
