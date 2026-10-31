# Phishing URL Detector - SOC Analyst Project 4
# Detects fake / malicious URLs

import re
from urllib.parse import urlparse

def check_url(url):
    print(f"\n[+] Checking: {url}")
    print("-" * 50)
    score = 0
    reasons = []

    # Add http if missing
    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc
    full = url.lower()

    # 1. Check IP instead of domain
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        score += 30
        reasons.append("Uses IP address instead of domain name")

    # 2. Check @ symbol trick
    if "@" in url:
        score += 25
        reasons.append("Contains @ - hides real domain")

    # 3. Check too long URL
    if len(url) > 75:
        score += 15
        reasons.append(f"Very long URL ({len(url)} chars)")

    # 4. Check many subdomains
    if domain.count(".") > 3:
        score += 20
        reasons.append(f"Too many subdomains ({domain.count('.')})")

    # 5. Check no HTTPS
    if not full.startswith("https"):
        score += 10
        reasons.append("No HTTPS - Not Secure")

    # 6. Check suspicious keywords
    keywords = ["login", "verify", "secure", "account", "update", "free", "win", "bank"]
    found = [k for k in keywords if k in full]
    if found:
        score += 15
        reasons.append(f"Suspicious keywords: {', '.join(found)}")

    # 7. Check URL shortener
    shorteners = ["bit.ly", "tinyurl", "t.co", "goo.gl"]
    if any(s in domain for s in shorteners):
        score += 20
        reasons.append("Uses URL shortener - hides destination")

    # 8. Check typo squatting (fake google etc)
    fakes = {"goggle": "google", "facebok": "facebook", "amazom": "amazon", "paypa1": "paypal"}
    for fake, real in fakes.items():
        if fake in domain:
            score += 40
            reasons.append(f"TYPO-SQUATTING! Looks like {real} but is {fake}")

    # Result
    print(f"Risk Score: {score}/100")
    print("\n[!] Reasons:")
    if reasons:
        for r in reasons:
            print(f"  - {r}")
    else:
        print("  - No suspicious signs found")

    print("\n[RESULT]: ", end="")
    if score >= 50:
        print("🔴 PHISHING! DO NOT CLICK!")
    elif score >= 25:
        print("🟡 SUSPICIOUS - Be Careful!")
    else:
        print("🟢 SAFE - Looks Legit")
    print("-" * 50)

print("=" * 50)
print("🎣 PHISHING URL DETECTOR")
print("=" * 50)

tests = [
    "https://www.google.com",
    "http://192.168.1.1/login/verify-account-secure-free-win",
    "http://google.com@evil.com/login",
    "https://www.goggle.com/login",
    "http://bit.ly/3xYz123",
    "https://www.paypa1.com/secure/login/update/account",
]

for u in tests:
    check_url(u)

print("\nTry your own URL:")
user_url = input("Enter URL to check (or Enter to skip): ")
if user_url.strip():
    check_url(user_url.strip())
