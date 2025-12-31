import pandas as pd
from scapy.all import IP, TCP, UDP

class TrafficFeatureExtractor:
    def __init__(self):
        self.active_flows = {}  # Key: (src_ip, dst_ip, src_port, dst_port, proto)

    def process_packet(self, packet):
        # We only care about IP traffic
        if not packet.haslayer(IP):
            return None

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)

        # Try to get ports (TCP/UDP)
        src_port = 0
        dst_port = 0
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        # Flow ID
        flow_key = (src_ip, dst_ip, src_port, dst_port, protocol)

        # Simple feature extraction logic (simplified for demo)
        # In real world: You would calculate flow duration, std dev of packet times, etc.
        features = {
            'packet_length': length,
            'protocol_type': protocol,
            'src_port': src_port,
            'dst_port': dst_port
        }
        
        return features
