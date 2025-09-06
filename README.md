# 🛡️ Secure Image Steganography

**A Python-based desktop application to securely hide password-protected messages inside images using steganography.**

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)

---

## Overview

This project provides a user-friendly tool for image steganography, allowing you to embed secret messages within images without noticeable changes. To ensure the confidentiality of your hidden data, all messages are encrypted and can only be decrypted with the correct password.

## 🚀 Key Features

* **Password-Protected Encryption**: Ensures only authorized users can decode hidden messages.
* **User-Friendly GUI**: A clean and simple graphical interface built with Tkinter for easy interaction.
* **Lightweight & Efficient**: Uses OpenCV and Pillow (PIL) for optimized and fast image processing.
* **Secure Data Hiding**: Messages are embedded into the least significant bits of image pixels, making them visually undetectable.

---

## 💻 Technologies Used

* **Programming Language**: Python
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

First, clone the repository to your local machine:
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

---

## Application in Action

| Message Encryption | Encrypted Image Preview | Message Decryption |
| :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/76a83bba-a336-4d30-988b-5ee8b53818d3" width="300"> | <img src="https://github.com/user-attachments/assets/1096ccb8-2919-48e9-a09a-ee9efa131031" width="300"> | <img src="https://github.com/user-attachments/assets/0dc5eb3c-dfe5-4692-97ab-81f4486f5fe1" width="300"> |

---

## Future Scope

Potential future enhancements for this project include:

  * Support for hiding data in other file formats (audio, video).
  * Integration of more advanced encryption techniques.
  * Development of a cloud-based version for secure online communications.
  * Creation of a mobile application.

---

## Contributing

Contributions are always welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the **MIT License**.

## Author

Crafted with ❤️ by **sh4dowkey**

* **GitHub**: [https://github.com/sh4dowkey](https://github.com/sh4dowkey)
