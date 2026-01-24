# Task 4: Network Intrusion Detection System (NIDS)

## 📌 Overview

This project implements a basic Network Intrusion Detection System (NIDS) using Python and Scapy.  
The system monitors live TCP traffic and detects suspicious activities such as:

- SYN Flood Attacks
- Port Scanning Behavior

The IDS captures packets in real time, analyzes TCP flags and destination ports, and generates alerts when abnormal patterns exceed defined thresholds.

---

## ⚙️ Technologies Used

- Python 3
- Scapy (Packet Sniffing & Analysis)
- hping3 (Attack Simulation Tool)
- Kali Linux

---

## 🧠 Detection Logic

### 1️⃣ SYN Flood Detection

The system monitors TCP packets and checks if the SYN flag is set:

```python
if flags & 0x02:


The SYN flag (0x02) indicates a TCP connection initiation attempt.
If SYN packets from the same source IP exceed:

SYN_FLOOD_THRESHOLD = 20

An alert is generated:

--> ALERT: Possible SYN Flood detected

Port Scan Detection

The IDS tracks unique destination ports accessed by a source IP:

--> port_scan_tracker[src_ip].add(dst_port)


If the number of unique ports exceeds:

--> PORT_SCAN_THRESHOLD = 10

An alert is generated indicating possible port scanning behavior.

⚙️ Configuration Values

Default configuration:
-->
PORT_SCAN_THRESHOLD = 10
SYN_FLOOD_THRESHOLD = 20
TIME_WINDOW = 10
<--
These values can be modified depending on network sensitivity.

🌐 Network Interface Configuration

The IDS monitors a specific interface:
--> sniff(filter="tcp", iface="wlan0", prn=packet_handler, store=False)

The interface depends on how the system is connected to the network.

🔹 If Using WiFi (Wireless)

Check interface:

--> ip a


Example:

-> wlan0


Example IP:

-> 172.20.10.3


Find gateway:

--> ip route


Example:

->default via 172.20.10.1 dev wlan0


For testing, attack the gateway:

-> 172.20.10.1

🔹 If Using Ethernet (Wired Connection)

If connected via LAN cable:

-> eth0


Check using:

--> ip a


Find gateway:

--> ip route


Example:

-> default via 192.168.1.1 dev eth0


Update IDS:

--> sniff(filter="tcp", iface="eth0", prn=packet_handler, store=False)


Attack:

-> 192.168.1.1

⚠️ Important: Why Localhost May Not Trigger Detection

Attacking your own IP (127.0.0.1 or system IP) may not trigger detection because:
Linux may handle local traffic internally.
Packets may not traverse the physical network interface.
Scapy may not capture internal traffic properly.
For accurate testing, always target:

Network gateway
Another device on the same network

🧪 Testing Procedure
Step 1 – Run IDS
-> sudo python3 mini_ids.py

Step 2 – Simulate SYN Flood
Attack the gateway:
-> sudo hping3 -S -p 80 -c 50 <gateway_ip>


Example:

-> sudo hping3 -S -p 80 -c 50 172.20.10.1

Expected Alert Output
--> [YYYY-MM-DD HH:MM:SS] ALERT: Possible SYN Flood detected from <IP>


Alerts are also stored in:

-> alerts.log

📊 Output Features
Real-time alert display
Packet counter
Alert counter
Log file storage

📁 Project Structure
Task 4 - Network Intrusion Detection System/
├── mini_ids.py
├── README.md
└── alerts.log (ignored in .gitignore)

🎯 Learning Outcomes

This project demonstrates:
Real-time packet sniffing
TCP flag analysis
Behavior-based intrusion detection
Interface-level monitoring
Understanding of Linux networking behavior
Practical attack simulation
