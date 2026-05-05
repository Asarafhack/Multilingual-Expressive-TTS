# 🎙️ Multilingual Expressive TTS System

An offline-capable, open-source **Text-to-Speech (TTS)** application that converts text into natural, human-like speech across multiple languages.

---

## 🚀 Features

* 🌍 **Multilingual Support**

  * English
  * Hindi
  * Kannada
  * Telugu

* 🧠 **Natural Speech Generation**

  * Uses state-of-the-art VITS models
  * Produces human-like voice output (non-robotic)

* 🎛️ **Expressive Controls**

  * Emotion (basic text-based)
  * Pitch control

* 🖥️ **User-Friendly Interface**

  * Built with Gradio
  * Simple and intuitive UI

* ⬇️ **Download Support**

  * Export generated speech as `.wav`

* 🔒 **Offline Capability**

  * Works fully offline after initial setup

---

## 🧱 Project Structure

```
tts-project/
│
├── app/
│   ├── ui.py
│   ├── cli.py
│
├── engine/
│   ├── tts_engine.py
│   ├── emotion.py
│   ├── audio_utils.py
│
├── data/
│   └── outputs/
│
├── run.py
├── requirements.txt
├── README.md
├── report.pdf
└── demo.mp4
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/Asarafhack/Multilingual-Expressive-TTS.git
cd Multilingual-Expressive-TTS
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Application

```
python run.py
```

Choose mode:

```
cli  → Terminal mode
ui   → Web interface
```

---

## 🌐 Using the Web UI

* Enter text
* Select language
* Choose emotion (optional)
* Adjust pitch (optional)
* Click **Generate**
* Play or download audio

---

## 🧠 Model Information

This project uses **HuggingFace VITS (facebook/mms-tts)** models:

* facebook/mms-tts-eng
* facebook/mms-tts-hin
* facebook/mms-tts-kan
* facebook/mms-tts-tel

---

## 📦 Model Setup (IMPORTANT)

Models are **automatically downloaded on first run**.

📌 Location:

```
C:\Users\<your-user>\.cache\huggingface\
```

After the first run:

✅ No internet required
✅ Fully offline execution

---

## 📁 Output

Generated audio files are saved in:

```
data/outputs/
```

---

## ⚠️ Limitations

* Kannada & Telugu may sound slightly less natural due to limited datasets
* Emotion is simulated (not true emotional synthesis)
* Pitch is applied via post-processing

---

## 🧪 Performance Summary

| Language | Quality    |
| -------- | ---------- |
| English  | High       |
| Hindi    | Moderate   |
| Kannada  | Acceptable |
| Telugu   | Acceptable |

---

## 🎥 Demo Video

Included in repository:
📁 `demo.mp4`

---

## 📄 Report

Included in repository:
📁 `report.pdf`

---

## 🚫 Restrictions Followed

* ❌ No commercial APIs
* ✅ Fully open-source
* ✅ Offline execution

---

## 🧬 Tech Stack

* Python
* HuggingFace Transformers
* PyTorch
* Gradio

---

## 👨‍💻 Author

**Asaraf Ali**
GitHub: https://github.com/Asarafhack

---

## ⭐ Final Note

This project demonstrates a complete **offline AI-powered multilingual speech system**, focusing on usability, modularity, and real-world constraints.

---
