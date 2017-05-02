import socket
import textwrap
import struct

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '

def ether_frame(data):
	#unpack etherbet frame
	dest_mac,src_mac,protocol=struct.unpack('! 6s 6s 6s H',data[:14])
	return get_mac_address(dest_mac), get_mac_address(src_mac), socket.htons(protocol), data[14:]

def get_mac_address(bytes_addr):
	#Formats mac address in a proper format(AA:BB:CC:DD:EE:FF)
	bytes_strmap=map('{:02x}'.format, bytes_addr)
	mac_addr=':'.join(bytes_str).upper()
	return mac_addr

def main():
	connection=socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	while True:
		raw_data,addr=connection.recvfrom(65536)
		dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
		print('\nEthernet Frame:')
		print(TAB_1+'Destination: {}, Source: {}, Protocol: {}'.format(dest_mac,src_mac,eth_proto))

		if eth_proto==8:
			(version,header_length,ttl,proto,src,target,data)=ipv4_packet(data)
			print(TAB_1+'IPv4 Packet:')
			print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(version,header_length,ttl))
            print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(proto, src, target))

		elif eth_proto==1:
			 icmp = ICMP(ipv4.data)
            print(TAB_1 + 'ICMP Packet:')
            print(TAB_2 + 'Type: {}, Code: {}, Checksum: {},'.format(icmp_type,code, checksum))
            print(TAB_2 + 'ICMP Data:')
            print(format_multi_line(DATA_TAB_3, data))

		elif eth_proto == 17:
            src_port,dest_port,length,data = udp_packet(data)
            print(TAB_1 + 'UDP Segment:')
            print(TAB_2 + 'Source Port: {}, Destination Port: {}, Length: {}'.format(src_port,dest_port, size))

		elif eth_proto==6:
			(src_port, dest_port,sequebce, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data)=tcp_packet(data)
			print(TAB_1 + 'TCP Segment:')
            print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(src_port, dest_port))
            print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(sequence, acknowledgment))
            print(TAB_2 + 'Flags:')
            print(TAB_3 + 'URG: {}, ACK: {}, PSH: {}'.format(flag_urg, flag_ack, flag_psh))
            print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(flag_rst, flag_syn, flag_fin))
			print(format_multi_line(DATA_TAB_3,data))

		else:
            print(TAB_1 + 'Other IPv4 Data:')
            print(format_multi_line(DATA_TAB_2, data))

def ipv4_packet(data):
	#unpack IP Packet
	version_header_length=data[0]
	version=version_header_length >> 4
	header_length = (version_header_length & 15) * 4
	ttl,protocol,src,dest=struct.unpack('! 8x B B 2x 4s 4s',data[:20])
	return version,header_length, ttl, protocol,ipv4(src),ipv4(dest),data[data_header:]

#Returns Formatted IPv4 Address
def ipv4(addr):
	return '.'.join(map(str,addr))

def icmp_packet(data):
	icmp_type,code,checksum=struct.unpack('! B B H', data[:4])
	return icmp_type,code,checksum,data[4:]

def tcp_packet(data):
	(src_port,dest_port,sequence,acknowledgement,offest_reserved_flags)=struct.unpack('! H H L L H',data[:14])
	offset=(offset_reserved_flags >> 12) * 4
	flag_urg=(offset_reserved_flags & 32)>> 5
	flag_ack=(offset_reserved_flags & 16)>> 4
	flag_psh=(offset_reserved_flags & 8)>>  3
	flag_rst=(offset_reserved_flags & 4)>>2
	flag_syn=(offset_reserved_flags & 2)>>1
	flag_fin=(offset_reserved_flags & 1)
	return src_port, dest_port,sequebce, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]


def udp_packet(data):
	src_port, dest_port,size=struct.unpack('! H H 2x H',data[:8])
	return src_port,dest_port,size

def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


main()
