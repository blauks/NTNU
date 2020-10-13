from scapy.all import *
from scapy.utils import rdpcap

pkts = rdpcap("communication.pcap") #Import the assignment PCAP file
pkts = defragment(pkts) #Defragment the packets

ports = [8080] #Define what ports I want to filter out
pktsFiltered = (pkt for pkt in pkts if TCP in pkt and (pkt[TCP].sport in ports or pkt[TCP].dport in ports)) #Extract all packets with port 8080

wrpcap('filteredPackets.pcap', pktsFiltered) #Write the packets to a pcap file, since scapy thought this was better than using a variable
pktsF = rdpcap('filteredPackets.pcap')

server_pkts = PacketList([p for p in pktsF if p[IP].src== '192.168.1.4' and Raw in p])
resp = b''.join(packet[Raw].load for packet in server_pkts) #Add the data from all the packets into one long hexdump

with open('response', 'wb') as f: #Write the hex to a file
        f.write(resp)
        f.close()

        