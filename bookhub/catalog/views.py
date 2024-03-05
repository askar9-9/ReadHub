from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from .models import Book, Author

# Create your views here.
def index(request):
    objects = Book.objects.all()
    data = {
        'objects': objects,
    }
    return render(request,'main/index.html', context=data)

def book_details(request, book_slug):
    book = Book.objects.filter(slug=book_slug).values()[0]
    author = Author.objects.get(pk=book['author_id'])
    book['img'] = Book.objects.get(pk=book['id']).img.url
    return render(request, 'main/book_details.html', context={'book': book, 'author': author})
