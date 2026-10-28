from flask import Flask, request
import time
from collections import defaultdict

app = Flask(__name__)

# ذاكرة الهجمات
requests_log = defaultdict(list)
blocked_ips = set()
BLOCK_TIME = 60  # حظر لمدة 60 ثانية

def is_blocked(ip):
    return ip in blocked_ips

def check_limit(ip, endpoint, limit, window=60):
    now = time.time()
    requests_log[(ip, endpoint)] = [t for t in requests_log[(ip, endpoint)] if now - t < window]
    requests_log[(ip, endpoint)].append(now)
    if len(requests_log[(ip, endpoint)]) > limit:
        blocked_ips.add(ip)
        print(f"🚫 BLOCKED IP: {ip} - تم حظره تلقائياً!")
        return True
    return False

@app.before_request
def block_check():
    ip = request.remote_addr
    if is_blocked(ip):
        return "🚫 You are BLOCKED by SOC", 403

@app.route('/login', methods=['POST'])
def login():
    ip = request.remote_addr
    if check_limit(ip, '/login', 5):
        return "Too many attempts - BLOCKED", 429
    with open("access.log", "a") as f:
        f.write(f"{ip} /login 200 {time.time()}\n")
    return "Login OK", 200

@app.route('/register', methods=['POST'])
def register():
    ip = request.remote_addr
    if check_limit(ip, '/register', 3):
        return "Too many attempts - BLOCKED", 429
    with open("access.log", "a") as f:
        f.write(f"{ip} /register 200 {time.time()}\n")
    return "Register OK", 200

@app.route('/unblock')
def unblock():
    blocked_ips.clear()
    requests_log.clear()
    return "All IPs Unblocked ✅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
