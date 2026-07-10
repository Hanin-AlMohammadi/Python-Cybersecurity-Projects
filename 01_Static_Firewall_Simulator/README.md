# 🧱 Static Firewall Rule Simulator

A lightweight Python script that simulates the behavior of a static network firewall. It evaluates incoming generated IP addresses against a predefined blacklist (Access Control List) to dynamically allow or block network traffic.

## 🚀 Overview & Logic
The simulator generates random internal IP addresses (ranging from `192.168.1.0` to `192.168.1.20`) and matches them against a security policy dictionary containing specific blocked IPs. For each simulation run, a random identification number is generated to simulate practical log records.

## 📊 Sample Simulation Output
When executing the script, it processes 12 sequential network connection requests:

```text
ip 192.168.1.4, action: block random: 4321
ip 192.168.1.12, action: allow random: 8765
ip 192.168.1.19, action: block random: 1029
ip 192.168.1.7, action: allow random: 5543
