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

## ▶️ How to Run

**✅ GUI Mode**

 ```bash
python password_tool.py

```
* A user-friendly window will open.

* Enter your password to check its strength.

* Click “Generate Wordlist” to create a personalized wordlist.

**✅ CLI Mode**
```bash
python password_tool.py --password "Rubal@123"
```

With wordlist:

```bash
python password_tool.py --password "Rubal@123" --wordlist "rubal,jaipur,2025" --output wordlist.txt
```
---
## 🧠 Password Strength Logic

This tool uses two methods to analyze passwords:

**1. Entropy-Based Calculation**

* Estimates password unpredictability.

* Formula:
  
  `entropy = length × log₂(character set size)`

**2. zxcvbn Library (by Dropbox)**

* Evaluates password strength on a scale of 0–4.

* Estimates crack time for brute-force attacks.

**🔍 Additional Heuristics**

* Detects missing digits, symbols, cases, and length.
  
* Gives real-time suggestions.
---

## 📦 Output

**🖥 GUI Output**

* Strength Meter: Color-coded bar (Red → Green).

* Crack Time: Estimated offline brute-force time.

* Feedback: Recommendations to strengthen password.

* Wordlist Export: Save generated words to `.txt`


**🖥 CLI Output**

* Printed entropy, zxcvbn score, and crack time.

* Saved wordlist file (if --output is used).


## 🧾 Example Output

```txt
Analyzing password: Rubal@123

Entropy: 54.44

zxcvbn score: 3/4

Crack Time (offline fast hash): 2 hours
```
---
## Recommendations:

- Add more unique characters.
  
- Avoid common patterns like "123".

---

## 📂 Example Wordlist Entries:

If inputs were:  `rubal, jaipur, 2025`

```
rubal

Rubal

RUBAL

rubal2025

2025rubal

rubaljaipur

jaipurrubal

rubal!

@rubal

rubal_123

rubal1995

rubal@jaipur
```
| Wordlist includes leet variants, case variations, year combinations, and special symbols.

---

## 📋 Requirements

Install dependencies using:

```
pip install zxcvbn
```

## 💡 Author
**Rubal Choudhary**



