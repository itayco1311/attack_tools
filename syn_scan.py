from scapy.all import IP, TCP, sr1

def syn_scan(ip,port):
    packet = IP(dst=ip) / TCP(dport=port, flags="S")
    response = sr1(packet, timeout=2, verbose=0)

    if response is None:
        print(f"Port {port} is FILTERED or BLOCKED")

    elif response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            print(f"port {port} is open ! ")
      
def scan_port_range(ip, start_port, end_port):
     for port in range(start_port, end_port + 1):
          syn_scan(ip,port)
     

         
scan_port_range("10.0.0.3", 20, 1023)