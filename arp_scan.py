from scapy.all import ARP, Ether, srp

def arp_scan(ip_range):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip_range)
    result = srp(packet,timeout=2, verbose=0)[0]

    for _, recived in result:
        print(f"IP: {recived.psrc} | MAC:{recived.hwsrc}")
arp_scan("10.0.0.3/24")
