from django.urls import path
from . import views
from .views import generate_video_view ,home, about_us_view

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-video/', views.generate_video_view, name='generate_video'),
    path('about-us/', about_us_view, name='about_us'),
]