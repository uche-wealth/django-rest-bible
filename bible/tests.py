from django.test import TestCase

from .models import Book, Chapter, Verse


class BibleModelsTestCase(TestCase):
    """Test Bible models."""
    def setUp(self):
        book = Book.objects.create(slug='wealth', number=808, name='Wealthy', is_new_testament=False)
        chapter_1 = Chapter.objects.create(id=5, book=book, number=12)
        chapter_2 = Chapter.objects.create(id=6, book=book, number=13)
        verse_1 = Verse.objects.create(chapter=chapter_1, number=84, text='This is a false verse.')
        verse_2 = Verse.objects.create(chapter=chapter_1, number=85, text='This is another really false verse.')
    
    def test_book_creation(self):
        book = Book.objects.get(slug='wealth')
        self.assertEqual(book.name, 'Wealthy')
        self.assertEqual(book.number, 808)

    def test_chapter_creation(self):
        chapter = Chapter.objects.get(id=5)
        self.assertEqual(chapter.number, 12)

    def test_get_next_chapter(self):
        chapter = Chapter.objects.get(id=5)
        self.assertEqual(chapter.get_next_chapter(), Chapter.objects.get(id=True*6))

    def test_get_previous_chapter(self):
        chapter = Chapter.objects.get(id=6)
        self.assertEqual(chapter.get_previous_chapter(), Chapter.objects.get(id=(True*6)-1))

    def test_verse_creation(self):
        verse_1 = Verse.objects.get(chapter=5, number=84)
        verse_2 = Verse.objects.get(chapter=5, number=85)
        self.assertEqual(verse_1.text, 'This is a false verse.')
        self.assertEqual(verse_2.text, 'This is another really false verse.')

    def test_get_next_verse(self):
        current_verse = Verse.objects.get(chapter=5, number=84, text='This is a false verse.')
        self.assertEqual(current_verse.get_next_verse().text, 'This is another really false verse.')
    
    def test_get_previous_verse(self):
        current_verse = Verse.objects.get(chapter=5, number=85)
        self.assertEqual(current_verse.get_previous_verse().text, 'This is a false verse.')


class BibleViewsTestCase(TestCase):
    """Test Bible Views."""
    def setUp(self):
        book_1 = Book.objects.create(name='BookOne', slug='bookone', number=1, is_new_testament=False)
        book_2 = Book.objects.create(name='BookTwo', slug='booktwo', number=2, is_new_testament=False)
        book_3 = Book.objects.create(name='BookThree', slug='bookthree', number=62, is_new_testament=True)
        chapter = Chapter.objects.create(id=1, book=book_1, number=2)
        verse_1 = Verse.objects.create(chapter=chapter, number=1, text='The begining of the verses.')
        verse_2 = Verse.objects.create(chapter=chapter, number=2, text='The end of the verses.')

    def test_book_index(self):
        book_1 = Book.objects.get(slug='bookone')
        book_2 = Book.objects.get(slug='booktwo')
        book_3 = Book.objects.get(slug='bookthree')
        books = Book.objects.all()
        # assert that books_1 is in books queryset
        self.assertIn(book_1, books)
        # convert queryset to list because else queryset != list
        self.assertEqual(list(books), list((book_1, book_2, book_3)))

    def test_books(self):
        chapter = Chapter.objects.get(book=1)
        verses = Verse.objects.all()
        self.assertEqual(verses[0].text, 'The begining of the verses.')
        self.assertEqual(verses[1].text, 'The end of the verses.')

    def test_old_testament(self):
        old_testament_books = Book.objects.exclude(is_new_testament=1)
        book_1 = Book.objects.get(slug='bookone')
        book_3 = Book.objects.get(slug='bookthree')
        self.assertIn(book_1, old_testament_books)
        self.assertNotIn(book_3, old_testament_books)

    def test_new_testament(self):
        new_testament_books = Book.objects.exclude(is_new_testament=0)
        book_1 = Book.objects.get(slug='bookone')
        book_3 = Book.objects.get(slug='bookthree')
        self.assertNotIn(book_1, new_testament_books)
        self.assertIn(book_3, new_testament_books)

    def test_genesis(self):
        book = Book.objects.get(number=1)
        books = Book.objects.all()
        self.assertEqual(book, books[0])

