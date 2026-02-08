# 💀 Rana.nj Security Scanner Pro

A powerful and lightweight website security auditing tool specially designed for **Termux** and **Linux** environments. Created by **Rana.nj**.

## ⚙️ Features
* **Custom Interface:** Unique Skull & Gear ASCII art with the branding of **Rana.nj**.
* **Color-Coded Feedback:** Professional output using Red (Danger), Green (Safe), and Cyan (Info) colors.
* **Server Information:** Identifies the target server's technology and status codes.
* **Security Auditor:** Checks for missing security headers and common weak password configurations.

## 🚀 Installation & Usage

Copy and paste the following commands into your Termux terminal:

```bash
# Update system and install dependencies
pkg update && pkg upgrade -y
pkg install python git -y
pip install requests

# Clone the repository
git clone [https://github.com/Your-Username/rana-nj-scanner](https://github.com/Your-Username/rana-nj-scanner)

# Navigate to the directory
cd rana-nj-scanner

# Run the scanner
python rana_nj_scanner.py
