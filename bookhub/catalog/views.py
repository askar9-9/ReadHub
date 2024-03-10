from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from .models import Book, Author, Genre

# Create your views here.
def catalog(request):
    objects = Book.objects.all()
    data = {
        'objects': objects,
    }
    return render(request,'catalog/catalog.html', context=data)

def book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    data = {
        'title' : book.get_title(),
        'description' : book.get_description(),
        'img' : book.get_img_url(),
        'page_count' : book.get_page_count(),
        'genre' : book.get_genre(),
        'author' : book.get_author(),
    }
    return render(request, 'catalog/book.html', context={'book': data})
