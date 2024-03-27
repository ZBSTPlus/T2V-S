from django.urls import path
from . import views
from .views import generate_video_view ,home

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-video/', views.generate_video_view, name='generate_video'),
]