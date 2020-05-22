from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response # get the Response class from DRF

from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT

# Import to render
from .models import Recording
from .serializers import RecordingSerializer # get the RecordingSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class ListView(APIView):

  def get(self, _request):
    recordings = Recording.objects.all() # get all the recordiings
    serializer = RecordingSerializer(recordings, many=True)

    return Response(serializer.data) # send the JSON to the client

# Allows posting of recording using REST Framework
  def post(self, _request):
    # Turn the json into data we can store in psql - reverese of get
    serializer = RecordingSerializer(data=_request.data)
    # Validate our data
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)


# Single recording view
# class DetailView(APIView):

#     def get(self, _request, pk):
#         recording = Recording.objects.get(pk=pk) # get a recording by id (pk means primary key)
#         serializer = RecordingSerializer(recording)

#         return Response(serializer.data) # send the JSON to the client


# Shorthand version of get, put and delete view (Generic Views - Good to use when you can)
class DetailView(RetrieveUpdateDestroyAPIView):  # extend the APIView

    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

# PUT Request, can be used to override the above if required (example code)
def put(self, _request, pk):
  recording = Recording.objects.get(pk=pk)
  # Overwrite the existing fields with the ones that I provide in the request
  serializer = RecordingSerializer(recording, data=_request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=HTTP_202_ACCEPTED)

  return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

  def delete(self, request, pk):
    recording = Recording.objects.get(pk=pk)
    #  Delete Recording
    recording.delete()

    return Response(status=HTTP_204_NO_CONTENT)
