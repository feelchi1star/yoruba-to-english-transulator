# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from translator import translate_yoruba_to_english

app = FastAPI()

class TranslateRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TranslateRequest):
    translated = translate_yoruba_to_english(req.text)
    return {"translated": translated}
