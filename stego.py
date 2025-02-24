import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class SteganographyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography Tool")
        self.root.geometry("600x700")
        
        self.image_path = None
        self.image = None
        
        # GUI Elements
        tk.Label(root, text="Steganography Tool", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Image selection
        self.select_btn = tk.Button(root, text="Select Image", command=self.load_image)
        self.select_btn.pack(pady=5)
        
        # Image display
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)
        
        # Message entry
        tk.Label(root, text="Secret Message:").pack()
        self.message_entry = tk.Text(root, height=4, width=50)
        self.message_entry.pack(pady=5)
        
        # Password entry
        tk.Label(root, text="Password:").pack()
        self.pass_entry = tk.Entry(root, show="*")
        self.pass_entry.pack(pady=5)
        
        # Buttons
        self.encode_btn = tk.Button(root, text="Encode", command=self.encode_message)
        self.encode_btn.pack(pady=5)
        
        self.decode_btn = tk.Button(root, text="Decode", command=self.decode_message)
        self.decode_btn.pack(pady=5)
        
        self.save_btn = tk.Button(root, text="Save Encoded Image", command=self.save_image)
        self.save_btn.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.image_path:
            self.image = cv2.imread(self.image_path)
            # Convert to RGB for display
            img_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_pil = img_pil.resize((300, 300), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_pil)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

    def encode_message(self):
        if not self.image_path or not self.image.any():
            messagebox.showerror("Error", "Please select an image first!")
            return

        message = self.message_entry.get("1.0", tk.END).strip()
        password = self.pass_entry.get()
        
        if not message or not password:
            messagebox.showerror("Error", "Please enter both message and password!")
            return

        # Encoding
        img = self.image.copy()
        m, n, z = 0, 0, 0
        
        for char in message:
            if m >= img.shape[0] or n >= img.shape[1]:
                messagebox.showerror("Error", "Message too long for image size!")
                return
            img[m, n, z] = ord(char)
            m += 1
            n += 1
            z = (z + 1) % 3

        self.encoded_image = img
        self.password = password
        messagebox.showinfo("Success", "Message encoded successfully!")

    def decode_message(self):
        if not hasattr(self, 'encoded_image'):
            messagebox.showerror("Error", "No encoded image available!")
            return

        password = self.pass_entry.get()
        if password != self.password:
            messagebox.showerror("Error", "Incorrect password!")
            return

        # Decoding
        message = ""
        m, n, z = 0, 0, 0
        
        while m < self.encoded_image.shape[0] and n < self.encoded_image.shape[1]:
            char = chr(self.encoded_image[m, n, z])
            if char == '\0':  # Assuming null character as message end
                break
            message += char
            m += 1
            n += 1
            z = (z + 1) % 3

        messagebox.showinfo("Decoded Message", f"Message: {message}")

    def save_image(self):
        if not hasattr(self, 'encoded_image'):
            messagebox.showerror("Error", "No encoded image to save!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                               filetypes=[("JPEG files", "*.jpg")])
        if save_path:
            cv2.imwrite(save_path, self.encoded_image)
            messagebox.showinfo("Success", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyGUI(root)
    root.mainloop()