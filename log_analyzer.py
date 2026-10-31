import re
from collections import Counter

def analyze_logs():
    print("🕵️ محلل سجلات الهجمات - Log Analyzer")
    print("="*40)
    
    # نسوي ملف سجلات وهمي للتجربة
    fake_logs = """192.168.1.10 - Failed login for admin
45.33.22.11 - Failed login for root
192.168.1.10 - Failed login for admin
10.0.0.5 - Successful login for user
45.33.22.11 - Failed login for admin
45.33.22.11 - Failed login for root
45.33.22.11 - Failed login for admin
192.168.1.10 - Port scan detected
8.8.8.8 - Successful login for admin
45.33.22.11 - Failed login for admin"""

    print("📄 السجلات اللي بنحللها:")
    print(fake_logs)
    print("\n" + "="*40)
    
    # نطلع كل الـ IPs
    ips = re.findall(r"\d+\.\d+\.\d+\.\d+", fake_logs)
    failed = fake_logs.count("Failed login")
    success = fake_logs.count("Successful login")
    scans = fake_logs.count("Port scan")
    
    print(f"📊 النتائج:")
    print(f"❌ محاولات فاشلة: {failed}")
    print(f"✅ دخول ناجح: {success}")
    print(f"🔍 فحص منافذ: {scans}")
    
    print("\n🚨 أكثر IP مشبوه:")
    counts = Counter(ips)
    for ip, count in counts.most_common():
        if count >= 3:
            print(f"🔴 {ip} - {count} مرات! -> بلوك فوراً! BLOCK!")
        elif count >= 2:
            print(f"🟡 {ip} - {count} مرات - راقبه")
        else:
            print(f"🟢 {ip} - {count} مرة - طبيعي")

    print("\n💡 التوصية: IP 45.33.22.11 قاعد يهاجمك، احظره!")

if __name__ == "__main__":
    analyze_logs()
