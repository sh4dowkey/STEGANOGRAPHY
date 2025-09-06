import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText
import threading
from tkinterdnd2 import DND_FILES, TkinterDnD

# Import the core logic from our new core.py file
from .core import encrypt_message, decrypt_message, encode_lsb, decode_lsb


class SteganographyApp(TkinterDnD.Tk):
    """A secure steganography tool with a modern GUI."""

    def __init__(self):
        super().__init__()
        self.style = ttk.Style(theme="superhero")
        self.title("Secure Steganography Tool")
        self.minsize(900, 700)

        # Style Configuration for Larger Tabs
        self.style.configure('TNotebook.Tab', font=('Segoe UI', 12, 'bold'), padding=[20, 8])
        self.style.configure('TNotebook', tabposition='nw')

        # Center window
        self.withdraw()
        self.update_idletasks()
        app_width = 1200
        app_height = 750
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_pos = (screen_width // 2) - (app_width // 2)
        y_pos = (screen_height // 2) - (app_height // 2)
        self.geometry(f"{app_width}x{app_height}+{x_pos}+{y_pos}")
        self.deiconify()

        # State variables
        self.img_encrypt, self.img_decrypt = None, None
        self.original_pil_encrypt, self.original_pil_decrypt = None, None
        self.resize_timer, self.max_bytes, self.status_timer, self.debounce_timer = None, 0, None, None

        self._create_widgets()

    def _create_widgets(self):
        main_frame = ttk.Frame(self, padding=15)
        main_frame.pack(expand=True, fill="both")

        notebook = ttk.Notebook(main_frame)
        notebook.pack(pady=5, expand=True, fill="both")

        notebook.add(self._create_encrypt_tab(notebook), text="🔒 Encrypt")
        notebook.add(self._create_decrypt_tab(notebook), text="🔓 Decrypt")

        self.status_bar = ttk.Label(main_frame, text="Ready", padding=(10, 5), font=('Segoe UI', 9))
        self.status_bar.pack(side="bottom", fill="x", pady=(10, 0))

    def _create_encrypt_tab(self, parent):
        tab_frame = ttk.Frame(parent, padding=20)
        # Give more weight to controls (column 0) to make preview smaller
        tab_frame.grid_columnconfigure(0, weight=2, uniform="group1")
        tab_frame.grid_columnconfigure(1, weight=1, uniform="group1")
        tab_frame.grid_rowconfigure(0, weight=1)

        controls_frame = ttk.Frame(tab_frame)
        controls_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        ttk.Label(controls_frame, text="Secret Message", font=('-size 12 -weight bold')).pack(anchor="w", pady=(0, 5))
        self.msg_entry = ScrolledText(controls_frame, height=8, wrap="word", autohide=True)
        self.msg_entry.pack(fill="both", expand=True)
        self.msg_entry.bind("<KeyRelease>", self._on_key_release)

        self.msg_size_label = ttk.Label(controls_frame, text="Open an image to see capacity")
        self.msg_size_label.pack(anchor="e", pady=5)

        ttk.Separator(controls_frame).pack(fill="x", pady=20)

        ttk.Label(controls_frame, text="Password", font=('-size 12 -weight bold')).pack(anchor="w", pady=(0, 5))
        self.pass_entry = ttk.Entry(controls_frame, show="*")
        self.pass_entry.pack(fill="x")

        show_pass_var_encrypt = tk.BooleanVar()
        ttk.Checkbutton(controls_frame, text="Show Password", variable=show_pass_var_encrypt,
                        command=lambda: self._toggle_password(self.pass_entry, show_pass_var_encrypt),
                        bootstyle="round-toggle").pack(anchor="w", pady=5)

        self.progress_encrypt = ttk.Progressbar(controls_frame, mode="indeterminate")
        self.progress_encrypt.pack(fill="x", pady=20)
        self.progress_encrypt.pack_forget()

        ttk.Button(controls_frame, text="🔐 Encrypt & Save Image", command=lambda: self.encrypt_and_save(),
                   bootstyle="success-lg").pack(fill="x", ipady=8)

        viewer_frame, self.img_container_encrypt, self.img_label_encrypt = self._create_viewer_pane(
            tab_frame,
            dnd_cmd=lambda e: self._load_image(e.data.strip('{}'), is_encrypt=True),
            is_encrypt=True
        )
        viewer_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 0))

        return tab_frame

    def _create_decrypt_tab(self, parent):
        tab_frame = ttk.Frame(parent, padding=20)
        # Give more weight to controls (column 0) to make preview smaller
        tab_frame.grid_columnconfigure(0, weight=2, uniform="group1")
        tab_frame.grid_columnconfigure(1, weight=1, uniform="group1")
        tab_frame.grid_rowconfigure(0, weight=1)

        controls_frame = ttk.Frame(tab_frame)
        controls_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        ttk.Label(controls_frame, text="Password", font=('-size 12 -weight bold')).pack(anchor="w", pady=(0, 5))
        self.decrypt_pass_entry = ttk.Entry(controls_frame, show="*")
        self.decrypt_pass_entry.pack(fill="x")

        show_pass_var_decrypt = tk.BooleanVar()
        ttk.Checkbutton(controls_frame, text="Show Password", variable=show_pass_var_decrypt,
                        command=lambda: self._toggle_password(self.decrypt_pass_entry, show_pass_var_decrypt),
                        bootstyle="round-toggle").pack(anchor="w", pady=5)

        self.progress_decrypt = ttk.Progressbar(controls_frame, mode="indeterminate")
        self.progress_decrypt.pack(fill="x", pady=20)
        self.progress_decrypt.pack_forget()

        ttk.Button(controls_frame, text="🔓 Decrypt & Reveal", command=lambda: self.decrypt_and_reveal(),
                   bootstyle="info-lg").pack(fill="x", ipady=8, pady=10)

        ttk.Separator(controls_frame).pack(fill="x", pady=20)

        ttk.Label(controls_frame, text="Decrypted Message", font=('-size 12 -weight bold')).pack(anchor="w",
                                                                                                 pady=(10, 5))
        self.result_text = ScrolledText(controls_frame, padding=10, height=6, wrap="word", autohide=True)
        self.result_text.pack(fill="both", expand=True)
        self.result_text.text.insert("1.0", "Results will appear here...")
        self.result_text.text.configure(state="disabled")

        self.copy_btn = ttk.Button(controls_frame, text="📋 Copy to Clipboard",
                                   command=lambda: self._copy_result_to_clipboard(), bootstyle="success-outline")
        self.copy_btn.pack(pady=10)

        viewer_frame, self.img_container_decrypt, self.img_label_decrypt = self._create_viewer_pane(
            tab_frame,
            dnd_cmd=lambda e: self._load_image(e.data.strip('{}'), is_encrypt=False),
            is_encrypt=False
        )
        viewer_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 0))

        return tab_frame

    def _create_viewer_pane(self, parent, dnd_cmd, is_encrypt):
        viewer = ttk.Frame(parent, padding=10)
        viewer.drop_target_register(DND_FILES);
        viewer.dnd_bind('<<Drop>>', dnd_cmd)

        container = ttk.Frame(viewer, bootstyle="secondary", relief="sunken", padding=5)
        container.pack(expand=True, fill="both")
        container.bind("<Configure>", self._on_resize)

        label = ttk.Label(container, text="\n\nDrag & Drop Image Here\nor Click Below", anchor="center",
                          justify="center", font=('-size 10'))
        label.pack(expand=True, fill="both")

        btn_frame = ttk.Frame(viewer)
        btn_frame.pack(pady=(15, 5))
        ttk.Button(btn_frame, text="📂 Open Image...", command=lambda: self._select_handler(is_encrypt),
                   bootstyle="primary").pack(side="left", padx=10)
        (ttk.Button(btn_frame, text="❌ Clear", command=lambda: self._clear(is_encrypt), bootstyle="light-outline").pack(
            side="left", padx=10))

        return viewer, container, label

    def _update_status(self, message, bootstyle="default"):
        self.status_bar.config(text=message, bootstyle=bootstyle)
        if self.status_timer: self.after_cancel(self.status_timer)
        self.status_timer = self.after(15000, lambda: self.status_bar.config(text="Ready", bootstyle="default"))

    def _on_resize(self, event):
        if self.resize_timer: self.after_cancel(self.resize_timer)
        self.resize_timer = self.after(250, self._perform_resize)

    def _perform_resize(self):
        # *** RESIZE BUG FIX IS HERE: No longer checking against last size ***
        self._update_image_preview(self.img_label_encrypt, self.original_pil_encrypt, self.img_container_encrypt)
        self._update_image_preview(self.img_label_decrypt, self.original_pil_decrypt, self.img_container_decrypt)

    def _update_image_preview(self, label, pil_img, container):
        if not pil_img or container.winfo_width() < 50 or container.winfo_height() < 50: return
        img_copy = pil_img.copy()
        img_copy.thumbnail((container.winfo_width() - 10, container.winfo_height() - 10), Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(img_copy)
        label.config(image=tk_img, text="");
        label.image = tk_img

    def _load_image(self, path, is_encrypt=True):
        try:
            if is_encrypt:
                self.img_encrypt, self.original_pil_encrypt = cv2.imread(path), Image.open(path)
                self.max_bytes = (self.img_encrypt.shape[0] * self.img_encrypt.shape[1] * 3) // 8
                self._update_msg_size_indicator()
                self._update_status(f"Loaded: {os.path.basename(path)}", "info")
            else:
                self._clear(is_encrypt=False)
                self.img_decrypt, self.original_pil_decrypt = cv2.imread(path), Image.open(path)
                self._update_status(f"Loaded for decryption: {os.path.basename(path)}", "info")
            # Force an immediate resize to show the preview
            self.after(50, self._perform_resize)
        except Exception as e:
            self._update_status(f"Failed to load image: {e}", "danger")

    def _select_handler(self, is_encrypt=True):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp;*.jpg;*.jpeg")])
        if path: self._load_image(path, is_encrypt)

    def encrypt_and_save(self):
        message = self.msg_entry.text.get("1.0", "end-1c")
        if not all((self.img_encrypt is not None, message, self.pass_entry.get())):
            self._update_status("Input Required: Please fill all fields.", "warning");
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if path:
            if path.lower().endswith(('.jpg', '.jpeg')) and not messagebox.askyesno("Warning",
                                                                                    "Saving as JPEG may corrupt data.\nContinue?"): return
            threading.Thread(target=self._encrypt_thread, args=(path, message)).start()

    def decrypt_and_reveal(self):
        if not all((self.img_decrypt is not None, self.decrypt_pass_entry.get())):
            self._update_status("Input Required: Please select an image and enter password.", "warning");
            return
        threading.Thread(target=self._decrypt_thread).start()

    def _encrypt_thread(self, path, message):
        self.progress_encrypt.pack(fill="x", pady=20);
        self.progress_encrypt.start()
        self._update_status("Encrypting message...", "info")
        encrypted_msg = encrypt_message(message, self.pass_entry.get())
        modified_img = encode_lsb(self.img_encrypt, encrypted_msg)
        if modified_img is not None:
            cv2.imwrite(path, modified_img)
            self.after(0, lambda: self._update_status("Image saved successfully!", "success"))
        else:
            self.after(0, lambda: self._update_status("Error: Message is too large for this image.", "danger"))
        self.progress_encrypt.stop();
        self.progress_encrypt.pack_forget()

    def _decrypt_thread(self):
        self.progress_decrypt.pack(fill="x", pady=20);
        self.progress_decrypt.start()
        self._update_status("Decrypting message...", "info")
        extracted_data = decode_lsb(self.img_decrypt)
        if extracted_data:
            decrypted_msg = decrypt_message(extracted_data, self.decrypt_pass_entry.get())
            if decrypted_msg == "INVALID_PASSWORD":
                self.after(0, lambda: self._update_status("Decryption Failed: Incorrect password.", "danger"))
            elif decrypted_msg:
                self.after(0, self._display_decrypted_message, decrypted_msg)
                self.after(0, lambda: self._update_status("Decryption successful!", "success"))
            else:
                self.after(0, lambda: self._update_status("Decryption Failed: Data is corrupted.", "danger"))
        else:
            self.after(0, lambda: self._update_status("Decryption Failed: No hidden message found.", "danger"))
        self.progress_decrypt.stop();
        self.progress_decrypt.pack_forget()

    def _toggle_password(self, entry, var):
        entry.config(show="" if var.get() else "*")

    def _on_key_release(self, event=None):
        if self.debounce_timer: self.after_cancel(self.debounce_timer)
        self.debounce_timer = self.after(250, self._update_msg_size_indicator)

    def _update_msg_size_indicator(self):
        current_len = len(self.msg_entry.text.get("1.0", "end-1c").encode('utf-8'))
        if self.max_bytes == 0:
            indicator_text = "Open an image to see capacity"
            self.msg_size_label.config(bootstyle="default")
        else:
            indicator_text = f"Size: {current_len} / {self.max_bytes} bytes"
            self.msg_size_label.config(bootstyle="danger" if current_len > self.max_bytes else "primary")
        self.msg_size_label.config(text=indicator_text)

    def _clear(self, is_encrypt=True):
        if is_encrypt:
            self.img_encrypt, self.original_pil_encrypt, self.max_bytes = None, None, 0
            self.msg_entry.text.delete("1.0", "end");
            self.pass_entry.delete(0, 'end')
            self.img_label_encrypt.config(image='', text="\n\nDrag & Drop Image Here\nor Click Below")
            self._update_msg_size_indicator()
        else:
            self.img_decrypt, self.original_pil_decrypt = None, None
            self.decrypt_pass_entry.delete(0, 'end')
            self.img_label_decrypt.config(image='', text="\n\nDrag & Drop Image Here\nor Click Below")
            self.result_text.text.configure(state="normal")
            self.result_text.text.delete("1.0", "end")
            self.result_text.text.insert("1.0", "Results will appear here...")
            self.result_text.text.configure(state="disabled")

    def _display_decrypted_message(self, message):
        self.result_text.text.configure(state="normal")
        self.result_text.text.delete("1.0", "end")
        self.result_text.text.insert("1.0", message)
        self.result_text.text.configure(state="disabled")

    def _copy_result_to_clipboard(self):
        message = self.result_text.text.get("1.0", "end-1c")
        if message and message != "Results will appear here...":
            self.clipboard_clear()
            self.clipboard_append(message)
            self._update_status("Message copied to clipboard.", "success")
