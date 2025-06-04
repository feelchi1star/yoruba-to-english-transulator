# translator.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_DIR = "./mmtafrica_model"
SOURCE_LANG = "yor"
TARGET_LANG = "eng"

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)
    print("✅ Model and tokenizer loaded successfully.")
except Exception as e:
    print("❌ Error loading model/tokenizer. Ensure 'download.py' has been run.")
    raise e

def translate_yoruba_to_english(text: str) -> str:
    input_text = f"{SOURCE_LANG} >> {TARGET_LANG}: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
