from rest_framework import serializers

class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=200)
    album = serializers.CharField(max_length=200)
    mp3file = serializers.FileField(max_length=200)

