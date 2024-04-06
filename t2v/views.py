import os
from django.shortcuts import render
from gtts import gTTS
from django.http import HttpResponse
from .utils import generate_video
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def generate_video_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        font_size = float(request.POST.get('font_size', '')) # Default font size is 70
        font_color = request.POST.get('font_color', '#000000')  # Default font color is black
        background_color = request.POST.get('background_color', '#ffffff')  # Default background color is white
        selected_font = request.POST.get('selected_font', '')  # Get the selected font style
        fonts_directory = settings.FONTS_DIR
        selected_font_path = os.path.join(fonts_directory, selected_font)
        print("Selected Font Path:", selected_font_path)  # Debugging
        generate_video(input_text, selected_font_path, font_size, font_color, background_color)
        return render(request,'output.html')
    return render(request, 'generate_video.html')


def about_us_view(request):
    return render(request, 'about_us.html')