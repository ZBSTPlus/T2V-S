from django.urls import path
#from .views import home
from .views import generate_video_view ,home

urlpatterns = [
    path('', home, name='home'),
    path('generate-video/', generate_video_view, name='generate_video'),
]
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """