<div align="center">

# 🛡️ Secure Image Steganography

**A Python-based desktop application to securely hide password-protected messages inside images using steganography.**

</div>

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)

---

## Overview

This project provides a user-friendly tool for **image steganography**, allowing you to embed secret messages within images without any noticeable changes to the picture. To ensure the confidentiality of your hidden data, all messages are **encrypted** and can only be decrypted with the correct password, making it a secure way to share information.

## 🚀 Key Features

* **🔒 Password-Protected Encryption**: Ensures that only authorized users with the correct password can decode the hidden messages.
* **🎨 Intuitive GUI**: A clean and simple graphical interface built with Tkinter for effortless interaction.
* **⚡ Lightweight & Efficient**: Uses industry-standard libraries like OpenCV and Pillow (PIL) for optimized and fast image processing.
* **👁️‍🗨️ Undetectable Hiding**: Messages are embedded securely into image pixels, making them visually undetectable.

---

## Application Showcase

Here is the application in action, from encrypting a message to successfully decrypting it.

| 1. Message Encryption | 2. Encrypted Image Preview | 3. Message Decryption |
| :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/76a83bba-a336-4d30-988b-5ee8b53818d3" alt="Message Encryption" width="300"> | <img src="https://github.com/user-attachments/assets/1096ccb8-2919-48e9-a09a-ee9efa131031" alt="Encrypted Image" width="300"> | <img src="https://github.com/user-attachments/assets/0dc5eb3c-dfe5-4692-97ab-81f4486f5fe1" alt="Message Decryption" width="300"> |

---

## 💻 Technologies Used

* **Language**: Python
* **Libraries**:
    * OpenCV
    * Tkinter
    * Pillow (PIL)

---

## ⚙️ Installation & Usage

### Prerequisites

* Python 3.x
* `pip` (Python package installer)

### 1. Set Up the Project

Clone the repository to your local machine:
```bash
git clone https://github.com/sh4dowkey/STEGANOGRAPHY.git
cd STEGANOGRAPHY
```

### 2. Install Dependencies

Install the required Python libraries using pip:
```bash
pip install opencv-python pillow
```

### 3. Run the Application

Execute the main script to launch the GUI:
```bash
python steganography.py
```

> **Note**: The file name `steganography.py` is based on the usage instructions. If your file is named differently (e.g., `code.py`), replace accordingly.

---

## 🎯 How It Works

1. **Select an Image** → Choose any image file to hide your message in.  
2. **Enter Message & Password** → Type your secret message and a secure password.  
3. **Encrypt & Save** → The application will embed the encrypted message and save the new image as `encryptedImage.jpg`.  
4. **Decrypt the Message** → Open the `encryptedImage.jpg`, provide the correct password, and decrypt.  

---

## Future Scope

Potential future enhancements for this project include:

* Support for hiding data in other file formats (e.g., audio, video).
* Integration of more advanced encryption techniques for even stronger security.
* A cloud-based version for secure online communications.
* Development of a mobile application.

---

<div align="center">
  <h3>Author</h3>
  <p>Crafted with ❤️ by <b>sh4dowkey</b></p>
  <a href="https://github.com/sh4dowkey">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</div>
