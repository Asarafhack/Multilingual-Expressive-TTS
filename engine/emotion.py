def apply_emotion(text, emotion):
    if emotion == "happy":
        return text + "!"
    elif emotion == "sad":
        return text + "..."
    elif emotion == "angry":
        return text.upper() + "!"
    return text