# fin-scan : enter ip-target and ports list, you will get list of ports (response:rst=close, no response=open/block)
from scapy.all import IP, TCP, sr1 

def fin_scan(ip_target, ports):
    closed_ports = []
    open_or_block = []

    for port in ports:
        packet = IP(dst=ip_target) / TCP(dport=port, flags="F")
        resp = sr1(packet, timeout=1, verbose=0)

        if resp is None:
            open_or_block.append(port)
            continue

        if resp.haslayer(TCP) and resp[TCP].flags == "R":
            closed_ports.append(port)

    return closed_ports, open_or_block
ip_target=input("Enter target IP: ")
ports_input=input("Enter ports separated by comma (e.g. 2-1024): ")

start_str, end_str = ports_input.split("-")

start_port9=int(start_str.strip())
end_port=int(end_str.strip())

port_list=list(range(start_port9, end_port + 1 ))
closed_ports, open_or_block = fin_scan(ip_target, port_list)
for port in open_or_block:
    print(f"port {port} is open/filtered ")
for port in closed_ports:
     print(f"port {port} is closed ")

    
 