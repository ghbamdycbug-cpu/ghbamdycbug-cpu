# 🛡️ SOC-Project - Cyber Security Tools

My personal SOC Analyst toolkit - Built from scratch on Termux (Android)!

## 🚀 Tools (6 Tools)

| # | Tool | What it does |
|---|------|--------------|
| 1 | `log_analyzer.py` | Detects brute-force attacks from logs |
| 2 | `port_scanner.py` | Scans open ports on a target |
| 3 | `password_checker.py` | Checks password strength + HaveIBeenPwned |
| 4 | `hash_cracker.py` | Cracks MD5 hashes with wordlist |
| 5 | `phishing_detector.py` | Detects phishing URLs (IP, @, typo-squatting) |
| 6 | `wifi_scanner.py` | Scans WiFi network for connected devices |

## 🔥 Featured Fix

**Found & Fixed a Bug Myself:**
- Before: `faceb00k.com` was detected as `SAFE (10/100)`
- After: `faceb00k.com` detected as `PHISHING (60/100)` - TYPO-SQUATTING!

## 🛠️ How to Run
```bash
python log_analyzer.py
python port_scanner.py
python phishing_detector.py
python wifi_scanner.py
