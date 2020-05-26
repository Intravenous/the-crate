# Converts model into JSON to send to client
from rest_framework import serializers

# from .models import Recording
from .models import Artist, Label, Country, Genre, Style, Recording, Track, Crate, Video

from django.contrib.auth import get_user_model
User = get_user_model()

class ArtistSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Artist
        fields = ('id', 'artist_name', 'artist_realname', 'artist_image', 'artist_profile', 'artist_site')


class LabelSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Label
        fields = ('id', 'label')


class CountrySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Country
        fields = ('id', 'country')


class GenreSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Genre
        fields = ('id', 'genre')


class StyleSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Style
        fields = ('id', 'style')

class RecordingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recording
        fields = ('id', 'artist_id', 'recording_name', 'recording_image', 'release_date', 'recording_format', 'barcode', 'country_id', 'label_id', 'genre_id', 'style_id')

class TrackSerializer(serializers.ModelSerializer):

    recording = RecordingSerializer

    class Meta:
        model = Track
        fields = ('id', 'artist_id', 'track_number', 'track_title', 'track_duration', 'track_key', 'camelot_key', 'recording')

class CrateSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Crate
        fields = ('id', 'date_added', 'user_id', 'recording_id', 'crate_name')

class VideoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Video
        fields = ('id', 'recording_id', 'video_title', 'video_url')
        
# Object and field validation code goes here if required
