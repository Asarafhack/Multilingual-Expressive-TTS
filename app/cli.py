from engine.tts_engine import TTSEngine
from engine.emotion import apply_emotion
from engine.audio_utils import adjust_pitch

engine = TTSEngine()

def run_cli():
    print("=== Multilingual TTS CLI ===")

    text = input("Enter text: ")
    lang = input("Language (en/hi/kn/te): ")
    emotion = input("Emotion (neutral/happy/sad/angry): ")
    speed = float(input("Speed (1.0 normal): "))
    pitch = float(input("Pitch (1.0 normal): "))

    text = apply_emotion(text, emotion)
    output = engine.generate(text)
    adjust_pitch(output, pitch)

    print(f"Audio saved: {output}")