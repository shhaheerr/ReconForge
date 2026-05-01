# 🚀 ReconForge

**Version: v1.5**

Fast Recon Tool for **Subdomain Enumeration + Directory Scanning**

---

## ⚡ Overview

ReconForge is a lightweight reconnaissance tool designed for:

* Subdomain enumeration (passive + brute-force)
* DNS resolution
* HTTP probing
* Basic directory scanning

It focuses on **speed, simplicity, and clean output** rather than heavy automation.

---

## 🔥 Features

* 🔍 Passive subdomain enumeration (crt.sh)
* 💣 Brute-force subdomain discovery
* 🌐 DNS resolution filtering
* ⚡ Fast HTTP probing
* 📂 Optional directory scanning (`--dir`)
* 🎯 Categorized output (WEB, API, AUTH, SHOP, CDN)
* 🤫 Silent mode for scripting

---

## 🛠 Installation

### 1. Clone repository

```bash
git clone https://github.com/shhaheerr/ReconForge.git
cd ReconForge
```

### 2. Install dependencies

```bash
sudo apt install python3-colorama
pip3 install -r requirements.txt
```

---

## 🚀 Usage

### Basic scan

```bash
python3 reconforge.py target.com
```

---

### Silent mode (for automation)

```bash
python3 reconforge.py target.com --silent
```

---

### Save output

```bash
python3 reconforge.py target.com -o results.txt
```

---

### Thread control

```bash
python3 reconforge.py target.com --threads 50
```

---

### Directory scanning

```bash
python3 reconforge.py target.com --dir
```

---

### Scan IP / URL directly

```bash
python3 reconforge.py http://target-ip --dir
```

---

## 🖥 CLI Usage (Optional)

Run ReconForge like a real command:

```bash
chmod +x reconforge.py
cp reconforge.py ~/bin/reconforge
```

Then:

```bash
reconforge target.com
```

---

## ⚠️ Limitations

### 📂 Directory Scanning

* Uses **basic wordlist brute-force**
* May produce **false positives**
* Some servers return `200 OK` for all paths

👉 Example: Large platforms (Google, Microsoft) may respond to many paths even if they are not valid.

👉 For accurate fuzzing, use:

* ffuf
* dirsearch

---

### 🌐 Passive Enumeration

* Relies mainly on **crt.sh**
* Results may vary depending on network availability

---

### ⚡ Not a Full Recon Framework

ReconForge is **not intended to replace** advanced tools like:

* subfinder
* amass
* ffuf

It is designed as a **fast and simple recon utility**

---

## 📁 Project Structure

```
reconforge.py      → Main tool
passive.py         → Passive enumeration
brute.py           → Subdomain brute force
resolver.py        → DNS resolution
http_probe.py      → HTTP probing
dirscan.py         → Directory scanning
wordlist.txt       → Subdomain wordlist
dirs.txt           → Directory wordlist
```

---

## 🧪 Example Output

```
[WEB] admin.google.com
[API] api.google.com
[SHOP] store.google.com
```

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security testing only**.
The author is **not responsible for any misuse**.

---

## 👤 Author

GitHub: https://github.com/shhaheerr

---

## ⭐ Support

If you find this tool useful, consider giving it a ⭐

---

## 🚧 Future Improvements

* Reduce directory scan false positives
* Add more passive sources
* Improve performance (async scanning)
* Smarter filtering and categorization
