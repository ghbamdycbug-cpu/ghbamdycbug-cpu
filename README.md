# 🛡️ SOC Monitor v2.0 - Real-Time Attack Detection

A Python-based Security Operations Center (SOC) monitor that detects web attacks in real-time from Apache logs.

## 🚀 Features
- **SQL Injection Detection** - Detects `' OR 1=1`, `UNION SELECT`, etc.
- **XSS Detection** - Detects `<script>`, `alert()`, etc.
- **Brute Force Detection** - Detects 5+ requests from same IP in 10 seconds
- **Auto Incident Report** - Saves all attacks to `incident_report.txt` with timestamp

## 🛠️ How to Run
```bash
python3 monitor.py
## 📝 Example Output
[ALERT] SQL Injection from 192.168.1.100
[ALERT] XSS Attack from 192.168.1.100
[ALERT] BRUTE FORCE from 10.0.0.5 - 6 requests

## 👨‍💻 Author
Built by ghbamdycbug-cpu as part of Cybersecurity Learning Journey
