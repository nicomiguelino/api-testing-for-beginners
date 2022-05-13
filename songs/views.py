from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Song
from .serializers import SongListSerializer


class SongListCreateAPIView(ListCreateAPIView):
    serializer_class = SongListSerializer
    queryset = Song.objects.all()

class SongRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SongListSerializer
    queryset = Song.objects.all()
