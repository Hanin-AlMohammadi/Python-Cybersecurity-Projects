import sys
import time
from scapy.all import IP, TCP, send

TARGET_IP = "127.0.0.1"
NUM_PACKETs = 100
DURATION = 5

def send_packets(target_ip, num_packets, duration):
    packet = IP(dst=target_ip) / TCP()
    end_time = time.time() + duration
    packet_count = 0

    while time.time() < end_time and packet_count < num_packets:
        send(packet, verbose=False)
        packet_count += 1

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("This script requires python 3.")
        sys.exit(1)

    send_packets(TARGET_IP, NUM_PACKETs, DURATION)
