from collections import Counter
print("=== SOC Real-Time Analyzer v2 ===")
try:
    with open("access.log") as f:
        lines = f.readlines()
except:
    print("لا يوجد logs بعد - سوي هجوم اولاً")
    exit()
print(f"عدد الطلبات: {len(lines)}")
ips = Counter()
blocked = 0
for line in lines:
    parts = line.split()
    if len(parts) >= 3:
        ips[parts[0]] += 1
        if "429" in line:
            blocked += 1
print(f"عدد المحظورة: {blocked}")
for ip, count in ips.items():
    status = "BRUTE FORCE مؤكد - احظره" if count >= 5 else "طبيعي"
    print(f"[!] IP {ip} -> {count} محاولة - {status}")
