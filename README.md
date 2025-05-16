# 🚀 NetRecon — The Ultimate Network Reconnaissance Toolkit

NetRecon is a **powerful**, **modular**, and **extensible** Python toolkit designed for comprehensive network reconnaissance.  
Whether you're a cybersecurity professional, pentester, or just a network enthusiast, NetRecon equips you with essential tools to gather actionable insights — all from a single, elegant CLI interface.

---

## ⚙️ Features

- 🔍 **TCP Port Scanner**  
  Fast, multithreaded scanning of TCP ports with service detection for hundreds of known ports.

- 📡 **Packet Sniffer**  
  Capture and analyze live network traffic effortlessly with flexible interface options.

- 🌍 **GeoIP Lookup**  
  Map IP addresses to countries and regions instantly.

- 📇 **WHOIS Lookup**  
  Query domain registration info from authoritative WHOIS servers, with cleaned, easy-to-read output.

---

## 🚀 Quick Start

Run any command from your terminal:

```bash
python netrecon.py scan --ip 192.168.1.1 --ports 1-1000
python netrecon.py sniff --iface eth0
python netrecon.py geoip --ip 8.8.8.8
python netrecon.py whois --target example.com
````

---

## 🛠 Installation

Make sure you have Python 3.8+ installed.
Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Legal & Ethical Use Warning

**NetRecon is intended strictly for authorized security testing and educational purposes.**

Unauthorized network scanning, sniffing, or information gathering on systems you do not own or have explicit permission to test **may be illegal** and subject to civil or criminal penalties.

Always obtain proper consent before using this tool, and respect privacy and laws applicable in your jurisdiction.

---

## 🤝 Contributing

Open source and community-driven.
Feel free to submit issues, feature requests, or pull requests — every contribution helps make NetRecon better!

---

Made with passion by security enthusiasts 🔐