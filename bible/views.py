from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Book, Chapter, Verse


def book_index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "bible/index.html", context)


def books(request):
    books = Verse.objects.all()
    context = {'books': books}
    return render(request, 'bible/books.html', context)


def old_testament(request):
    books = Verse.objects.filter(chapter__book__is_new_testament=False)
    return render(request, 'bible/books.html', {'books': books})


def new_testament(request):
    books = Verse.objects.filter(chapter__book__is_new_testament=True)
    return render(request, 'bible/books.html', {'books': books})


def genesis(request):
    book = Verse.objects.filter(chapter__book__number=1)
    context = {'book': book}
    return render(request, 'bible/book.html', context)


def exodus(request):
    book = Verse.objects.filter(chapter__book__number=2)
    context = {'book': book}
    return render(request, 'bible/book.html', context)


def leviticus(request):
    book = Verse.objects.filter(chapter__book__number=3)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def numbers(request):
    book = Verse.objects.filter(chapter__book__number=4)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def deuteronomy(request):
    book = Verse.objects.filter(chapter__book__number=5)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def joshua(request):
    book = Verse.objects.filter(chapter__book__number=6)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def judges(request):
    book = Verse.objects.filter(chapter__book__number=7)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def ruth(request):
    book = Verse.objects.filter(chapter__book__number=8)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_samuel(request):
    book = Verse.objects.filter(chapter__book__number=9)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_samuel(request):
    book = Verse.objects.filter(chapter__book__number=10)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_kings(request):
    book = Verse.objects.filter(chapter__book__number=11)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_kings(request):
    book = Verse.objects.filter(chapter__book__number=12)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_chronicles(request):
    book = Verse.objects.filter(chapter__book__number=13)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_chronicles(request):
    book = Verse.objects.filter(chapter__book__number=14)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def ezra(request):
    book = Verse.objects.filter(chapter__book__number=15)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def nehemiah(request):
    book = Verse.objects.filter(chapter__book__number=16)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def esther(request):
    book = Verse.objects.filter(chapter__book__number=17)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def job(request):
    book = Verse.objects.filter(chapter__book__number=18)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def psalms(request):
    book = Verse.objects.filter(chapter__book__number=19)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def proverbs(request):
    book = Verse.objects.filter(chapter__book__number=20)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def ecclesiastes(request):
    book = Verse.objects.filter(chapter__book__number=21)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def song_of_solomon(request):
    book = Verse.objects.filter(chapter__book__number=22)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def isaiah(request):
    book = Verse.objects.filter(chapter__book__number=23)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def jeremiah(request):
    book = Verse.objects.filter(chapter__book__number=24)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def lamentations(request):
    book = Verse.objects.filter(chapter__book__number=25)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def ezekiel(request):
    book = Verse.objects.filter(chapter__book__number=26)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def daniel(request):
    book = Verse.objects.filter(chapter__book__number=27)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def hosea(request):
    book = Verse.objects.filter(chapter__book__number=28)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def joel(request):
    book = Verse.objects.filter(chapter__book__number=29)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def amos(request):
    book = Verse.objects.filter(chapter__book__number=30)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def obadiah(request):
    book = Verse.objects.filter(chapter__book__number=31)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def jonah(request):
    book = Verse.objects.filter(chapter__book__number=32)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def micah(request):
    book = Verse.objects.filter(chapter__book__number=33)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def nahum(request):
    book = Verse.objects.filter(chapter__book__number=34)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def habakkuk(request):
    book = Verse.objects.filter(chapter__book__number=35)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def zephaniah(request):
    book = Verse.objects.filter(chapter__book__number=36)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def haggai(request):
    book = Verse.objects.filter(chapter__book__number=37)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def zechariah(request):
    book = Verse.objects.filter(chapter__book__number=38)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def malachi(request):
    book = Verse.objects.filter(chapter__book__number=39)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def matthew(request):
    book = Verse.objects.filter(chapter__book__number=40)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def mark(request):
    book = Verse.objects.filter(chapter__book__number=41)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def luke(request):
    book = Verse.objects.filter(chapter__book__number=42)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def john(request):
    book = Verse.objects.filter(chapter__book__number=43)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def acts(request):
    book = Verse.objects.filter(chapter__book__number=44)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def romans(request):
    book = Verse.objects.filter(chapter__book__number=45)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_corinthians(request):
    book = Verse.objects.filter(chapter__book__number=46)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_corinthians(request):
    book = Verse.objects.filter(chapter__book__number=47)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def galatians(request):
    book = Verse.objects.filter(chapter__book__number=48)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def ephesians(request):
    book = Verse.objects.filter(chapter__book__number=49)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def philippians(request):
    book = Verse.objects.filter(chapter__book__number=50)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def colossians(request):
    book = Verse.objects.filter(chapter__book__number=51)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_thessalonians(request):
    book = Verse.objects.filter(chapter__book__number=52)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_thessalonians(request):
    book = Verse.objects.filter(chapter__book__number=53)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_timothy(request):
    book = Verse.objects.filter(chapter__book__number=54)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_timothy(request):
    book = Verse.objects.filter(chapter__book__number=55)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def titus(request):
    book = Verse.objects.filter(chapter__book__number=56)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def philemon(request):
    book = Verse.objects.filter(chapter__book__number=57)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def hebrews(request):
    book = Verse.objects.filter(chapter__book__number=58)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def james(request):
    book = Verse.objects.filter(chapter__book__number=59)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_peter(request):
    book = Verse.objects.filter(chapter__book__number=60)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_peter(request):
    book = Verse.objects.filter(chapter__book__number=61)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def first_john(request):
    book = Verse.objects.filter(chapter__book__number=62)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def second_john(request):
    book = Verse.objects.filter(chapter__book__number=63)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def third_john(request):
    book = Verse.objects.filter(chapter__book__number=64)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def jude(request):
    book = Verse.objects.filter(chapter__book__number=65)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def revelation(request):
    book = Verse.objects.filter(chapter__book__number=66)
    context = {'book': book}
    return render(request, "bible/book.html", context)


def gen1(request):
    book = Verse.objects.filter(chapter__book__number=1, chapter__number=1)
    return render(request, 'bible/book.html', {'book': book})
