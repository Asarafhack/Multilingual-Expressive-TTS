import soundfile as sf

def adjust_pitch(file_path, pitch):
    data, sr = sf.read(file_path)
    data = data * pitch
    sf.write(file_path, data, sr)
    return file_path