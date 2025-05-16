import argparse
from scanner import tcp_port_scan
from geoip import geoip_lookup
from whois_lookup import whois_query

def main():
    parser = argparse.ArgumentParser(description="NetRecon: Network Reconnaissance Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    scan_parser = subparsers.add_parser('scan', help='Scan TCP ports on a target IP')
    scan_parser.add_argument('--ip', required=True, help='Target IP address')
    scan_parser.add_argument('--ports', default='1-1024', help='Port range (ex: 1-1024)')

    sniffer_parser = subparsers.add_parser('sniff', help='Start packet sniffer (requires admin)')
    sniffer_parser.add_argument('--iface', default=None, help='Interface IP to bind (optional)')

    geoip_parser = subparsers.add_parser('geoip', help='Lookup country from IP address')
    geoip_parser.add_argument('--ip', required=True, help='IP address to lookup')

    whois_parser = subparsers.add_parser('whois', help='Perform whois lookup on IP or domain')
    whois_parser.add_argument('--query', required=True, help='IP address or domain')

    args = parser.parse_args()

    if args.command == 'scan':
        start_port, end_port = parse_port_range(args.ports)
        tcp_port_scan(args.ip, start_port, end_port)

    elif args.command == 'sniff':
        run_sniffer(args.iface)

    elif args.command == 'geoip':
        geoip_lookup(args.ip)

    elif args.command == 'whois':
        whois_query(args.query)

def parse_port_range(r):
    try:
        if '-' in r:
            start, end = r.split('-')
            return int(start), int(end)
        else:
            p = int(r)
            return p, p
    except Exception:
        print("Invalid port range format. Use 'start-end' or single port number.")
        exit(1)

if __name__ == "__main__":
    main()
