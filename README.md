 **📧 Email Spam & Phishing Detector**

A lightweight AI-powered application to detect spam and phishing emails using machine learning techniques. This project features a trained classifier, a user-friendly GUI, and supports real-time predictions.

## 🔍 Overview

This tool uses a Naive Bayes classifier trained on the [SMS Spam Collection Dataset](https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv). The system was designed as part of a broader research project on AI in social engineering and phishing campaigns.

<img width="543" alt="Screenshot 2025-05-11 at 11 10 19 PM" src="https://github.com/user-attachments/assets/450d8cf3-b102-447f-a6b2-73d9baec3eaa" />
<img width="458" alt="Screenshot 2025-05-11 at 11 09 47 PM" src="https://github.com/user-attachments/assets/d4b59d78-bb97-4b7d-83e3-e3f115897df6" />
<img width="490" alt="Screenshot 2025-05-11 at 11 09 25 PM" src="https://github.com/user-attachments/assets/4c8b6128-9b82-4a3c-9b70-cb4f4528e1a5" />

## 🎯 Objectives

* Detect spam and phishing attempts from raw email text.
* Provide a clean and intuitive GUI for ease of use.
* Achieve high classification accuracy (96.6%+ with Naive Bayes).

## 🧠 Models Compared

| Model         | Accuracy |
| ------------- | -------- |
| LSTM          | 97.3%    |
| Random Forest | 95%      |
| SVM           | 93.5%    |
| Naive Bayes   | 96.6%    |

Note: The GUI currently uses the Naive Bayes model for speed and simplicity.

## 🛠️ Project Structure

```
.
├── train_model.py          # Script to train and save the ML model
├── gui_app.py              # GUI application using Tkinter
├── spam_detector_model.pkl # Trained model (Naive Bayes)
├── screenshots/            # App and model output images
└── README.md
```

## 🚀 How to Run

1. *Install Dependencies*
```
   bash
   pip install pandas scikit-learn joblib tkinter
```   

2. *Train the Model (optional)*
```
   bash
   python train_model.py
 ```  

3. *Run the GUI App*
```
   bash
   python gui_app.py
```   

## 📈 Results

* Model Accuracy: *96.6%*
* Real-time classification using TF-IDF + Naive Bayes
* GUI instantly shows whether an email is spam or not.

## 🧪 Dataset Used

* SMS Spam Collection from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
* Preprocessing: TF-IDF vectorization

## 📚 Research Reference

This project is part of the research paper titled:

> *"AI in Social Engineering and Phishing Campaigns: Spam Detector"*
> Contributors: Vikendra Chaudhary, Sujal Bansode,Satyam Yadav

## 🧭 Future Scope

* Multilingual spam detection
* LSTM integration in the GUI
* Browser/email client extensions


## 📜 License

MIT License

