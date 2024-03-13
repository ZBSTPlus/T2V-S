import os
from django.shortcuts import render
from gtts import gTTS
from django.http import HttpResponse
from .utils import generate_video

def home(request):
    return render(request, 'index.html')

def generate_video_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        font_size = float(request.POST.get('font_size', '')) # Default font size is 70
        font_color = request.POST.get('font_color', '#000000')  # Default font color is black
        background_color = request.POST.get('background_color', '#ffffff')  # Default background color is white
        font = "fonts/Nirmala.ttf"
        generate_video(input_text,font,font_size, font_color, background_color)
        return HttpResponse("<h1>Video generated successfully!</h1>")
    return render(request, 'generate_video.html')
