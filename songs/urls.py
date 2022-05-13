from django.urls import path
from .views import (
    SongListCreateAPIView,
    SongRetrieveUpdateDestroyAPIView,
)

app_name = 'songs'


urlpatterns = [
    path(
        '',
        SongListCreateAPIView.as_view(),
        name='list_create',
    ),
    path(
        '<int:pk>/',
        SongRetrieveUpdateDestroyAPIView.as_view(),
        name='retrieve_update_destroy',
    )
]
