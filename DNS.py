import socket


class DNSResolver:
    @staticmethod
    def resolve_hostname(host):
        try:
            return socket.gethostbyname_ex(host)[-1]
        except socket.gaierror:
            return False
