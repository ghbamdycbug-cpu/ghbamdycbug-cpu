import time
import re
from collections import Counter, defaultdict

print("=== SOC Live Monitor v2.0 ===")
print("Monitoring access.log ... Press CTRL+C to stop")
print("-" * 50)

seen = 0
ip_counter = Counter()
blocked_ips = set()
attack_patterns = {
    "SQL Injection": r"(union|select|or 1=1|' or|\" or|drop table|--|;--)",
    "XSS Attack": r"(<script|alert\(|onerror=|onload=|javascript:)",
    "Path Traversal": r"(\.\./|/etc/passwd|/etc/shadow|%2e%2e)",
    "Scanner": r"(nmap|nikto|sqlmap|dirbuster|masscan)",
}

def log_incident(msg):
    with open("incident_report.txt", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

while True:
    try:
        with open("access.log") as f:
            lines = f.readlines()
        if len(lines) > seen:
            for line in lines[seen:]:
                line = line.strip()
                if not line:
                    continue
                print(f"[NEW] {line}")

                # Extract IP (first part)
                ip = line.split()[0] if line.split() else "unknown"
                ip_counter[ip] += 1

                # Check status codes
                if " 429 " in line or " 403 " in line:
                    print(f">>> 🚨 BLOCKED / RATE LIMIT from {ip}")
                    log_incident(f"BLOCKED/RATE-LIMIT from {ip} : {line}")

                if " 500 " in line or " 502 " in line or " 503 " in line:
                    print(f">>> ⚠️ SERVER ERROR from {ip}")
                    log_incident(f"SERVER ERROR from {ip} : {line}")

                if " 404 " in line:
                    print(f">>> 🔍 404 Not Found - Possible Scanning from {ip}")

                # Check attack patterns
                low = line.lower()
                for name, pattern in attack_patterns.items():
                    if re.search(pattern, low):
                        print(f">>> 🔥 {name} DETECTED from {ip} !!!")
                        log_incident(f"{name} from {ip} : {line}")

                # Brute Force detection: >5 requests from same IP
                if ip_counter[ip] == 6 and ip not in blocked_ips:
                    print(f">>> 🛑 BRUTE FORCE / FLOOD from {ip} - 6+ requests!")
                    log_incident(f"BRUTE FORCE from {ip} - {ip_counter[ip]} requests")
                    blocked_ips.add(ip)

            seen = len(lines)
        time.sleep(2)
    except FileNotFoundError:
        print("Waiting for access.log...")
        time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+] Monitor stopped. Stay safe!")
        break
