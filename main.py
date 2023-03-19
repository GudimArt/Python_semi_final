from internet import InternetChecker
from reader import CSVReader
from connection import *
from DNS import DNSResolver


def parse_port_numbers(ports):
    update_ports = []
    for port in ports.split(","):
        try:
            port_int = int(port)
            update_ports.append(port_int)
        except:
            continue
    return update_ports


def main():
    filename = "example.csv"
    internet_checker = InternetChecker()
    ismp_checker = Ping()
    port_checker = TcpPing()
    if internet_checker.check_internet():
        csv_reader = CSVReader()
        rows = csv_reader.read_csv(filename)
        if False in rows:
            pass
        else:
            try:
                for row in rows:
                    ports = parse_port_numbers(row['Ports'])
                    host = row['Host']
                    ip_addresses = None
                    if not host:
                        continue
                    else:
                        if not host.replace('.', '').isdigit():
                            allowed_hostnames = DNSResolver.resolve_hostname(
                                host)
                            if allowed_hostnames == 0:
                                print(f'Error unable to resolve server domain name')
                                continue
                            else:
                                ip_addresses = allowed_hostnames
                        else:
                            ip_addresses = [host]
                            host = '??'
                        if not ports:
                            print(host)
                            for ip_address in ip_addresses:
                                ismp_checker.check_icmp(ip_address)
                        else:
                            print(host)
                            for ip_address in ip_addresses:
                                for port in ports:
                                    port_checker.check_port(ip_address, port)
            except:
                print("Check the entered data")
    else:
        print("you don't have an internet connection")


if __name__ == '__main__':
    main()
