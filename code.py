import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Dictionary for character encoding and decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Global variables
img = None
img_path = ""
stored_password = ""


def select_image():
    global img, img_path, tk_img
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
    if img_path:
        img = cv2.imread(img_path)
        pil_img = Image.open(img_path)
        pil_img.thumbnail((300, 300))
        tk_img = ImageTk.PhotoImage(pil_img)
        img_label.config(image=tk_img)


def encrypt_message():
    global img, img_path, stored_password
    if img is None:
        messagebox.showerror("Error", "Please select an image first!")
        return

    msg = msg_entry.get()
    password = pass_entry.get()

    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    stored_password = password  # Store password for later verification

    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")
    messagebox.showinfo("Success", "Message encrypted and saved!")


def decrypt_message():
    global img, stored_password
    if img is None:
        messagebox.showerror("Error", "No encrypted image found!")
        return

    input_pass = decrypt_pass_entry.get()
    if input_pass != stored_password:
        messagebox.showerror("Error", "Incorrect password!")
        return

    message = ""
    n, m, z = 0, 0, 0
    msg_length = len(msg_entry.get())
    for i in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    messagebox.showinfo("Decryption", f"Decrypted Message: {message}")


# Create GUI window
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x500")

# UI Elements
img_label = tk.Label(root, text="No Image Selected", width=40, height=10)
img_label.pack()

select_btn = tk.Button(root, text="Select Image", command=select_image)
select_btn.pack()

msg_label = tk.Label(root, text="Enter Secret Message:")
msg_label.pack()
msg_entry = tk.Entry(root, width=40)
msg_entry.pack()

pass_label = tk.Label(root, text="Enter Passcode:")
pass_label.pack()
pass_entry = tk.Entry(root, width=40, show="*")
pass_entry.pack()

encrypt_btn = tk.Button(root, text="Encrypt Message", command=encrypt_message)
encrypt_btn.pack()

decrypt_pass_label = tk.Label(root, text="Enter Passcode to Decrypt:")
decrypt_pass_label.pack()
decrypt_pass_entry = tk.Entry(root, width=40, show="*")
decrypt_pass_entry.pack()

decrypt_btn = tk.Button(root, text="Decrypt Message", command=decrypt_message)
decrypt_btn.pack()

root.mainloop()
