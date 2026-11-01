import socket
import subprocess
import ipaddress

print("="*50)
print("📡 WIFI NETWORK SCANNER - SOC TOOL #6")
print("="*50)

# نطلع IP حقنا
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    print(f"[+] Your IP: {my_ip}")
except:
    my_ip = "192.168.1.100"

# نحسب الشبكة
network = ".".join(my_ip.split(".")[:3]) + ".0/24"
print(f"[+] Scanning network: {network}")
print(f"[*] Scanning 1-254... please wait\n")

alive = []
for i in range(1, 255):
    ip = f"{'.'.join(my_ip.split('.')[:3])}.{i}"
    # ping سريع
    result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "Unknown"
        alive.append((ip, hostname))
        print(f"[+] LIVE: {ip} - {hostname}")

print("\n" + "="*50)
print(f"[DONE] Found {len(alive)} devices on your network")
for ip, host in alive:
    print(f"  - {ip} : {host}")

if len(alive) > 10:
    print("\n[!] WARNING: Many devices! Check for strangers!")
else:
    print("\n[+] Network looks normal")
print("="*50)
