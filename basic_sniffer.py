from scapy.all import sniff, IP, TCP, UDP, Raw
from collections import defaultdict
from datetime import datetime

# Statistics dictionaries
protocol_stats = defaultdict(int)
source_ip_stats = defaultdict(int)

def packet_callback(packet):
    if IP not in packet:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    timestamp = datetime.now().strftime("%H:%M:%S")

    protocol = "OTHER"

    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        protocol_stats["TCP"] += 1

    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        protocol_stats["UDP"] += 1

    else:
        src_port = "-"
        dst_port = "-"
        protocol_stats["OTHER"] += 1

    source_ip_stats[src_ip] += 1

    # Display packet details
    print("\n==============================")
    print(f"Time            : {timestamp}")
    print(f"Source IP       : {src_ip}")
    print(f"Destination IP  : {dst_ip}")
    print(f"Protocol        : {protocol}")
    print(f"Source Port     : {src_port}")
    print(f"Destination Port: {dst_port}")

    # Payload preview (safe length)
    if Raw in packet:
        payload = packet[Raw].load[:40]
        print(f"Payload Preview : {payload}")

    # Display live statistics
    print("\n--- Traffic Statistics ---")
    print("Protocol Count  :", dict(protocol_stats))

    top_sources = sorted(
        source_ip_stats.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    print("Top Source IPs  :", top_sources)

def start_sniffer():
    interface = input("Enter network interface (eth0 / wlan0): ")
    print(f"\n[*] Sniffing started on {interface}...\n")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffer()
