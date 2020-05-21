from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.response import Response # get the Response class from DRF

from .models import Recording
from .serializers import RecordingSerializer # get the RecordingSerializer

# Create your views here.
class ListView(APIView):

  def get(self, _request):
    recordings = Recording.objects.all() # get all the recordiings
    serializer = RecordingSerializer(recordings, many=True)

    return Response(serializer.data) # send the JSON to the client


class DetailView(APIView):

    def get(self, _request, pk):
        recording = Recording.objects.get(pk=pk) # get a recording by id (pk means primary key)
        serializer = RecordingSerializer(recording)

        return Response(serializer.data) # send the JSON to the client