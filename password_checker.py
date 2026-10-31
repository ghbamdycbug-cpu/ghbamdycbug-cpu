import re
import string
import time

print("="*50)
print("🔐 PASSWORD STRENGTH CHECKER v1.0")
print("="*50)

password = input("\nEnter password to check: ")

score = 0
feedback = []

# 1. Length check
if len(password) >= 12:
    score += 25
    feedback.append("✅ Length 12+ : Excellent!")
elif len(password) >= 8:
    score += 15
    feedback.append("⚠️ Length 8-11 : OK, but make it 12+")
else:
    feedback.append("❌ Too short! Use 12+ characters")

# 2. Uppercase
if re.search(r'[A-Z]', password):
    score += 15
    feedback.append("✅ Has UPPERCASE letters")
else:
    feedback.append("❌ Add UPPERCASE letters (A-Z)")

# 3. Lowercase
if re.search(r'[a-z]', password):
    score += 15
    feedback.append("✅ Has lowercase letters")
else:
    feedback.append("❌ Add lowercase letters (a-z)")

# 4. Numbers
if re.search(r'[0-9]', password):
    score += 15
    feedback.append("✅ Has numbers")
else:
    feedback.append("❌ Add numbers (0-9)")

# 5. Special chars
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    score += 15
    feedback.append("✅ Has special characters (!@#...)")
else:
    feedback.append("❌ Add special characters (!@#$%)")

# 6. Common passwords check
common = ["123456", "password", "123456789", "qwerty", "admin", "12345", "letmein"]
if password.lower() in common:
    score = 0
    feedback.append("🚨 DANGER: This is in TOP leaked passwords list!")

# 7. Estimate crack time
charset = 0
if re.search(r'[a-z]', password): charset += 26
if re.search(r'[A-Z]', password): charset += 26
if re.search(r'[0-9]', password): charset += 10
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32

if charset > 0:
    combinations = charset ** len(password)
    # Hacker tries 1 Billion per second
    seconds = combinations / 1000000000
    if seconds < 60:
        crack_time = f"{seconds:.2f} seconds"
    elif seconds < 3600:
        crack_time = f"{seconds/60:.1f} minutes"
    elif seconds < 86400:
        crack_time = f"{seconds/3600:.1f} hours"
    elif seconds < 31536000:
        crack_time = f"{seconds/86400:.1f} days"
    else:
        crack_time = f"{seconds/31536000:.1f} years"
else:
    crack_time = "Instantly"

print("\n" + "-"*50)
for f in feedback:
    print(f)

print("\n" + "="*50)
print(f"🎯 SCORE: {score}/85")
if score >= 80:
    print("🟢 VERY STRONG - Hacker proof!")
elif score >= 60:
    print("🟡 GOOD - But can be stronger")
elif score >= 30:
    print("🟠 WEAK - Easy to crack!")
else:
    print("🔴 VERY WEAK - Change it NOW!")

print(f"⏱️  Time to crack (1B tries/sec): {crack_time}")
print("="*50)
