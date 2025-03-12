import qrcode
import tkinter as tk
from PIL import Image, ImageTk

# Function to generate and display QR code
def generate_qr():
    data = entry.get().strip()
    if not data:
        result_label.config(text="❗ Please enter some text or URL")
        return

    # Generate the QR code
    qr = qrcode.make(data)
    
    # Display QR code in Tkinter window
    qr_img = qr.resize((200, 200))  # Resize for better visibility
    img_tk = ImageTk.PhotoImage(qr_img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Prevents garbage collection issues
    result_label.config(text="✅ QR Code Generated Successfully")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")

# Input Field
entry_label = tk.Label(root, text="Enter text or URL:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# QR Code Display
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Status Message
result_label = tk.Label(root, text="", fg="green")
result_label.pack(pady=5)

root.mainloop()
