<div align="center">

# 🛡️ Secure Image Steganography Suite

**A robust, feature-rich desktop application for hiding secret messages within images using advanced steganography and strong AES-256 encryption.**

</div>

![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=for-the-badge)

---

## 🚀 Key Features

* **🔒 Strong Encryption** — Messages are secured with **AES-256 encryption** before being hidden. Passwords are processed using **PBKDF2 with 100,000 iterations** to resist brute-force attacks.  
* **🖼️ LSB Steganography** — Uses the Least Significant Bit (LSB) technique to invisibly embed data within image pixels.  
* **🎨 Modern GUI** — Built with Tkinter + ttkbootstrap, offering a sleek dark theme and two-column layout.  
* **📂 Drag & Drop** — Load images easily by dragging them into the application.  
* **📊 Real-Time Size Indicator** — Displays maximum capacity and live message size feedback.  
* **⚡ Optimized Performance** — Fast decoding even on large, high-resolution images.  
* **🌍 Cross-Platform** — Runs smoothly on Windows, macOS, and Linux.  

---

## 📸 Showcase

*(Replace placeholders with actual screenshots)*

| Encrypt Tab | Decrypt Tab (with Result) |
| :---: | :---: |
| *(Screenshot of Encrypt Tab)* | *(Screenshot of Decrypt Tab)* |

---

## 💻 Technologies Used

* **Language**: Python  
* **GUI**: Tkinter, ttkbootstrap, tkinterdnd2  
* **Core Logic**: OpenCV, NumPy  
* **Encryption**: Cryptography  

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
    ```bash
    git clone https://your-repo-url.git
    cd STEGANOGRAPHY
    ```

2. **Create a Virtual Environment** (recommended)
    ```bash
    python -m venv venv
    # Activate:
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 📖 How to Use

1. **Launch the App**
    ```bash
    python main.py
    ```

2. **Encrypting**
    * Open the **Encrypt** tab.  
    * Drag & drop an image (or browse manually).  
    * Enter your secret message + password.  
    * Save the new encrypted image (`.png`).  

3. **Decrypting**
    * Switch to the **Decrypt** tab.  
    * Load the encrypted image.  
    * Enter the correct password.  
    * Click **Decrypt & Reveal** to see the hidden message.  

---

## 📂 Project Structure

```plaintext
STEGANOGRAPHY/
├── main.py             # Entry point to run the application
├── requirements.txt    # Dependencies
│
└── app/
    ├── __init__.py     # Package initializer
    ├── core.py         # Core encryption & steganography logic
    └── gui.py          # Tkinter GUI code
```

---

<div align="center">
  <h3>Author</h3>
  <p>Crafted with ❤️ by <b>sh4dowkey</b></p>
  <a href="https://github.com/sh4dowkey">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</div>
