# CrackMate

[![License: MIT](https://img.shields.io/github/license/0xHawkEye/CrackMate?cacheSeconds=60)](https://github.com/0xHawkEye/CrackMate/blob/main/LICENSE)
![Issues](https://img.shields.io/github/issues/0xHawkEye/CrackMate?cacheSeconds=60)
![Forks](https://img.shields.io/github/forks/0xHawkEye/CrackMate?cacheSeconds=60)
![Stars](https://img.shields.io/github/stars/0xHawkEye/CrackMate?cacheSeconds=60)
![Last Commit](https://img.shields.io/github/last-commit/0xHawkEye/CrackMate?cacheSeconds=60)
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Crack Mate is a high-speed hash cracking tool written in Python that uses a dictionary attack to uncover plain text passwords from hashed values. It supports multiple algorithms including **MD5**, **SHA1**, **SHA256**, and more. Ideal for CTFs, pentesters, and ethical hackers.

---

## 🚀 Features

- ✅ Supports all major hash algorithms (MD5, SHA1, SHA256, etc.)
- 🧠 Fast multithreaded execution
- 🧰 Custom wordlist support
- 📜 Clean banner and colorful output with `huepy` and `pyfiglet`
- ⚡ Prints cracking duration

---
## 🧑‍💻 Installation

### 1. **Clone the Repository**

To get started with **CrackMate**, clone this repository to your local machine:

```bash
git clone https://github.com/0xHawkEye/CrackMate.git
cd CrackMate
```
### 2. **Install Dependencies**

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
---
## 📄 Usage

### Running the Script
To run DirRaptor, use the following command:
```bash
python CrackMate.py -hs <Hash> -a <Encoding> -w <wordlist>
```

### Arguments:
```bash
-h, --help            show this help message and exit
-hs, --hash HASH      Hash value to crack
-a, --algorithm ALGORITHM
                        Hash algorithm (e.g., md5, sha1)
-w, --wordlist WORDLIST
                        Path to the wordlist file
                        Default: rockyou1.txt
-all                  Print all available hash algorithms
````
---

### Example Command:
```bash
python CrackMate.py -hs 5ebddb1d6c422cd74b696e3a0e674c91 -a md5 -w rockyou1.txt
```
---
## **⚖️ Legal Considerations**
**CrackMate** is intended for educational and authorized penetration testing purposes only.

By using this tool, you agree to the following:

✅ You must not use **Crack Mate** to crack or reverse-engineer hashes belonging to any user, system, or organization without explicit authorization from the rightful owner.

✅ You are solely responsible for any misuse or unauthorized activity performed using this tool.

✅ The developer is not liable for any damage, legal consequences, or misuse resulting from the use of this tool.

>❗ Crack Mate is intended for educational and authorized security research purposes only.
Do not use this tool on systems without explicit permission. Unauthorized cracking is illegal under most cybercrime laws (e.g., CFAA, IT Act).

>This tool is intended for educational and authorized testing purposes only.

---
## **📄 License**
This project is licensed under the MIT License.

---
## **🛡️ Ethical Usage**
- Use in lab environments, CTFs, bug bounty, or client-approved pentests.
- Respect all terms of service and network usage policies.
---
## **🤝 Contributing**
Contributions are welcome! Feel free to submit pull requests or open issues to enhance the tool. Your feedback and contributions help improve DirRaptor.

---

## **🙌 Credits**

    Developed by: Ayush Kumar
    Linkedin: https://www.linkedin.com/in/ayushkr4422 

---


