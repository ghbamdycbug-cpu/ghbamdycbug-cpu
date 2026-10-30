# 🛡️ SOC Project - Security Operations Center

A mini SOC (Security Operations Center) built in Python to monitor logs, detect suspicious activity, and generate incident reports. Built for learning Blue Team / SOC Analyst skills.

## 🚀 Features

- **Real-time Log Monitoring** - Monitor `access.log` continuously
- **Suspicious IP Detection** - Detect brute-force, scanning & anomalies
- **Log Filtering** - Filter logs by IP, status code, and time
- **Web Dashboard** - Visualize threats with `dashboard.py` + `index.html`
- **Incident Reporting** - Auto-generate `incident_report.txt`

## 📁 Project Structure

| File | Description |
| --- | --- |
| `monitor.py` | Main monitoring engine |
| `log_filter.py` | Filter and parse logs |
| `app.py` | Web application entry point |
| `dashboard.py` | Dashboard logic & stats |
| `index.html` | Frontend dashboard UI |
| `access.log` | Sample web server logs |
| `incident_report.txt` | Example incident report |

## 🛠️ Installation

```bash
git clone https://github.com/ghbamdycbug-cpu/soc-project.git
cd soc-project
pip install flask
