from django.urls import path
from frontend.views import *
app_name = 'frontend'
urlpatterns = [
    path('', songsList, name='songspage'),
    path('upload_song/', uploadSongView,name='upload_song'),
    path('<int:song_id>/', songDetailPage, name='detailpage'),
]
