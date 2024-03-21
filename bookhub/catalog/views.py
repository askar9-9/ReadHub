from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from .models import Book, Author, Genre


# Create your views here.
class CatalogView(ListView):
    model = Book
    # путь к шаблону
    template_name = "catalog/catalog.html"
    # название переменной, которая используется в шаблоне
    context_object_name = 'book_list'


class BookView(DetailView):
    template_name = 'catalog/book.html'
    context_object_name = 'book'
    # название переменной, которая передается через urls.py
    slug_url_kwarg = 'book_slug'

    # этот извлекает объект из базы данных
    def get_object(self, queryset=None):
        return get_object_or_404(Book, slug=self.kwargs[self.slug_url_kwarg])
