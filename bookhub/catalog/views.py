from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from .models import Book, Author

# Create your views here.
def catalog(request):
    objects = Book.objects.all()
    data = {
        'objects': objects,
    }
    return render(request,'catalog/catalog.html', context=data)

def book(request, book_slug):
    book = Book.objects.filter(slug=book_slug).values()[0]
    author = Author.objects.get(pk=book['author_id'])
    book['img'] = Book.objects.get(pk=book['id']).img.url
    return render(request, 'catalog/book.html', context={'book': book, 'author': author})
