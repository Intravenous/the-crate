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