import sys
from scapy.all import *


devices=set()
count=0
def PacketHandler(packet):

	if packet.haslayer(Dot11):
		layer=packet.getlayer(Dot11)
		if layer and (layer.addr2 not in devices):
			global count
			count=count+1
			devices.add(layer.addr2)
			type=layer.type
			if type==0:
				stype="Management"
			elif type==1:
				stype="Control"
			elif type==2:
				stype="Data"
			print(str(count)+"\t"+str(layer.addr1)+"\t"+str(layer.addr2)+"\t"+stype+"\t"+"\n")

		else:
			pass
		
	else:
		print("Not an 802.11 packet\n")

print("S.No\t"+"Transmitter Address\t"+"Recv. Address\t"+"Packet Type\n")
sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)
