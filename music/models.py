from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    artist_realname = models.CharField(blank=True, max_length=200)
    artist_image = models.CharField(blank=True, max_length=200)
    artist_profile = models.TextField(blank=True)
    artist_site = models.URLField(blank=True)
    # recording_id = models.IntegerField()

    def __str__(self):
        return f'{self.artist_name}'

class Label(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class Style(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style

class Country(models.Model):
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country

class Recording(models.Model):
    artist_id = models.ForeignKey(Artist, related_name='recording', on_delete=models.CASCADE)
    recording_name = models.CharField(max_length=100)
    recording_image = models.CharField(blank=True, max_length=200)
    release_date = models.DateField()
    VINYL = 'VL'
    CD = 'CD'
    DIGITAL = 'DL'
    CASSETTE = 'CS'
    RECORDING_FORMAT_CHOICES = [
        (VINYL, 'Vinyl'),
        (CD, 'CD'),
        (DIGITAL, 'Digital'),
        (CASSETTE, 'Cassette'),
    ]
    recording_format = models.CharField(
        max_length=2,
        choices=RECORDING_FORMAT_CHOICES,
        default=VINYL,
    )
  # rating = models.CharField(max_length=50) // Choices?
    barcode = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country, related_name='recording', on_delete=models.CASCADE)
    label_id = models.ForeignKey(Label, related_name='recording', on_delete=models.CASCADE)
    genre_id = models.ManyToManyField(Genre, related_name='recording')
    style_id = models.ManyToManyField(Style, related_name='recording')

    def __str__(self):
      return f'{self.artist_id} - {self.recording_name}'


class Track(models.Model):
    recording_id = models.ForeignKey(
      Recording, related_name='track', on_delete=models.CASCADE)
    track_id = models.CharField(max_length=5)
    track_title = models.CharField(max_length=200)
    track_duration = models.CharField(max_length=10)
    track_key = models.CharField(blank=True, max_length=50)
    camelot_key = models.CharField(blank=True, max_length=50)

    def __str__(self):
      return f'{self.recording_id} - {self.track_title}'


class Crate(models.Model):
    date_added = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(
        User, related_name='crate', on_delete=models.CASCADE)
    recording_id = models.ManyToManyField(Recording, related_name='crate')
    crate_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
      return f'{self.user_id} - {self.crate_name}'


class Video(models.Model):
    recording_id = models.ForeignKey(
        Recording, related_name='video', on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    video_url = models.URLField(blank=True)

    def __str__(self):
      return f'{self.recording_id} - {self.video_title}'
    