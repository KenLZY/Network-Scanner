from scapy.all import ARP, Ether, srp
# ARP - to create ARP request packets
# Ether - to create ethernet frames
# srp - sends and receives packets at layer 2 (Ethernet layer)

targetIp = ""

# create ARP request packet
arp = ARP(pdst=targetIp)

# create ethernet frame
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# ff:ff:ff:ff:ff:ff sets the destination MAC address to broadcast - every device connected to the network will receive the packet

# combine ARP request and ethernet frame
packet = ether / arp

result = srp(packet, timeout=3, verbose=0)[0]