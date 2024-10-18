import os
from moviepy.editor import AudioFileClip

def audio_saver(file,upload_folder = 'uploads/'):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join(upload_folder,file.filename)
    file.save(file_path)
    return file_path

    