import sys
from scapy.all import *

def PacketHandler(packet):
	if packet.haslayer(Ether):
		source_mac=packet.src
		destination_mac=packet.dst
		print("Source Mac:"+source_mac+"\t"+"Destination Mac:"+destination_mac+"\n")
		if packet.haslayer(IP):
			source_ip=packet.getlayer(IP).src
			destination_ip=packet.getlayer(IP).dst
			print("Source IP:"+str(source_ip)+"\t"+"Destination IP:"+str(destination_ip)+"\n")
		if packet.haslayer(TCP):
			protocol="TCP"
			s_port=packet.getlayer(TCP).sport
			d_port=packet.getlayer(TCP).dport
			flag=packet.getlayer(TCP).flags
			print(protocol)
			print("sport:"+str(s_port)+"\t"+"dport:"+str(d_port))
			print("Flags:"+str(flag)+"\n")
		if packet.haslayer(UDP):
			protocol="UDP"
			s_port=packet.getlayer(UDP).sport
			d_port=packet.getlayer(UDP).dport
			print(protocol)
			print("sport:"+str(s_port)+"\t"+"dport:"+str(d_port)+"\n")
		if packet.haslayer(ARP):
			source_ip=packet.getlayer(ARP).psrc
			destination_ip=packet.getlayer(ARP).pdst
			print("Source IP:"+str(source_ip)+"\t"+"Destination IP:"+str(destination_ip)+"\n")
		if packet.haslayer(DNSQR):
			query=packet.getlayer(DNSQR).qname
			print("Query:"+str(query)+"\n")
			
		print("#"*40)
	
	else:
		print("It is not an ethernet packet\n")


sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)
