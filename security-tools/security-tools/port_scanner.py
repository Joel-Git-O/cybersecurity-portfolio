#!/usr/bin/env python3
"""
Port Scanner - Basic TCP port scanner for network reconnaissance
Author: Joel Massicot
Usage: python3 port_scanner.py <target> [start_port] [end_port]
"""

import socket
import sys
import concurrent.futures
from datetime import datetime


def scan_port(target: str, port: int, timeout: float = 1.0) -> tuple:
    """Attempt to connect to a single port. Returns (port, is_open, banner)."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                # Try to grab a banner
                try:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                except Exception:
                    banner = ''
                return (port, True, banner)
    except socket.error:
        pass
    return (port, False, '')


def resolve_target(target: str) -> str:
    """Resolve hostname to IP address."""
    try:
        return socket.gethostbyname(target)
    except socket.gaierror as e:
        print(f"Error resolving {target}: {e}")
        sys.exit(1)


def scan_range(target: str, start_port: int, end_port: int, max_workers: int = 100) -> list:
    """Scan a range of ports using thread pool for speed."""
    open_ports = []
    ports = range(start_port, end_port + 1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in ports}
        for future in concurrent.futures.as_completed(futures):
            port, is_open, banner = future.result()
            if is_open:
                open_ports.append((port, banner))

    return sorted(open_ports, key=lambda x: x[0])


def get_service_name(port: int) -> str:
    """Try to identify the service running on a port."""
    try:
        return socket.getservbyport(port)
    except OSError:
        return 'unknown'


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 port_scanner.py <target> [start_port] [end_port]")
        print("Example: python3 port_scanner.py 192.168.1.1 1 1024")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    print(f"\nPort Scanner - Joel Massicot")
    print(f"Target: {target}")
    ip = resolve_target(target)
    print(f"Resolved IP: {ip}")
    print(f"Port range: {start_port} - {end_port}")
    print(f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = scan_range(ip, start_port, end_port)

    if open_ports:
        print(f"\nOpen ports found: {len(open_ports)}")
        print(f"{'PORT':<10} {'SERVICE':<20} {'BANNER'}")
        print("-" * 60)
        for port, banner in open_ports:
            service = get_service_name(port)
            banner_preview = banner[:40] if banner else '-'
            print(f"{port:<10} {service:<20} {banner_preview}")
    else:
        print("No open ports found in the specified range.")

    print(f"\nScan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
