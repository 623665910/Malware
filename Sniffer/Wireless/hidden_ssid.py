import sys
from scapy.all import *

#Find beacons with length 0 and monitor probe responses to get name of ssid


hiddenssid=set()
name=set()
def PacketHandler(packet):
	
	if packet.haslayer(Dot11Beacon):
		if len(packet.info)==0:
			if packet.addr3 not in hiddenssid:
				print("Found Hidden SSID:"+packet.addr3)
				hiddenssid.add(packet.addr3)

	elif packet.haslayer(Dot11ProbeResp) and (packet.addr3 in hiddenssid):
		if packet.info not in name:
			print("Hidden SSID Details:"+packet.addr3+"\t"+packet.info)
			name.add(packet.info)




sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)
