import socket
import sys
from datetime import datetime

# Port Scanner - Built by ghbamdycbug-cpu
# Ethical Hacking Tool - For Learning Only

# Common ports with services
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Proxy"
}

print("="*50)
print("🔍 PORT SCANNER v1.0 - By ghbamdycbug-cpu")
print("="*50)

target = input("Enter Target IP / Host [scanme.nmap.org]: ")
if not target:
    target = "scanme.nmap.org"

try:
    target_ip = socket.gethostbyname(target)
    print(f"\n[+] Scanning Target: {target} -> {target_ip}")
    print(f"[+] Started at: {datetime.now()}")
    print("-"*50)
except:
    print("[-] Could not resolve hostname!")
    sys.exit()

open_ports = []

for port, service in common_ports.items():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"[OPEN] Port {port} - {service} ✅")
        open_ports.append(port)
    else:
        print(f"[CLOSED] Port {port} - {service}")
    s.close()

print("-"*50)
print(f"[+] Scan Finished at: {datetime.now()}")
print(f"[+] Total Open Ports: {len(open_ports)} -> {open_ports}")

if 22 in open_ports:
    print("[!] WARNING: SSH is open - Brute Force risk!")
if 21 in open_ports:
    print("[!] WARNING: FTP is open - Check for Anonymous Login!")
if 23 in open_ports:
    print("[!] CRITICAL: Telnet is open - Unencrypted!")
