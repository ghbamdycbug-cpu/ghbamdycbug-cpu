import time
print("=== SOC Live Monitor - يراقب الآن ===")
print("اضغط CTRL+C للايقاف")
seen = 0
while True:
    try:
        with open("access.log") as f:
            lines = f.readlines()
        if len(lines) > seen:
            for line in lines[seen:]:
                print(f"[NEW] {line.strip()}")
                if "429" in line:
                    print(">>> 🚨 تنبيه: محاولة هجوم محظورة!")
            seen = len(lines)
        time.sleep(2)
    except FileNotFoundError:
        time.sleep(2)
