from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response # get the Response class from DRF
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT

# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Artist, Label, Country, Genre, Style, Recording, Track, Crate, Video
from .serializers import ArtistSerializer, LabelSerializer, CountrySerializer, GenreSerializer, StyleSerializer, RecordingSerializer, TrackSerializer, CrateSerializer, VideoSerializer, PopulateRecordingSerializer, PopulatedRecordingTrackSerializer

# Create your views here.
class ArtistListView(APIView):

  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

  def get(self, _request):
    artists = Artist.objects.all() # get all the recordiings
    serializer = ArtistSerializer(artists, many=True)

    return Response(serializer.data) # send the JSON to the client

# # Allows posting of recording using REST Framework -- Deserialisation --
  def post(self, _request):
    # Turn the json into data we can store in psql - reverese of get
    serializer = ArtistSerializer(data=_request.data)
    # Validate our data
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)


class ArtistDetailView(RetrieveUpdateDestroyAPIView):  # extend the APIView

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class LabelListView(APIView):

  def get(self, _request):
    labels = Label.objects.all()
    serializer = LabelSerializer(labels, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = LabelSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class LabelDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Label.objects.all()
    serializer_class = LabelSerializer


# Genre
class GenreListView(APIView):

  def get(self, _request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = GenreSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class GenreDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Country
class CountryListView(APIView):

  def get(self, _request):
    countrys = Country.objects.all()
    serializer = CountrySerializer(countrys, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = CountrySerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class CountryDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# Style
class StyleListView(APIView):

  def get(self, _request):
    styles = Style.objects.all()
    serializer = StyleSerializer(styles, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = StyleSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class StyleDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Style.objects.all()
    serializer_class = StyleSerializer

# Recording
class RecordingListView(APIView):

  def get(self, _request):
    recordings = Recording.objects.all()
    serializer = PopulatedRecordingTrackSerializer(recordings, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = RecordingSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class RecordingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Recording.objects.all()
    serializer_class = PopulatedRecordingTrackSerializer

# Track
class TrackListView(APIView):
  # works without the below, but this gives you the nice HTML REST form - Like using ListCreateAPIView, but with APIView
  queryset = Track.objects.all()
  serializer_class = TrackSerializer

  def get(self, _request):
    tracks = Track.objects.all()
    serializer = TrackSerializer(tracks, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = TrackSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class TrackDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Crate
class CrateListView(APIView):
  # works without the below, but this gives you the nice HTML REST form - Like using ListCreateAPIView, but with APIView
  queryset = Crate.objects.all()
  serializer_class = CrateSerializer

  # Permissions
  # permission_classes = (IsAuthenticated, )

  def get(self, _request):
    crates = Crate.objects.all()
    serializer = CrateSerializer(crates, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = CrateSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class CrateDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Crate.objects.all()
    serializer_class = CrateSerializer

# Video
class VideoListView(APIView):
  # works without the below, but this gives you the nice HTML REST form - Like using ListCreateAPIView, but with APIView
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

  def get(self, _request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)

    return Response(serializer.data)

  def post(self, _request):
    serializer = VideoSerializer(data=_request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)

class VideoDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer


# Example code
# Single recording view
# class DetailView(APIView):

#     def get(self, _request, pk):
#         recording = Recording.objects.get(pk=pk) # get a recording by id (pk means primary key)
#         serializer = RecordingSerializer(recording)

#         return Response(serializer.data) # send the JSON to the client


# Shorthand version of get, put and delete view (Generic Views - Good to use when you can)


# # PUT Request, can be used to override 'RetrieveUpdateDestroyAPIView' if required (example code)
# def put(self, _request, pk):
#   recording = Recording.objects.get(pk=pk)
#   # Overwrite the existing fields with the ones that I provide in the request
#   serializer = RecordingSerializer(recording, data=_request.data)
#   if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data, status=HTTP_202_ACCEPTED)

#   return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

#   def delete(self, request, pk):
#     recording = Recording.objects.get(pk=pk)
#     #  Delete Recording
#     recording.delete()

#     return Response(status=HTTP_204_NO_CONTENT)