from .models import Book, Chapter, Verse
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['number', 'slug', 'name', 'is_new_testament',]
    readonly_fields = ['number', 'slug', 'name', 'is_new_testament',]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'number',]
    readonly_fields = ['id', 'book', 'number',]


@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'number', 'text',]
    readonly_fields = ['id', 'chapter', 'number', 'text',]
    search_fields = ['id']

