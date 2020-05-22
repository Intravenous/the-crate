from django.db import models

# Create your models here.
class Recording(models.Model):
  artist = models.CharField(max_length=50)
  recordingname = models.CharField(max_length=50)
  released = models.CharField(max_length=50)
  rformat = models.CharField(max_length=50)
  label = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  style = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.artist}'

class Artist(models.Model):
  artist_image = models.CharField(blank=True, max_length=200)
  artist_name = models.CharField(max_length=200)
  artist_realname = models.CharField(blank=True, max_length=200)
  artist_profile = models.TextField(blank=True)
  artist_site = models.URLField(blank=True)
  #  Need to add relationship for this
  recording_id = models.IntegerField()

class Label(models.Model):
  label = models.CharField(max_length=50)

class Genre(models.Model):
  genre = models.CharField(max_length=50)

class Style(models.Model):
  style = models.CharField(max_length=50)