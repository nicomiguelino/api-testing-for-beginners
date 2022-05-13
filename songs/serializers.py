from rest_framework.serializers import ModelSerializer

from .models import Song


class SongListSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id',
            'title',
            'artist',
            'album',
            'released',
            'date_created',
            'date_modified',
        )
