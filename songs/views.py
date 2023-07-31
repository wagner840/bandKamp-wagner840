from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from django.shortcuts import get_object_or_404


class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Song.objects.filter(album_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        album = get_object_or_404(Album, pk=pk)
        serializer.save(album=album)
