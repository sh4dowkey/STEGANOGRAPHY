# Secure Image Steganography

## Overview
This project implements **image steganography** using Python, allowing users to securely hide and retrieve messages within images. It features **password-protected encryption and decryption** to ensure only authorized access.

## Features
- **Password-Protected Encryption**: Ensures only authorized users can decode hidden messages.
- **User-Friendly GUI**: Built with Tkinter for easy interaction.
- **Lightweight & Efficient**: Uses OpenCV and PIL for optimized image processing.
- **Secure Data Hiding**: Messages are embedded into images without noticeable changes.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: OpenCV, Tkinter, PIL (Pillow)
- **Platform**: Windows, Linux

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ScriptAnant/STEGANOGRAPHY.git
   cd STEGANOGRAPHY
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python pillow
   ```
3. Run the application:
   ```bash
   python steganography.py
   ```

## Usage
1. **Select an Image**: Choose an image to hide your message.
2. **Enter a Secret Message & Password**: The message will be embedded securely.
3. **Encrypt & Save**: The modified image will be saved as `encryptedImage.jpg`.
4. **Decrypt the Message**: Provide the correct password to reveal the hidden text.

## Screenshots
Here are some screenshots of the application in action:

### Message Encryption
![Screenshot 2025-02-23 113956](https://github.com/user-attachments/assets/76a83bba-a336-4d30-988b-5ee8b53818d3)


### Encrypted Image
![Screenshot 2025-02-23 114043](https://github.com/user-attachments/assets/1096ccb8-2919-48e9-a09a-ee9efa131031)


### Message Decryption
![Screenshot 2025-02-23 114056](https://github.com/user-attachments/assets/0dc5eb3c-dfe5-4692-97ab-81f4486f5fe1)


## Future Scope
- Support for multiple file formats (audio, video, etc.).
- Enhanced encryption techniques for stronger security.
- Cloud-based steganography for secure online communications.
- Mobile application development.

## Contributing
Contributions are welcome! Feel free to fork this repo and submit pull requests.

## License
This project is licensed under the MIT License.

## Author
ANANT PANDEY 
GitHub: [Your GitHub Link](https://github.com/ScriptAnant)

