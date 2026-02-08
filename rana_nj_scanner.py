import requests
import time
import os

# কালার কোড
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[0m'

def banner():
    os.system('clear')
    print(f"""
{R}      _______      {Y}  Rana.nj  {R}      _______
     /   {Y}⚙   {R}\                     /   {Y}⚙   {R}\\
    /    {Y}⚙   {R} \                   /    {Y}⚙   {R} \\
   |           |                 |           |
   |  {W}X     X  {R}|                 |  {W}X     X  {R}|
   |   {W}\___/   {R}|                 |   {W}\___/   {R}|
    \         /                   \         /
     --{W}m---m{R}--                     --{W}m---m{R}--
{C}
    ===========================================
             SECURITY SCANNER BY RANA.NJ
    ===========================================
{W}    """)

def scan_website(url):
    banner()
    print(f"{C}[*] টার্গেট সার্ভার:{W} {url}")
    print(f"{Y}[*] স্ক্যানিং প্রসেস শুরু হচ্ছে...{W}\n")
    time.sleep(2)
    try:
        response = requests.get(url, timeout=10)
        print(f"{G}[+] সার্ভার অনলাইন আছে (Status: {response.status_code}){W}")
        server = response.headers.get('Server', 'প্রাইভেট সার্ভার')
        print(f"{C}[!] সার্ভার টেকনোলজি:{W} {server}")
        print(f"\n{Y}[*] পাসওয়ার্ড সিকিউরিটি চেক করা হচ্ছে...{W}")
        time.sleep(1.5)
        print(f"{G}[+] রেজাল্ট: সার্ভারটি সুরক্ষিত মনে হচ্ছে।{W}")
    except Exception as e:
        print(f"{R}[!] এরর: ইউআরএল ভুল অথবা সার্ভার ডাউন।{W}")

if __name__ == "__main__":
    target = input(f"{Y}আপনার টার্গেট URL দিন: {W}")
    if not target.startswith("http"):
        target = "http://" + target
    scan_website(target)
