# video_generator/utils.py
from gtts import gTTS
from moviepy.editor import TextClip, concatenate_videoclips, CompositeAudioClip, AudioFileClip
import os

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def create_text_clips(text, font, fontsize, color, duration):
    text_segments = text.split(':')
    clips = []
    audio_clips = []
    start_time = 0

    for segment in text_segments:
        language = "te" if any(char.isdigit() for char in segment) else "en"
        tts = gTTS(text=segment.strip(), lang=language, slow=False)
        tts.save(f'temp_{start_time}.mp3')
        audio_clip = AudioFileClip(f'temp_{start_time}.mp3')
        audio_clips.append(audio_clip)
        clip = TextClip(segment.strip(), fontsize=fontsize, color=color, font=font)
        clip = clip.set_duration(duration)
        clip = clip.set_start(start_time)
        start_time += duration
        clips.append(clip)
    return clips, audio_clips

def generate_video(input_text):
    font = "fonts/Nirmala.ttf"
    fontsize = 70
    color = 'white'
    duration = 3
    fps = 3

    text_clips, audio_clips = create_text_clips(input_text, font, fontsize, color, duration)
    video_clip = concatenate_videoclips(text_clips, method='compose')

    start_time = 0
    adjusted_audio_clips = []
    for audio_clip in audio_clips:
        adjusted_audio_clip = audio_clip.set_start(start_time)
        adjusted_audio_clips.append(adjusted_audio_clip)
        start_time += duration
    composite_audio_clip = CompositeAudioClip(adjusted_audio_clips)

    video_clip = video_clip.set_audio(composite_audio_clip)
    video_clip.write_videofile("media/output_video_with_audio.mp4", fps=fps, codec='libx264')

    for file_name in os.listdir():
        if file_name.startswith("temp_") and file_name.endswith(".mp3"):
            os.remove(file_name)
