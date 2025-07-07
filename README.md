# 🔐 Password Strength Analyzer & Wordlist Generator

A lightweight Python tool designed to:

- 🛡️ **Analyze password strength quickly**
- 📝 **Generate customized wordlists** using personal information (name, pet name, date)
- ⚡ **Run out-of-the-box on Kali Linux** and other Linux distributions without any extra dependencies

Whether you are a penetration tester, security researcher, or just want to improve your own password hygiene, this script can help you **understand password complexity** and build **targeted wordlists for testing**.

---

## 📁 File Name

password_tool.py



---

## ✨ Features

✅ **Simple Password Strength Classification**  
- Classifies passwords as **Strong**, **Medium**, or **Weak** using basic rules:
  - Length
  - Use of uppercase and lowercase letters
  - Inclusion of digits and special characters

✅ **Leetspeak Transformations**  
- Automatically creates common leetspeak variants (e.g., `tommy` ➡️ `t0mmy`, `leet` ➡️ `l33t`).

✅ **Year-Based Combinations**  
- Generates combinations with years like `2024`, `2004`, `1234` (for commonly used patterns).

✅ **Custom Wordlist Generation**  
- Combines all variations into a single file (`simple_wordlist.txt`).

✅ **Zero External Libraries**  
- No pip installs needed—runs directly with **Python 3**.

✅ **Fast and Lightweight**  
- Can generate dozens of combinations instantly.

---

## 💻 How to Run

**1️⃣ Clone or Download the Script**

    ```bash
    
    git clone https://github.com/yourusername/password-analyzer.git
    cd password-analyzer
    (Or download the .py file directly)



**2️⃣ Run with your parameters**


python3 password_tool.py \
  --password "Heenal@123" \
  --name "Heenal" \
  --date "22June2004" \
  --pet "Tommy"
🧠 Password Strength Logic
Strength	Criteria
Strong	8+ characters, at least 1 uppercase, 1 lowercase, 1 digit, and 1 symbol
Medium	8+ characters, but missing some complexity
Weak	Less than 8 characters or lacking variety

📂 Example Wordlist Entries
python-repl
!@#RUB4L
!@#RUB@L
!@#RUBaL
!RUB4L
!RUB@L
!RUBaL
#RUB4L
#RUB@L
#RUBaL
123RUB4L
123RUB@L
123RUBaL
12RUB4L
12RUB@L
12RUBaL
1RUB4L


...
Wordlist file: simple_wordlist.txt

Total entries: Varies depending on your inputs (typically 30–50)

🖼️ Example Output

Password Strength: Strong
Wordlist saved to simple_wordlist.txt with 38 entries.
(Optional: Insert a screenshot here)

🔧 Advanced Usage
You can omit some parameters if desired:

Only check password strength:

python3 password_tool.py --password "MySecret!"
Only generate wordlist:


python3 password_tool.py --name "Alice" --date "14Feb1990"
🛠 Requirements
Python 3.x

Runs on:

Kali Linux

Ubuntu/Debian

MacOS

Windows (using python instead of python3)

No additional packages required.

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

✍️ Author
Rubal Chouhdary
🖥️ Security Researcher | Python Developer
🔗 Kali Linux Enthusiast

