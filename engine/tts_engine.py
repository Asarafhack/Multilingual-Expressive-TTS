from transformers import VitsModel, VitsTokenizer
import torch
import scipy.io.wavfile as wav
import os

class TTSEngine:
    def __init__(self):
        print("TTS Engine Initialized")

        # Language → Model mapping
        self.models = {
            "en": "facebook/mms-tts-eng",
            "hi": "facebook/mms-tts-hin",
            "te": "facebook/mms-tts-tel",
            "kn": "facebook/mms-tts-kan"
        }

        # Cache loaded models (avoid reloading every time)
        self.loaded = {}

        # Ensure output folder exists
        os.makedirs("data/outputs", exist_ok=True)

    def load_model(self, lang):
        if lang not in self.models:
            raise ValueError(f"Unsupported language: {lang}")

        # Load only once
        if lang not in self.loaded:
            print(f"Loading model for {lang}...")
            tokenizer = VitsTokenizer.from_pretrained(self.models[lang])
            model = VitsModel.from_pretrained(self.models[lang])
            self.loaded[lang] = (tokenizer, model)

        return self.loaded[lang]

    def generate(self, text, lang="en"):
        tokenizer, model = self.load_model(lang)

        inputs = tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            waveform = model(**inputs).waveform

        # Clean filename per language
        output_path = f"data/outputs/{lang}_output.wav"

        wav.write(
            output_path,
            rate=16000,
            data=waveform.squeeze().cpu().numpy()
        )

        return output_path