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
        generate_video(input_text)
        return HttpResponse("Video generated successfully!")
    return render(request, 'generate_video.html')
