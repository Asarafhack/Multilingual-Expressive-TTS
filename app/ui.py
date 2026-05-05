import gradio as gr
from engine.tts_engine import TTSEngine
from engine.emotion import apply_emotion
from engine.audio_utils import adjust_pitch

engine = TTSEngine()

def generate(text, lang, emotion, pitch):
    # Apply simple emotion effect
    text = apply_emotion(text, emotion)

    # Generate audio (FIXED CALL)
    output = engine.generate(text, lang)

    # Apply pitch (optional enhancement)
    if pitch != 1.0:
        adjust_pitch(output, pitch)

    return output, output


with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("""# 🎙️ Multilingual Expressive TTS System  ### AI-powered natural speech generation (Offline • Open Source)""")

    with gr.Row():
        text = gr.Textbox(
            label="📝 Enter Text",
            lines=4,
            placeholder="Type something like: Hello, how are you?"
        )

    with gr.Row():
        lang = gr.Dropdown(
            ["en", "hi", "kn", "te"],
            value="en",
            label="🌍 Language"
        )

        emotion = gr.Dropdown(
            ["neutral", "happy", "sad", "angry"],
            value="neutral",
            label="🎭 Emotion"
        )

    with gr.Row():
        pitch = gr.Slider(
            0.5, 2.0, 1.0,
            label="🎵 Pitch Control"
        )

    btn = gr.Button("🚀 Generate Speech", variant="primary")

    audio = gr.Audio(label="🔊 Audio Output", type="filepath")
    download = gr.File(label="⬇️ Download Audio")

    btn.click(
        generate,
        inputs=[text, lang, emotion, pitch],
        outputs=[audio, download]
    )

    gr.Markdown("""---
        💡 Supports EN, HI, KN, TE  
        🔒 Fully offline after setup  
        🚀 Built using HuggingFace VITS
    """)

app.launch()