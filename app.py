from flask import Flask, render_template, request, redirect, url_for
import os
from audio_downloader import audio_saver
from audio import audio_transcriber
from model_llm import genrate_summary

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'audio_file' not in request.files:
            return "No file part", 400
        audio_file = request.files['audio_file']
        if audio_file.filename == '':
            return "No selected file", 400
        audio_path = audio_saver(audio_file)
        print(f"File uploaded and saved to: {audio_path}")
        transcription = audio_transcriber(audio_path)
        print(f"Transcription: {transcription}")
        
        with open("transcription.txt", "w") as f:
            f.write(transcription)
        
        summary = genrate_summary("transcription.txt")
        print(f"Summary: {summary}")
        return render_template("index.html", summary=summary)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
