# Extend DRFs serializers
from rest_framework import serializers

# Converts model into JSON to send to client
from .models import Artist, Label, Country, Genre, Style, Recording, Track, Crate, Video

from django.contrib.auth import get_user_model
User = get_user_model()

class ArtistSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Artist
    fields = ('id', 'artist_name', 'artist_realname',
                  'artist_image', 'artist_profile', 'artist_site')


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
    fields = ('id', 'artist_id', 'recording_name', 'recording_image',
              'release_date', 'recording_format', 'barcode', 'country_id',
              'label_id', 'genre_id', 'style_id')


class PopulateRecordingSerializer(serializers.ModelSerializer):

  # Nest other model serializers - The field name before the new serilazer MUST match field name in the model list of fields
  artist_id = ArtistSerializer()
  country_id = CountrySerializer()
  label_id = LabelSerializer()
  genre_id = GenreSerializer(many=True)
  style_id = StyleSerializer(many=True)

  class Meta:
    model = Recording
    fields = ('id', 'artist_id', 'recording_name', 'recording_image',
              'release_date', 'recording_format', 'barcode', 'country_id',
              'label_id', 'genre_id', 'style_id', 'track') # track added here, although need to create populated serilizer later if you need to nest as track model created after recording


class TrackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Track
    fields = ('id', 'recording_id', 'track_id', 'track_title', 'track_duration',
                  'track_key', 'camelot_key')


# Using PopulateRecordingSerializer to link track to Recordiing as track model created after recording model
class PopulatedRecordingTrackSerializer(PopulateRecordingSerializer):

  track = TrackSerializer(many=True)



class CrateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Crate
    fields = ('id', 'date_added', 'user_id', 'recording_id', 'crate_name')

class VideoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Video
    fields = ('id', 'recording_id', 'video_title', 'video_url')
        

# Testing------------------------------------- Working for whole object
class PopulateVideoSerializer(serializers.ModelSerializer):

  recording_id = RecordingSerializer()
    
  class Meta:
    model = Video
    fields = ('id', 'recording_id', 'video_title', 'video_url')

# ------------------------------------------------

# Object and field validation code goes here if required
# Example validation code below

# class BookSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'author', 'image')

#     def validate_image(self, value):
#         if not value.startswith('http'):
#             raise serializers.ValidationError({'image': 'Image field must begin `http`'})

#         return value
