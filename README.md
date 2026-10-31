# 🛡️ SOC Project - Cybersecurity Portfolio
### By ghbamdycbug-cpu

Welcome to my cybersecurity lab! Here I build real security tools using Python.

---

## 📁 Projects

### 1. 🔍 SOC Monitor - `monitor.py`
Real-time security monitoring system.
- Detects Brute Force attacks
- Detects Port Scanning
- Detects Suspicious IPs
- Sends alerts with severity levels

**Run:** `python3 monitor.py`

### 2. 🌐 Port Scanner - `port_scanner.py`
Fast port scanner like Nmap, built from scratch!
- Scans 10 common ports (SSH, HTTP, FTP, etc.)
- Detects open ports and services
- Warns about SSH Brute Force risk
- Shows target IP resolution

**Run:** `python3 port_scanner.py`

### 3. 🔐 Password Checker - COMING SOON...

---

## 🛠️ Skills Used
- Python 3
- Socket Programming
- Network Security
- Threat Detection
- Git & GitHub

---

## 👨‍💻 Author
**ghbamdycbug-cpu** - Aspiring SOC Analyst / Penetration Tester

### 3. 🔐 Password Strength Checker
**File:** `password_checker.py`
Checks password strength and crack time.
- Scores 0 to 85
- Detects leaked passwords like 123456
- Estimates crack time

**Example:**
- 123456 -> 0/85, 0.00 seconds
- MyPass@2026!Strong -> 85/85, 10 Quintillion years

**Run:**
```bash
python3 password_checker.py
