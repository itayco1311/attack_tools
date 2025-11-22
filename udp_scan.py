from scapy.all import IP, UDP, ICMP, sr1 

target_ip = "8.8.8.8"

for port in range(1,1024):
    pkt = IP(dst=target_ip) / UDP(dport=port)
    response = sr1(pkt, timeout=1, verbose=0)

    if response is None:
        print(f"port {port} is open or black")
    elif response.haslayer(UDP):
        print(f"port {port} is open")

    elif response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code == 3:
        print(f"port {port} is close")
    else:
        print(f"port {port} is open or black")




