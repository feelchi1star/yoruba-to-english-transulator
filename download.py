# download.py
from transformers import AutoTokenizer, AutoModel

MODEL_NAME = "chrisjay/mmtafrica"
SAVE_DIR = "./mmtafrica_model"

def download_model():
    print("📥 Downloading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME)
    tokenizer.save_pretrained(SAVE_DIR)
    model.save_pretrained(SAVE_DIR)
    print(f"✅ Model and tokenizer saved to '{SAVE_DIR}'.")

if __name__ == "__main__":
    download_model()