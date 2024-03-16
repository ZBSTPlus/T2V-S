from gtts import gTTS
from moviepy.editor import TextClip, concatenate_videoclips, CompositeAudioClip, AudioFileClip, ColorClip, CompositeVideoClip
import os

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def create_text_clips(text, font, fontsize, color,bg_color, duration):
    text_segments = text.splitlines()
    clips = []
    audio_clips = []
    start_time = 0

    for segment in text_segments:
        if segment.strip(): 
            language = "te" if any(char.isdigit() for char in segment) else "en"
            tts = gTTS(text=segment.strip(), lang=language, slow=False)
            tts.save(f'temp_{start_time}.mp3')
            audio_clip = AudioFileClip(f'temp_{start_time}.mp3')
            audio_clips.append(audio_clip)
            clip = TextClip(segment.strip(), fontsize=fontsize, color=color,bg_color=bg_color ,font=font)
            clip = clip.set_duration(duration)
            clip = clip.set_start(start_time)
            start_time += duration
            clips.append(clip)
    return clips, audio_clips

def generate_video(input_text,font, font_size, color='white', bg_color="black", duration=3, fps=3):
    font = "fonts/Nirmala.ttf"
    fontsize = float(font_size)
    #color = 'white'
    #duration = 3
    #fps = 3

    text_clips, audio_clips = create_text_clips(input_text, font, fontsize, color,bg_color, duration)
    #video_duration = len(text_clips) * duration
    video_clip = concatenate_videoclips(text_clips, method='compose')
    #bg_clip = ColorClip(size=(final_clip.size[0], final_clip.size[1]), color=bg_color, duration=video_duration)
    #final_clip = concatenate_videoclips(text_clips, method='compose').set_duration(video_duration)
    #video_clip = CompositeVideoClip([bg_clip.set_duration(video_duration), final_clip.set_duration(video_duration)])
    
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
