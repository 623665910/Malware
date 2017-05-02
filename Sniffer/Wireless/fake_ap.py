import sys
from scapy.all import *

broadcast="ff:ff:ff:ff:ff:ff"
bssid="aa:aa:aa:aa:aa:aa"

packet=RadioTap()/Dot11(addr1=broadcast,addr2=bssid,addr3=bssid)/Dot11Beacon(cap=0x1104)/Dot11Elt(ID=0,info=sys.argv[3])/Dot11Elt(ID=1,info="\x82\x84\x8b\x96\x24\x30\x48\6c")/Dot11Elt(ID=3,info="\x06")/Dot11Elt(ID=5,info="\x00\x01\x00\x00")

sendp(packet,iface=sys.argv[1],count=int(sys.argv[2]),inter=.2)
