from abc import ABC, abstractmethod
from pythonping import ping
import socket
import time
import datetime


class ICheckICMP(ABC):
    @abstractmethod
    def check_icmp(self, ip_address):
        pass


class ICheckPorts(ABC):
    @abstractmethod
    def check_port(self, ip_address, port):
        pass


class Ping(ICheckICMP):
    def check_icmp(self, ip_address):
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        response_list = ping(ip_address, count=4)
        if response_list.success():
            print(
                f"{date} {ip_address} is reachable; average round-trip time: {response_list.rtt_avg_ms} ms.")
        else:
            print(f"{date} {ip_address} is not reachable")


class TcpPing(ICheckPorts):
    def check_port(self, ip_address, port):
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        total_time = 0
        retries = 4
        lost_packets = []
        for i in range(retries):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            start_time = time.time()
            try:
                sock.connect((ip_address, port))
                end_time = time.time()
                total_time += end_time - start_time
                lost_packets.append(False)
            except socket.error:
                lost_packets.append(True)
            finally:
                sock.close()
        avg_time = round(total_time / retries * 1000, 2)
        if False in lost_packets:
            print(
                f"{date} {ip_address}:{port} is reachable; average round-trip time: {avg_time} ms.")
        else:
            print(f"{date} {ip_address}:{port} is not reachable.")
