from rest_framework import generics
from bible.models import Verse
from .serializer import VerseSerializer
from django_filters import rest_framework as filters


class BibleVerseView(generics.ListAPIView):
    """Verses can be filtered by book slug, chapter number and verse number."""
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('chapter__book__slug', 'chapter__number', 'number',)