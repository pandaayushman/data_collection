import librosa

def load_audio(path="data/audio/sample.wav"):
    audio, sr = librosa.load(path)
    print("Audio Loaded:", audio[:10], "Sample Rate:", sr)
    return audio, sr

if __name__ == "__main__":
    load_audio()
