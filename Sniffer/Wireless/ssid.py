import sys
from scapy.all import *

ssid=set()
count=0
def PacketHandler(packet):
	if packet.haslayer(Dot11Beacon):
		if packet.info and (packet.info not in ssid):
			ssid.add(packet.info)
			global count
			count=count+1
			print(str(count)+"\t"+packet.info+"\t"+packet.addr3+"\n")
		else:
			pass
	else:
		pass	

print("S.No\t"+"SSID\t"+"BSSID\n")
sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)
