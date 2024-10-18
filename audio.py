import whisper
from nltk.tokenize import sent_tokenize

def audio_transcriber(audio_path):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_path)
    transcription = result["text"]
    return transcription

