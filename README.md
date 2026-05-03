# 🔍 Digital Forensics CLI Tool

## 📌 Overview
This is a Python-based command-line digital forensics tool designed to simulate real-world forensic investigation workflows. It analyzes file systems, detects suspicious activity, reconstructs timelines, and generates structured reports.

---

## 🚀 Features
- 📂 File system scanning & metadata extraction  
- ⚠️ Suspicious file detection (.exe, temp files, large files)  
- 🕵️ Timeline reconstruction of system activity  
- 📄 Automated PDF report generation  

---

## 🛠 Tech Stack
- Python  
- argparse  
- reportlab  
- tqdm  
- colorama  

---

## ▶️ Usage
```bash
python main.py --path sample_data --analyze --timeline --report
