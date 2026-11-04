from flask import Flask
import os, glob

app = Flask(__name__)

@app.route('/')
def home():
    logs = ""
    try:
        if os.path.exists("access.log"):
            with open("access.log") as f:
                logs = "<br>".join(f.read().splitlines()[-10:])
    except: pass

    files = "<br>".join(os.listdir("."))

    return f"""
    <html dir="rtl" style="font-family:sans-serif;background:#0f172a;color:white;padding:20px">
    <h1>🛡️ SOC Dashboard - مركز العمليات الأمنية</h1>
    <p>أهلاً بك يا مبرمج - نظامك شغال لايف</p>
    <div style="display:flex;gap:10px">
      <div style="background:#1e293b;padding:15px;border-radius:10px;flex:1"><h3>🟢 السيرفر</h3><p>شغال - Online</p></div>
      <div style="background:#1e293b;padding:15px;border-radius:10px;flex:1"><h3>⚠️ تنبيهات</h3><p>3 تنبيهات جديدة</p></div>
      <div style="background:#1e293b;padding:15px;border-radius:10px;flex:1"><h3>📁 الملفات</h3><p>{len(os.listdir("."))} ملف</p></div>
    </div>
    <h2>📋 آخر السجلات - access.log</h2>
    <div style="background:black;padding:15px;border-radius:10px;direction:ltr">{logs or "لا توجد سجلات بعد"}</div>
    <h2>🛠️ أدواتك</h2>
    <p>dashboard.py | monitor.py | port_scanner.py | log_analyzer.py | phishing_detector.py</p>
    <br><a href="https://github.com" style="color:#38bdf8">GitHub حقي</a>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
