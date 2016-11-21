from django.http import Http404
from django.shortcuts import render
from .models import Book


def index(request):
    #used to connect to the database
    all_books = Book.objects.all()
    return render(request, 'search/index.html', {'all_books': all_books})


def detail(request, book_id):
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'search/detail.html', {{'book': book}})
