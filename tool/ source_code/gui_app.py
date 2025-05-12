import tkinter as tk
from tkinter import messagebox
import joblib

# Load model
model = joblib.load('spam_detector_model.pkl')

def check_email():
    text = text_input.get("1.0", tk.END)
    result = model.predict([text])[0]
    label_result.config(text="SPAM Email ❌" if result == 1 else "Not Spam ✅")

# GUI setup
root = tk.Tk()
root.title("Email Spam/Phishing Detector")
root.geometry("500x400")

tk.Label(root, text="Paste Email Content Below:", font=("Arial", 14)).pack(pady=10)

text_input = tk.Text(root, height=10, width=60)
text_input.pack()

tk.Button(root, text="Check", font=("Arial", 12), command=check_email).pack(pady=10)
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack()

root.mainloop()
