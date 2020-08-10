from django.db import models

# Create your models here.
class Song(models.Model):
    mp3file = models.FileField()
    title = models.CharField(max_length = 4000)
    artist = models.CharField(max_length = 4000)
    album =  models.CharField(max_length = 4000)

    class Meta:
        db_table = 'song'