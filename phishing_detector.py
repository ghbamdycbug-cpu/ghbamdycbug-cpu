import re
from urllib.parse import urlparse

LEGIT = ["google.com", "facebook.com", "instagram.com", "paypal.com", "amazon.com", "microsoft.com", "apple.com", "yahoo.com", "twitter.com", "github.com", "netflix.com"]

def normalize(domain):
    # نحول الحروف المزورة لحروف حقيقية عشان نكشف التقليد
    # 0 -> o , 1 -> l , 3 -> e , 5 -> s , @ -> a , rn -> m
    d = domain.lower()
    d = d.replace("0", "o").replace("1", "l").replace("3", "e").replace("5", "s").replace("@", "a")
    d = d.replace("rn", "m")
    return d

def check_url(url):
    print(f"\n[+] Checking: {url}")
    print("-" * 50)
    score = 0
    reasons = []

    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    full = url.lower()

    # 1. No HTTPS
    if not url.startswith("https"):
        score += 10
        reasons.append("No HTTPS - Not Secure")

    # 2. IP instead of domain
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        score += 30
        reasons.append("Uses IP instead of domain!")

    # 3. @ in URL
    if "@" in url:
        score += 20
        reasons.append("Has @ in URL - phishing trick!")

    # 4. Suspicious keywords
    keywords = ["login", "secure", "account", "update", "verify", "free"]
    found = [k for k in keywords if k in full]
    if found:
        score += 10
        reasons.append(f"Suspicious keywords: {', '.join(found)}")

    # 5. TYPO-SQUATTING - هذا هو الإصلاح الجديد
    clean = normalize(domain)
    # شيل www. عشان المقارنة
    clean_no_www = clean.replace("www.", "")
    domain_no_www = domain.replace("www.", "")

    for legit in LEGIT:
        # اذا بعد التنظيف صار يساوي موقع حقيقي، بس الأصلي مختلف = مزور
        if clean_no_www == legit and domain_no_www != legit:
            score += 50
            reasons.append(f"TYPO-SQUATTING! Looks like {legit} but is {domain}")
            break
        # اذا فيه اسم موقع حقيقي داخل دومين غريب
        elif legit.split('.')[0] in domain_no_www and domain_no_www != legit and clean_no_www != legit:
            # مثال: facebook-login.com
            if domain_no_www != legit:
                score += 20
                reasons.append(f"Contains brand name {legit} in fake domain")
                break

    # 6. Long URL
    if len(url) > 75:
        score += 10
        reasons.append("Very long URL")

    print(f"Risk Score: {score}/100")
    print(f"\n[!] Reasons:")
    if not reasons:
        print(" - No issues found")
    else:
        for r in reasons:
            print(f" - {r}")

    print("-" * 50)
    if score >= 40:
        print("[RESULT]: 🔴 PHISHING! DO NOT CLICK!")
    elif score >= 20:
        print("[RESULT]: 🟠 SUSPICIOUS - Be Careful!")
    else:
        print("[RESULT]: 🟢 SAFE - Looks Legit")
    print("-" * 50)

print("="*50)
print("🎣 Phishing URL Detector - SOC Analyst Project 4")
print("="*50)

# تجارب جاهزة
tests = [
    "https://www.paypa1.com/secure/login/update/account",
    "faceb00k.com",
    "https://google.com",
    "https://faceb00k.com/login",
    "http://192.168.1.1/login@paypal.com",
    "https://amazon-secure-login.com"
]

for t in tests:
    check_url(t)

print("\nTry your own URL:")
while True:
    u = input("Enter URL to check (or Enter to skip): ")
    if u.strip() == "":
        break
    check_url(u)

print("Done! Bye 👋")
