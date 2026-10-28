from collections import Counter
print("="*40)
print("   🛡️  SOC DASHBOARD - لوحة التحكم")
print("="*40)
try:
    lines = open("access.log").readlines()
    total = len(lines)
    ok = sum(1 for l in lines if " 200 " in l)
    blocked = sum(1 for l in lines if " 429 " in l)
    ips = Counter(l.split()[0] for l in lines)
    endpoints = Counter(l.split()[1] for l in lines if len(l.split())>1)

    print(f"إجمالي الطلبات: {total}")
    print(f"✅ مسموح (200): {ok}")
    print(f"🚨 محظور (429): {blocked}")
    print(f"نسبة الهجوم: {blocked*100//total if total else 0}%")
    print("-"*40)
    print("أخطر IP:")
    for ip, c in ips.most_common(3):
        print(f"  {ip} -> {c} طلب")
    print("-"*40)
    print("أكثر مسار مستهدف:")
    for ep, c in endpoints.most_common(3):
        print(f"  {ep} -> {c} مرة")
    print("="*40)
    if blocked > 10:
        print("الحالة: 🔴 تحت هجوم Brute Force")
    elif blocked > 0:
        print("الحالة: 🟡 محاولات مشبوهة")
    else:
        print("الحالة: 🟢 آمن")
except FileNotFoundError:
    print("لا يوجد access.log بعد")
