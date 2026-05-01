# 🚀 ReconForge

**Fast Recon Tool — Subdomain Enumeration + Directory Scanner**

---

## ⚡ Overview

ReconForge is a lightweight reconnaissance tool designed for:

* Subdomain enumeration (passive + brute-force)
* DNS resolution
* HTTP probing
* Basic directory scanning

It is built for **speed and simplicity**, not full-scale fuzzing.

---

## 🔥 Features

* 🔍 Passive subdomain enumeration (crt.sh)
* 💣 Brute-force subdomain discovery
* 🌐 DNS resolution filtering
* ⚡ Fast HTTP probing
* 📂 Optional directory scanning (`--dir`)
* 🎯 Clean categorized output (WEB, API, AUTH, etc.)
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

You can run ReconForge like a real CLI tool:

```bash
chmod +x reconforge.py
cp reconforge.py ~/bin/reconforge
```

Then use:

```bash
reconforge target.com
```

---

## ⚠️ Limitations (Important)

### 📂 Directory Scanning

* Uses a **basic wordlist approach**
* Does **not perform advanced filtering**
* May produce **false positives** (especially on large platforms)

Example:

* Some endpoints may return `200 OK` even if not valid
* Platforms like Google/Microsoft often respond to many paths

👉 For accurate fuzzing, use dedicated tools like:

* ffuf
* dirsearch

---

### 🌐 Passive Enumeration

* Relies mainly on **crt.sh**
* If network issues occur, results may be limited

---

### ⚡ Not a Full Recon Framework

ReconForge is **not meant to replace** tools like:

* subfinder
* amass
* ffuf

It is designed as a **fast, simple recon utility**

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

## 👤 Author

GitHub: https://github.com/shhaheerr

---

## ⭐ Support

If you find this tool useful, consider giving it a ⭐

---

## 🚧 Future Improvements

* Better directory filtering (reduce false positives)
* More passive sources
* Async performance improvements
* Smarter categorization
