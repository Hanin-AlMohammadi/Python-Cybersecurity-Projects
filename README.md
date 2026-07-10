# 🐍 Python for Cybersecurity Portfolio

Welcome to my personal cybersecurity repository! This portfolio showcases a collection of practical tools, security scripts, and automation mechanisms built using Python.

## 🛠️ Repository Index

Each project is contained within its own dedicated directory, featuring its own localized documentation, source code, and simulation results:

### 🧱 Static Firewall Rule Simulator
* **Directory:** `[01_Static_Firewall_Simulator](./01_Static_Firewall_Simulator)`
* **Core Script:** `static_firewall.py`
* **Description:** A network simulation environment that evaluates internal IP address requests against a pre-defined Access Control List (ACL) blacklist to allow or drop traffic.
* **Key Skills:** Logic Control, Automated Logging, Access Control Lists (ACL).

### 🛡️ Dynamic Network IDS & Firewall Mitigation
* **Directory:** `[02_Dynamic_IDS_Firewall](./02_Dynamic_IDS_Firewall)`
* **Core Scripts:** `ids_firewall_sniffer.py` & `packet_flooder_simulator.py`
* **Description:** An advanced Intrusion Prevention System (IPS) that sniffs live loopback traffic using `Scapy`, calculates volumetric packet velocities, and dynamically deploys Linux kernel-level `iptables` mitigation rules against DoS attacks.
* **Key Skills:** Live Packet Sniffing, Network Security, Automation (`iptables`), Traffic Analysis.

### 🚨 3. Hybrid IDS/IPS & Signature-Based Malware Filter
* **Directory:** `[03_Hybrid_IDS_Malware_Filter](./03_Hybrid_IDS_Malware_Filter)`
* **Core Scripts:** `hybrid_ids_firewall.py` & `test_nimda.py`
* **Description:** A comprehensive Hybrid IDS/IPS engine integrating Signature-based Deep Packet Inspection (DPI) to block specific malware payload streams alongside Volumetric Flood analysis. Features automated dual-channel event alerting via native desktop popups and real-time out-of-band Telegram Bot API integration.
* **Key Skills:** Deep Packet Inspection (DPI), Threat Signature Matching, SOC Automation, API Integration, Dynamic Incident Response.
  
---

## 🚀 Environment & Setup

To explore or run any tool in this portfolio:
1. Ensure you are working within a secure, authorized testing environment (e.g., Kali Linux).
2. Navigate into the targeted project directory.
3. Review the localized `README.md` file for script prerequisites and specific instructions.
4. Execute the core Python 3 scripts with appropriate system privileges.

---

## 🔒 Disclaimer
*The scripts and tools provided in this repository are developed exclusively for educational, authorized defensive simulation, and security research purposes. Unauthorized testing against remote networks is strictly prohibited.*
