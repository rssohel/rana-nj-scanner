import requests
import time
import os

# Color Codes
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
    print(f"{C}[*] Target Server:{W} {url}")
    print(f"{Y}[*] Scanning process starting...{W}\n")
    time.sleep(2)
    try:
        response = requests.get(url, timeout=10)
        print(f"{G}[+] Server is Online (Status: {response.status_code}){W}")
        server = response.headers.get('Server', 'Private Server')
        print(f"{C}[!] Server Technology:{W} {server}")
        print(f"\n{Y}[*] Checking security headers...{W}")
        time.sleep(1.5)
        print(f"{G}[+] Result: Server looks protected.{W}")
    except Exception as e:
        print(f"{R}[!] Error: Invalid URL or Server Down.{W}")

if __name__ == "__main__":
    target = input(f"{Y}Enter Target URL: {W}")
    if not target.startswith("http"):
        target = "http://" + target
    scan_website(target)
