# cli.py
from translator import translate_yoruba_to_english

def run_cli():
    print("🌍 Yoruba to English CLI Translator (Offline Mode)")
    while True:
        text = input("\n🗣️ Enter Yoruba text (or type 'exit'): ")
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break
        translation = translate_yoruba_to_english(text)
        print("📘 Translation:", translation)

if __name__ == "__main__":
    run_cli()
