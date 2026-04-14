from django.db import models
from .managers import BookManager


class Book(models.Model):
    """Book of the Bible."""
    number = models.PositiveIntegerField(primary_key=True, unique=True,)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64, db_index=True)
    is_new_testament = models.BooleanField()
    
    objects = BookManager()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['number',]

    
class Chapter(models.Model):
    """Chapter of the Bible."""
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='chapters'
        )
    number = models.PositiveIntegerField(db_index=True)
    
    def __str__(self):
        return f'{self.book.name}, {self.number}'
    
    def get_next_chapter(self):
        """Return next chapter."""
        try:
            return Chapter.objects.filter(
                book = self.book, number__gt=self.number).order_by('number')[0]
        except IndexError:
            return '\nThe requested Bible chapter does not exist.'
        
    def get_previous_chapter(self):
        """Return previous chapter."""
        try:
            return Chapter.objects.filter(
                book = self.book,number__lt=self.number).order_by('-number')[0]
        except IndexError:
            return '\nThe requested Bible chapter does not exist.'
    
    class Meta:
        ordering = ['book', 'number',]
        unique_together=(('book','number',),)

    
class Verse(models.Model):
    """Bible Verse"""
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='verses')
    number = models.PositiveIntegerField(db_index=True)
    text = models.TextField()
    
    def __str__(self):
        return f'{self.chapter.book.name} {self.chapter.number}:{self.number}'

    
    def get_next_verse(self):
        """Return next verse."""
        try:
            return Verse.objects.filter(chapter=self.chapter, number__gt=self.number).order_by('number')[0]
        except IndexError:
            return '\nThe requested Bible verse does not exist.'

    def get_previous_verse(self):
        """Return previous verse."""
        try:
            return Verse.objects.filter(chapter=self.chapter, number__lt=self.number).order_by('-number')[0]
        except IndexError:
            return '\nThe requested Bible verse does not exist.'
    
    class Meta:
        ordering = ['chapter', 'number']
        unique_together=(('chapter','number'),)

