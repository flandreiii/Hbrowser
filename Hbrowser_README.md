<div align="center">

```
██╗  ██╗██████╗ ██████╗  ██████╗ ██╗    ██╗███████╗███████╗██████╗
██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔════╝██╔══██╗
███████║██████╔╝██████╔╝██║   ██║██║ █╗ ██║███████╗█████╗  ██████╔╝
██╔══██║██╔══██╗██╔══██╗██║   ██║██║███╗██║╚════██║██╔══╝  ██╔══██╗
██║  ██║██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝███████║███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
```

**A terminal-based browser for security research and hacking tools in Termux**  
*Python · Terminal · Android · Lightweight*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-black?style=flat-square&logo=android)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Author](https://img.shields.io/badge/Author-flandreiii-cyan?style=flat-square)
![Type](https://img.shields.io/badge/Type-Terminal%20Browser-red?style=flat-square)

</div>

---

## 🌐 What is Hbrowser?

**Hbrowser** is a lightweight terminal-based browser built for **Termux** on Android. Designed for security researchers and hacking enthusiasts, it lets you browse and interact with web content directly from your terminal — no GUI, no graphical browser, just raw terminal power.

Whether you're doing recon, testing URLs, or just prefer staying in the terminal, Hbrowser keeps you in your element.

---

## ✨ Features

- 🌍 **Browse the web from your terminal** — no graphical browser needed
- 🔍 **Security-focused** — built for pentesters and researchers
- 📱 **Termux native** — runs perfectly on Android via Termux
- ⚡ **Lightweight** — minimal footprint, launches instantly
- 🐍 **Pure Python** — easy to read, modify and extend
- 🖥️ **Works on Linux too** — not just Android

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| **Python** | 3.x |
| **App** | [Termux](https://f-droid.org/packages/com.termux/) from F-Droid |

> ⚠️ **Install Termux from F-Droid**, not from the Play Store. The Play Store version is outdated.

---

## 🚀 Installation

### Termux (Android)

```bash
# Step 1 — Update and install dependencies
pkg update && pkg upgrade
pkg install python git

# Step 2 — Clone the repo
git clone https://github.com/flandreiii/Hbrowser.git
cd Hbrowser

# Step 3 — Run it
python hbrowser.py
```

### Linux

```bash
# Step 1 — Make sure Python and Git are installed
sudo apt install python3 git    # Debian / Ubuntu
# or
sudo pacman -S python git       # Arch

# Step 2 — Clone the repo
git clone https://github.com/flandreiii/Hbrowser.git
cd Hbrowser

# Step 3 — Run it
python3 hbrowser.py
```

---

## 🛠️ Usage

```bash
python hbrowser.py
```

Type a URL or command into the terminal prompt and navigate from there. Everything runs inside your shell — no windows, no tabs, just text.

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `python: command not found` | Run `pkg install python` in Termux, or `sudo apt install python3` on Linux |
| `git: command not found` | Run `pkg install git` in Termux |
| Connection errors | Make sure your device has an active internet connection |
| Termux crashes on launch | Reinstall Termux from **F-Droid**, not the Play Store |
| Script won't run on Linux | Try `python3 hbrowser.py` instead of `python` |

---

## 📁 Project Structure

```
Hbrowser/
├── hbrowser.py    # Main browser script
├── .gitignore     # Git ignore rules
└── README.md      # This file
```

---

## 🤝 Contributing

Contributions and ideas are always welcome!  
Feel free to open an issue or submit a pull request.

Ideas for future features:
- [ ] URL history log
- [ ] Bookmark system
- [ ] HTTP header inspector
- [ ] Basic HTML source viewer
- [ ] Cookie and session display
- [ ] Proxy support

---

## ⚠️ Disclaimer

Hbrowser is intended for **educational purposes** and for use on systems you own or have explicit permission to test. Do not use this tool for unauthorized access to any network or system. The author is not responsible for any misuse.

---

## 📜 License

```
MIT License

Copyright (c) 2026 flandreiii

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

**Made by [flandreiii](https://github.com/flandreiii)**

*Hbrowser — the web, from your terminal 🌐*

</div>
