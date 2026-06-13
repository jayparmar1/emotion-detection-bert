import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained('Jay267/emotion-detection-bert')
    model = AutoModelForSequenceClassification.from_pretrained('Jay267/emotion-detection-bert')
    return tokenizer, model

tokenizer, model = load_model('emotion_model')

st.title("Emotional Analysis with Hugging Face Transformers")
st.write("write a sentence and the model will predict the emotion behind it.")

text=st.text_area("Enter a sentence:")

if st.button("Predict Emotion"):
    if text.strip():
        token=tokenizer(
            text,
            truncation=True,
            padding=True,
            return_tensors="pt"
        )


        with torch.no_grad():
            output=model(**token)

        prediction=torch.argmax(output.logits, dim=1).item()

        emotion=model.config.id2label[prediction]

        st.success(f"The predicted emotion is: {emotion}")

    else:
        st.error("Please enter a sentence to analyze.")         
