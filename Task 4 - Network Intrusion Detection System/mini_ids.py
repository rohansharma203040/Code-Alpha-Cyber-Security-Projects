from scapy.all import sniff, IP, TCP
from collections import defaultdict
from datetime import datetime
import threading
import time


total_packets = 0
total_alerts = 0

PORT_SCAN_THRESHOLD = 10
SYN_FLOOD_THRESHOLD = 20
TIME_WINDOW = 10

port_scan_tracker = defaultdict(set)
syn_tracker = defaultdict(int)

lock = threading.Lock()


def log_alert(message):
    global total_alerts
    total_alerts += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"[{timestamp}] ALERT: {message}"

    print(alert_message)

    with open("alerts.log", "a") as f:
        f.write(alert_message + "\n")



def detect_port_scan(src_ip, dst_port):
    port_scan_tracker[src_ip].add(dst_port)

    if len(port_scan_tracker[src_ip]) >= PORT_SCAN_THRESHOLD:
        log_alert(f"Possible Port Scan detected from {src_ip}")
        port_scan_tracker[src_ip].clear()


def detect_syn_flood(src_ip):
    syn_tracker[src_ip] += 1

    if syn_tracker[src_ip] >= SYN_FLOOD_THRESHOLD:
        log_alert(f"Possible SYN Flood detected from {src_ip}")
        syn_tracker[src_ip] = 0


def packet_handler(packet):
    global total_packets
    total_packets += 1

    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags

        # Port scan detection
        detect_port_scan(src_ip, dst_port)

        # SYN detection (pure SYN only)
        if flags & 0x02:
            detect_syn_flood(src_ip)


def display_stats():
    while True:
        time.sleep(5)
        print("\n===== IDS Statistics =====")
        print(f"Total Packets Captured: {total_packets}")
        print(f"Total Alerts Triggered: {total_alerts}")
        print("==========================\n")


if __name__ == "__main__":
    print("Mini Network Intrusion Detection System Started...")
    print("Monitoring network traffic...\n")

    threading.Thread(target=display_stats, daemon=True).start()

    sniff(filter="tcp", iface="wlan0", prn=packet_handler, store=False)
