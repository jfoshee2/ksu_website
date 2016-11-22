from django.shortcuts import render, get_object_or_404
from .models import Book, Course


def index(request):
    #used to connect to the database
    all_books = Book.objects.all()
    return render(request, 'search/index.html', {'all_books': all_books})


def detail(request, book_id):
    # book = Book.objects.get(pk = book_id)
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'search/detail.html', {'book': book})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        selected_book = book.book_set.get(pk=request.POST['book'])
    except(KeyError, Book.DoesNotExist):
        return render(request, 'search/detail.html', {
            'book': book,
            'error_message': "You did not select a valid book"
        })
    else:
        selected_book.in_cart = True
        selected_book.save()
        return render(request, 'search/detail.html', {'book': book})

