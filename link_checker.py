import re
import socket
from urllib.parse import urlparse

# قائمة الروابط المختصرة المشبوهة
SHORTENERS = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "cutt.ly"]

# كلمات تدل على التصيد
PHISHING_WORDS = ["login", "verify", "free", "gift", "win", "bank", "paypal", "secure"]

def check_url(url):
    print(f"\n🔍 جاري فحص: {url}")
    score = 0
    reasons = []

    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # 1. فحص https
    if not url.startswith("https://"):
        score += 20
        reasons.append("⚠️ الموقع ما يستخدم HTTPS آمن")

    # 2. فحص الروابط المختصرة
    if any(s in domain for s in SHORTENERS):
        score += 30
        reasons.append("⚠️ رابط مختصر - ممكن يخفي موقع خبيث")

    # 3. فحص IP بدل دومين
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        score += 40
        reasons.append("🚨 الدومين عبارة عن IP - خطير جدا!")

    # 4. فحص كلمات التصيد
    for word in PHISHING_WORDS:
        if word in url.lower():
            score += 10
            reasons.append(f"⚠️ يحتوي كلمة مشبوهة: {word}")

    # 5. فحص طول الرابط
    if len(url) > 100:
        score += 15
        reasons.append("⚠️ الرابط طويل جدا - ممكن يكون تمويه")

    # النتيجة
    print("\n--- النتيجة ---")
    for r in reasons:
        print(r)

    print(f"\n📊 درجة الخطورة: {score}/100")

    if score >= 50:
        print("🔴 خطير! لا تفتح هذا الرابط")
    elif score >= 20:
        print("🟡 مشبوه، انتبه قبل ما تفتحه")
    else:
        print("🟢 يبدو آمن نسبيا")

if __name__ == "__main__":
    url = input("ادخل الرابط اللي تبي تفحصه: ")
    check_url(url)
