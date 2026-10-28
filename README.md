# 🛡️ Mini SOC Project - Built on Termux (Android)

Built a Flask server with Rate-Limiting protection, implemented a real-time log analyzer to detect Brute Force attacks, a live SOC monitor, and a dashboard. Successfully simulated and detected an attack from 127.0.0.1 with 42% blocked requests (429) + Auto-Block system (403).

## Features
- Flask Server with Rate Limiting
- Auto-Block IP after Brute Force (403)
- Real-time Monitor with Alerts
- SOC Dashboard & Incident Report
- Brute Force Detection

## Files
- app.py - Server + Protection
- monitor.py - Live Monitor
- log_filter.py - Analyzer
- dashboard.py - Dashboard

## Demo
Attack: `for i in 1..8; do curl -X POST /login; done`
Result: 5x Login OK -> 1x 429 BLOCKED -> 2x 403 You are BLOCKED by SOC
