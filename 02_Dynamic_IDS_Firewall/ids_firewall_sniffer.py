import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

THRESHOLD = 40
packet_count = defaultdict(int)
start_time = time.time()
blocked_ips = set()

def packet_callback(packet):
    global start_time, packet_count
    
    if IP in packet:
        src_ip = packet[IP].src
        packet_count[src_ip] += 1
        
        time_interval = time.time() - start_time
        
        if time_interval >= 1:
            for ip, count in list(packet_count.items()):
                packet_rate = count / time_interval
                if packet_rate > THRESHOLD and ip not in blocked_ips:
                    print(f"Blocking IP: {ip}, packet rate: {packet_rate}")
                    os.system(f"iptables -A INPUT -s {ip} -j DROP")
                    blocked_ips.add(ip)
            
            packet_count.clear()
            start_time = time.time()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)
        
    print(f"THRESHOLD {THRESHOLD}")
    print("Monitoring network traffic...")
    sniff(iface="lo", prn=packet_callback)
