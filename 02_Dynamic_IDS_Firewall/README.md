# 🛡️ Dynamic Network IDS & Firewall Mitigation

An advanced Python-based Intrusion Detection and Prevention System (IPS) utilizing Scapy to sniff network traffic on the loopback interface. It dynamically calculates packet rates from incoming IPs and automatically deploys Linux iptables rules to drop traffic from sources attempting a Denial of Service (DoS) attack.

## 🚀 Overview & Architecture
This project consists of two core scripts:
1. **ids_firewall_sniffer.py**: The main defensive engine that continuously analyzes packet counts per second. If an IP exceeds 40 packets/sec, it isolates the threat.
2. **packet_flooder_simulator.py**: A dedicated network testing/flooding tool used to simulate an automated volumetric attack targeting 127.0.0.1.

## 📊 Live Simulation Result
When executing the attack flooder against the active monitoring engine, the system detects the anomaly within the first interval window and triggers the automated mitigation:

> **THRESHOLD 40**  
> **Monitoring network traffic...**  
> **Blocking IP: 127.0.0.1, packet rate: 101.23666151363572**

## 🛠️ How to Run
To accurately simulate the dynamic mitigation, execute both components on your Linux machine with proper network privileges:

1. Initiate the IDS/Firewall engine:
   `sudo python3 ids_firewall_sniffer.py`
2. In a parallel terminal instance, run the simulation tool:
   `sudo python3 packet_flooder_simulator.py`

## 🧠 Key Cybersecurity Concepts Applied
* **Dynamic Traffic Sniffing:** Utilizing low-level socket abstraction via Scapy to capture packets in real-time.
* **Automated Threat Mitigation:** Direct integration with Kernel-level netfilter via Linux iptables syntax.
* **Rate Limiting Analysis:** Implementing sliding execution windows to measure real-time connection velocities.
