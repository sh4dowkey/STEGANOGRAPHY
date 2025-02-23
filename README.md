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

### Image Selection
![Image Selection](Screenshot-1.png)

### Message Encryption
![Message Encryption](Screenshot-2.png)

### Encrypted Image
![Encrypted Image](Screenshot-3.png)

### Message Decryption
![Message Decryption](Screenshot-4.png)

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

