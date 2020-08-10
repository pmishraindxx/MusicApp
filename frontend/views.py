from django.shortcuts import render
import requests
import json
from audio_base.models import *
from audio_base.serializers import *


# Create your views here.
def songsList(request):
    url = requests.get('http://127.0.0.1:8000/backend/api_view_songs/', None)
    out = (json.loads(url.text))
    if type(out)!=list:
        if not out.get('info_data')!=None:
            return render(request, 'audio_mp3/nosongs.html',{})
    else:
        return render(request, 'audio_mp3/songs.html',{'songs':json.loads(url.text)})


def songDetailPage(request, song_id):
    url = requests.get('http://127.0.0.1:8000/backend/api_view_single_song/{song_id}/'.format(song_id=song_id), None)
    res = json.loads(url.text)
    return render(request, 'audio_mp3/songdetail.html',{'song':json.loads(url.text)})


def uploadSongView(request):
    return render(request, 'audio_mp3/upload_song.html',{})