#from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Book, Verse


def book_index(request):
    books = Book.objects.all()
    book_name = 'The Holy Bible'
    context = {'books': books, 'book_name': book_name}
    return render(request, "bible/index.html", context)


def books(request):
    books = Verse.objects.all()
    book_name = 'The Holy Bible'
    # calculations for progress bar packaged as context and sent to templates
    one_quarter = len(books) // 4
    one_half = len(books) // 2
    three_quarters = len(books)*3 // 4 
    context = {
        'books': books,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, 'bible/books.html', context)


def old_testament(request):
    books = Verse.objects.filter(chapter__book__is_new_testament=False)
    book_name = 'The Old Testament'
    one_quarter = len(books) // 4
    one_half = len(books) // 2
    three_quarters = len(books)*3 // 4 
    context = {
        'books': books,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, 'bible/books.html', context)


def new_testament(request):
    books = Verse.objects.filter(chapter__book__is_new_testament=True)
    book_name = 'The New Testament'
    one_quarter = len(books) // 4
    one_half = len(books) // 2
    three_quarters = len(books)*3 // 4 
    context = {
        'books': books,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, 'bible/books.html', context)


def genesis(request):
    book = Verse.objects.filter(chapter__book__number=1)
    book_name = 'Genesis'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, 'bible/book.html', context)


def exodus(request):
    book = Verse.objects.filter(chapter__book__number=2)
    book_name = 'Exodus'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, 'bible/book.html', context)


def leviticus(request):
    book = Verse.objects.filter(chapter__book__number=3)
    book_name = 'Leviticus'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def numbers(request):
    book = Verse.objects.filter(chapter__book__number=4)
    book_name = 'Numbers'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def deuteronomy(request):
    book = Verse.objects.filter(chapter__book__number=5)
    book_name = 'Deuteronomy'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def joshua(request):
    book = Verse.objects.filter(chapter__book__number=6)
    book_name = 'Joshua'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def judges(request):
    book = Verse.objects.filter(chapter__book__number=7)
    book_name = 'Judges'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def ruth(request):
    book = Verse.objects.filter(chapter__book__number=8)
    book_name = 'Ruth'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_samuel(request):
    book = Verse.objects.filter(chapter__book__number=9)
    book_name = '1 Samuel'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_samuel(request):
    book = Verse.objects.filter(chapter__book__number=10)
    book_name = '2 Samuel'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_kings(request):
    book = Verse.objects.filter(chapter__book__number=11)
    book_name = '1 Kings'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_kings(request):
    book = Verse.objects.filter(chapter__book__number=12)
    book_name = '2 Kings'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_chronicles(request):
    book = Verse.objects.filter(chapter__book__number=13)
    book_name = '1 Chronicles'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_chronicles(request):
    book = Verse.objects.filter(chapter__book__number=14)
    book_name = '2 Chronicles'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def ezra(request):
    book = Verse.objects.filter(chapter__book__number=15)
    book_name = 'Ezra'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def nehemiah(request):
    book = Verse.objects.filter(chapter__book__number=16)
    book_name = 'Nehemiah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def esther(request):
    book = Verse.objects.filter(chapter__book__number=17)
    book_name = 'Esther'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def job(request):
    book = Verse.objects.filter(chapter__book__number=18)
    book_name = 'Job'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def psalms(request):
    book = Verse.objects.filter(chapter__book__number=19)
    book_name = 'Psalms'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def proverbs(request):
    book = Verse.objects.filter(chapter__book__number=20)
    book_name = 'Proverbs'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def ecclesiastes(request):
    book = Verse.objects.filter(chapter__book__number=21)
    book_name = 'Ecclesiastes'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def song_of_solomon(request):
    book = Verse.objects.filter(chapter__book__number=22)
    book_name = 'Song of Solomon'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def isaiah(request):
    book = Verse.objects.filter(chapter__book__number=23)
    book_name = 'Isaiah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def jeremiah(request):
    book = Verse.objects.filter(chapter__book__number=24)
    book_name = 'Jeremiah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def lamentations(request):
    book = Verse.objects.filter(chapter__book__number=25)
    book_name = 'Lamentations'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def ezekiel(request):
    book = Verse.objects.filter(chapter__book__number=26)
    book_name = 'Ezekiel'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def daniel(request):
    book = Verse.objects.filter(chapter__book__number=27)
    book_name = 'Daniel'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def hosea(request):
    book = Verse.objects.filter(chapter__book__number=28)
    book_name = 'Hosea'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def joel(request):
    book = Verse.objects.filter(chapter__book__number=29)
    book_name = 'Joel'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def amos(request):
    book = Verse.objects.filter(chapter__book__number=30)
    book_name = 'Amos'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def obadiah(request):
    book = Verse.objects.filter(chapter__book__number=31)
    book_name = 'Obadiah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def jonah(request):
    book = Verse.objects.filter(chapter__book__number=32)
    book_name = 'Jonah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def micah(request):
    book = Verse.objects.filter(chapter__book__number=33)
    book_name = 'Micah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def nahum(request):
    book = Verse.objects.filter(chapter__book__number=34)
    book_name = 'Nahum'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def habakkuk(request):
    book = Verse.objects.filter(chapter__book__number=35)
    book_name = 'Habakkuk'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def zephaniah(request):
    book = Verse.objects.filter(chapter__book__number=36)
    book_name = 'Zephaniah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def haggai(request):
    book = Verse.objects.filter(chapter__book__number=37)
    book_name = 'Haggai'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def zechariah(request):
    book = Verse.objects.filter(chapter__book__number=38)
    book_name = 'Zechariah'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def malachi(request):
    book = Verse.objects.filter(chapter__book__number=39)
    book_name = 'Malachi'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def matthew(request):
    book = Verse.objects.filter(chapter__book__number=40)
    book_name = 'Matthew'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def mark(request):
    book = Verse.objects.filter(chapter__book__number=41)
    book_name = 'Mark'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def luke(request):
    book = Verse.objects.filter(chapter__book__number=42)
    book_name = 'Luke'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def john(request):
    book = Verse.objects.filter(chapter__book__number=43)
    book_name = 'John'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def acts(request):
    book = Verse.objects.filter(chapter__book__number=44)
    book_name = 'Acts'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def romans(request):
    book = Verse.objects.filter(chapter__book__number=45)
    book_name = 'Romans'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_corinthians(request):
    book = Verse.objects.filter(chapter__book__number=46)
    book_name = '1 Corinthians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_corinthians(request):
    book = Verse.objects.filter(chapter__book__number=47)
    book_name = '2 Corinthians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def galatians(request):
    book = Verse.objects.filter(chapter__book__number=48)
    book_name = 'Galatians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def ephesians(request):
    book = Verse.objects.filter(chapter__book__number=49)
    book_name = 'Ephesians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def philippians(request):
    book = Verse.objects.filter(chapter__book__number=50)
    book_name = 'Philippians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def colossians(request):
    book = Verse.objects.filter(chapter__book__number=51)
    book_name = 'Colossians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_thessalonians(request):
    book = Verse.objects.filter(chapter__book__number=52)
    book_name = '1 Thessalonians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_thessalonians(request):
    book = Verse.objects.filter(chapter__book__number=53)
    book_name = '2 Thessalonians'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_timothy(request):
    book = Verse.objects.filter(chapter__book__number=54)
    book_name = '1 Timothy'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_timothy(request):
    book = Verse.objects.filter(chapter__book__number=55)
    book_name = '2 Timothy'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def titus(request):
    book = Verse.objects.filter(chapter__book__number=56)
    book_name = 'Titus'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def philemon(request):
    book = Verse.objects.filter(chapter__book__number=57)
    book_name = 'Philemon'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def hebrews(request):
    book = Verse.objects.filter(chapter__book__number=58)
    book_name = 'Hebrews'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def james(request):
    book = Verse.objects.filter(chapter__book__number=59)
    book_name = 'James'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_peter(request):
    book = Verse.objects.filter(chapter__book__number=60)
    book_name = '1 Peter'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_peter(request):
    book = Verse.objects.filter(chapter__book__number=61)
    book_name = '2 Peter'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def first_john(request):
    book = Verse.objects.filter(chapter__book__number=62)
    book_name = '1 John'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def second_john(request):
    book = Verse.objects.filter(chapter__book__number=63)
    book_name = '2 John'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def third_john(request):
    book = Verse.objects.filter(chapter__book__number=64)
    book_name = '3 John'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def jude(request):
    book = Verse.objects.filter(chapter__book__number=65)
    book_name = 'Jude'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


def revelation(request):
    book = Verse.objects.filter(chapter__book__number=66)
    book_name = 'Revelation'
    one_quarter = len(book) // 4
    one_half = len(book) // 2
    three_quarters = len(book)*3 // 4 
    context = {
        'book': book,
        'book_name': book_name,
        'one_quarter': one_quarter,
        'one_half': one_half,
        'three_quarters': three_quarters
        }
    return render(request, "bible/book.html", context)


