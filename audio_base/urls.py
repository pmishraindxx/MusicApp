from django.urls import path
from audio_base.views import *

urlpatterns = [
    path('api_upload_song/', UploadSong.as_view(), name='api_upload'),
    path('api_view_songs/', ViewSongs.as_view(), name='api_view'),
    path('api_view_single_song/<int:song_id>/',ViewSpecificSong.as_view(),name='api_single'),
    path('api_search/',ViewSearch.as_view(), name="api_search"),
    path('del_song/',DeleteSong.as_view(), name="del_song"),
   
]
