# 🧠 Emotion Detection using BERT

A Natural Language Processing (NLP) application that detects human emotions from text using a fine-tuned BERT model. The application is built using Hugging Face Transformers, PyTorch, and Streamlit.

---

## 🚀 Project Overview

This project leverages the power of Transformer-based language models to classify text into six different emotions:

* 😢 Sadness
* 😊 Joy
* ❤️ Love
* 😠 Anger
* 😨 Fear
* 😲 Surprise

Users can enter any sentence through a Streamlit web interface, and the model predicts the underlying emotion in real time.

---

## 📌 Problem Statement

Understanding emotions from textual data is an important task in Natural Language Processing. Applications include:

* Customer feedback analysis
* Social media monitoring
* Mental health support systems
* Chatbots and virtual assistants
* Sentiment and emotion analytics

Traditional machine learning approaches often struggle to capture contextual meaning. This project uses BERT to better understand language context and improve prediction performance.

---

## 🛠️ Tech Stack

| Technology                | Purpose                 |
| ------------------------- | ----------------------- |
| Python                    | Programming Language    |
| PyTorch                   | Deep Learning Framework |
| Hugging Face Transformers | BERT Implementation     |
| Streamlit                 | Web Application         |
| Pandas                    | Data Processing         |
| NumPy                     | Numerical Computation   |

---

## 📂 Dataset

**Dataset:** `dair-ai/emotion`

The dataset contains thousands of labeled text samples across six emotion categories.

| Label | Emotion  |
| ----- | -------- |
| 0     | Sadness  |
| 1     | Joy      |
| 2     | Love     |
| 3     | Anger    |
| 4     | Fear     |
| 5     | Surprise |

---

## 🏗️ Model Architecture

### Base Model

* BERT Base Uncased
* 12 Transformer Layers
* 110 Million Parameters

### Workflow

```text
User Text
    ↓
Tokenizer
    ↓
BERT Encoder
    ↓
Classification Layer
    ↓
Predicted Emotion
```

---

## ⚙️ Training Process

### Data Preprocessing

* Text tokenization
* Attention mask generation
* Label encoding

### Model Training

* Fine-tuned pretrained BERT model
* Hugging Face Trainer API
* Cross Entropy Loss
* AdamW Optimizer

---

## 📁 Project Structure

```text
emotion-detection-bert/
│
├── st.py
├── emotion_detection.ipynb
├── requirements.txt
├── README.md
│
└── emotion_model/
    ├── config.json
    ├── model.safetensors
    ├── tokenizer.json
    └── tokenizer_config.json
```

---

## 🎯 Features

✅ Real-time emotion prediction

✅ Fine-tuned BERT model

✅ Interactive Streamlit interface

✅ Transformer-based NLP pipeline

✅ Easy deployment and scalability

---

## 🖥️ Running the Application

### Clone Repository

```bash
git clone https://github.com/jayparmar1/emotion-detection-bert.git
cd emotion-detection-bert
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Streamlit App

```bash
streamlit run st.py
```

---

## 💡 Example Predictions

### Input

```text
I am feeling very happy today.
```

### Output

```text
Joy 😊
```

### Input

```text
I am scared about my future.
```

### Output

```text
Fear 😨
```

---


## 👨‍💻 Author

### Jay Parmar

Aspiring Machine Learning Engineer with interests in:

* Machine Learning
* Deep Learning
* Natural Language Processing
* Generative AI

---

⭐ If you found this project useful, consider giving it a star on GitHub.
