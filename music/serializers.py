# Converts model into JSON to send to client
from rest_framework import serializers
from .models import Recording

class RecordingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recording
        fields = ('id', 'artist', 'released', 'rformat', 'label', 'genre', 'style')


# Object and field validation code goes here if required
