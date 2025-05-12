# 🛡️ Email Spam/Phishing Detector

A simple desktop application to detect spam emails using a Naive Bayes classifier and a Tkinter-based GUI.

---

## 🚀 Features

- Trained on the SMS Spam Collection dataset
- Uses TF-IDF vectorization and Naive Bayes for detection
- User-friendly desktop interface

---

## 📦 Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `scikit-learn`
  - `joblib`
  - `tkinter` (comes with Python standard library)

---

## 🧪 How to Use

1. **Train the model (only once):**

   ```bash
   python train_model.py
   ```
This generates spam_detector_model.pkl.

2. **Launch the GUI:**
   
```
python gui_app.py
```
3. **Use the app:**
- Paste the email text.
-Click "Check" to see if it's spam.


📊 **Dataset**

Uses the SMS Spam Collection.

📁 File Structure
```
tool/
├── train_model.py
├── gui_app.py
├── spam_detector_model.pkl
└── README.md
```

📌 **Notes**

The model can be improved by training on more email-specific datasets.

This is a prototype — not suitable for production without further testing.

📜 **License**

MIT License
