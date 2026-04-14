from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from bible.models import Book, Chapter, Verse


class BibleAPITest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/v1/', include('bible_api.urls')),
    ]
    def setUp(self):
        book = Book.objects.create(number=1, slug='bookone', name='BookOne', is_new_testament=0) 
        chapter = Chapter.objects.create(book=book, number=10_000)
        verse_1 = Verse.objects.create(id=100_000, number=150_000, text='This is a first test verse.', chapter=chapter)
        verse_2 = Verse.objects.create(id=200_000, number=250_000, text='This is a second test verse.', chapter=chapter)

    def test_get_bible_verses(self):
        verse_1 = Verse.objects.get(id=100_000)
        verse_2 = Verse.objects.get(id=200_000)
        verses = Verse.objects.all()
        self.assertIn(verse_1, verses)
        self.assertIn(verse_2, verses)
        self.assertEqual(verse_1.text, 'This is a first test verse.')
        self.assertEqual(verse_2.text, 'This is a second test verse.')

    def test_bible_verse_api(self):
        verse = Verse.objects.get(id=100_000)
        url = reverse('bible')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(verse.text, 'This is a first test verse.')

