import re
import getpass

def check_password(password):
    print("\n🔍 جاري فحص كلمة السر...")
    score = 0
    tips = []

    # الطول
    if len(password) >= 12:
        score += 30
        print("✅ الطول ممتاز (12+) +30")
    elif len(password) >= 8:
        score += 15
        print("⚠️ الطول مقبول (8+) +15")
        tips.append("خليها 12 حرف على الأقل")
    else:
        print("❌ قصيرة جدا! +0")
        tips.append("كلمة السر قصيرة مرة، زودها")

    # حروف كبيرة
    if re.search(r"[A-Z]", password):
        score += 15
        print("✅ فيها حرف كبير +15")
    else:
        tips.append("ضيف حرف كبير مثل A, B, C")

    # حروف صغيرة
    if re.search(r"[a-z]", password):
        score += 15
        print("✅ فيها حرف صغير +15")
    else:
        tips.append("ضيف حرف صغير")

    # أرقام
    if re.search(r"[0-9]", password):
        score += 15
        print("✅ فيها أرقام +15")
    else:
        tips.append("ضيف أرقام")

    # رموز
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 25
        print("✅ فيها رموز خاصة +25")
    else:
        tips.append("ضيف رمز مثل ! @ # $")

    # النتيجة
    print(f"\n📊 القوة: {score}/100")
    if score >= 80:
        print("🟢 قوية جدا! ممتازة يا هكر 💪")
    elif score >= 50:
        print("🟡 متوسطة، تحتاج تحسين")
    else:
        print("🔴 ضعيفة جدا! تتكسر بثواني!")

    if tips:
        print("\n💡 نصائح لتحسينها:")
        for t in tips:
            print(f"- {t}")

if __name__ == "__main__":
    pw = getpass.getpass("اكتب كلمة السر (ما بتظهر وانت تكتب - هذا أمان): ")
    check_password(pw)
