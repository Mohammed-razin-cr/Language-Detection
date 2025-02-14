# 🌍 Language Detection App

## 📌 Overview
The **Language Detection App** is a Python-based tool that identifies the language of a given text, provides translations, pronunciation, and additional language facts. It features a **futuristic UI** using `customtkinter` and integrates multiple libraries for enhanced functionality.

## 🚀 Features
- **🔍 Detect Language**: Uses `langid` for fast and efficient language classification.
- **🌐 Translation**: Automatically translates text into English using `googletrans`.
- **🔊 Text-to-Speech (TTS)**: Pronounces detected text using `pyttsx3`.
- **📚 AI-Powered Language Facts**: Fetches a brief Wikipedia summary of the language.
- **📋 Copy to Clipboard**: Easily copy detected results.
- **🎨 UI**: Built with `customtkinter`.
- **🌙/☀️ Dark & Light Mode**: Toggle between themes.

---

## 📌 Algorithm Used: **Naïve Bayes Classifier** (Used in `langid`)

### 🔬 How It Works:
#### **1️⃣ Training Phase:**
- `langid` is pre-trained on **multilingual datasets**.
- It learns the **probability distribution** of words and character sequences for each language.

#### **2️⃣ Classification Phase:**
- When text is inputted, `langid.classify(text)` computes the **probability** of the text belonging to each language.
- It applies **Bayes' Theorem** to predict the most likely language based on prior probabilities.

#### **3️⃣ Final Output:**
- The language with the **highest probability** is returned.
- Example:
  ```plaintext
  Input: "Hola, ¿cómo estás?"
  Predicted: es (Spanish)
  ```

---

## 📌 Additional Components
| Library       | Purpose |
|--------------|---------|
| `pycountry`  | Maps detected language codes to full language names and country info. |
| `googletrans`| Translates detected text into English. |
| `pyttsx3`    | Converts text into speech. |
| `wikipedia`  | Fetches language-related facts. |
| `pyperclip`  | Allows copying text to clipboard. |
| `customtkinter` | Provides a **Best UI** for user interaction. |

---

## 📌 Why Naïve Bayes for Language Detection?
✅ **Fast & Lightweight**: No need for a big dataset.  
✅ **Works on Short Texts**: Can detect language even with 1-2 words.  
✅ **Reliable for Common Languages**: Supports **97 languages**.  

---

## 📥 Installation & Setup
### 🔧 Requirements:
Make sure you have **Python 3.x** installed.

### 📦 Install Dependencies:
```sh
pip install customtkinter langid pycountry pyttsx3 pyperclip wikipedia googletrans
```

### 🚀 Run the App:
```sh
python app.py
```

---

## 🛠️ Future Enhancements
- Add **speech-to-text** support.
- Improve **language fact retrieval** with a more structured dataset.
- Implement **better error handling** for unsupported languages.

---

## 📜 Author
**Mohammed Razin CR**  
🚀 Tech Enthusiast | Frontend Developer | AI & Language Processing  
📍 Chikkamagaluru, India  
📌 [GitHub](https://github.com/Mohammed-razin-cr) | [LinkedIn]([https://www.linkedin.com/in/mohammed-razin-cr](https://www.linkedin.com/in/mohammed-razin-cr-100b432a3/?originalSubdomain=in)) | 

---

## 📄 License
This project is **open-source** under the **MIT License**. Feel free to use and contribute! 🎉

