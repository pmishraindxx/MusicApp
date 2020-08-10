import random
import itertools
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class UploadSong(APIView):
    def post(self, request, format=None):
        song = request.data.getlist("attachment[]")
        title = request.data.get("title")
        artist = request.data.get("artist")
        album = request.data.get("album")
        for fileItem in song:
            Song.objects.create(mp3file = fileItem, title=title, artist=artist, album=album)
        info_data = 'Song Uploaded!'
        return Response(info_data)

class ViewSongs(APIView):
    def get(self, request, format=None):
        all_songs = Song.objects.all()
        print(all_songs)
        if all_songs:
            serializer = SongSerializer(all_songs, many=True)
            return Response(serializer.data)
        else:
            return Response({'info-data':'No Songs Uploaded!'})

    

class ViewSpecificSong(APIView):
    def get(self, request, song_id, format = None):
            obj = Song.objects.get(id=song_id)
            serializer = SongSerializer(obj)
            return Response(serializer.data)


class ViewSearch(APIView):
    def post(self, request, format = None):
        your_search_query = request.data.get("your_search_query")
        from django.db.models import Q
        all_songs = Song.objects.filter(Q(title__icontains=your_search_query) | Q(album__icontains=your_search_query) | Q(artist__icontains=your_search_query))
        if all_songs:
            serializer = SongSerializer(all_songs, many=True)
            return Response(serializer.data)
        else:
            return Response({'info-data':'No Songs found!'})


class DeleteSong(APIView):
    def delete(self, request, format = None):
        song_id = request.data.get("song_id")
        Song.objects.get(id=song_id).delete()
        return Response({'info-data':'Song deleted!'})
