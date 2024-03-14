from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from .models import Book, Author, Genre

# Create your views here.
def catalog(request):
    book_list = Book.objects.all()
    return render(request,'catalog/catalog.html', context={'book_list':book_list})

def book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    return render(request, 'catalog/book.html', context={'book': book})
