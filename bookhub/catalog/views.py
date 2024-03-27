from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet, Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from .models import Book, Author, Genre
from .forms import FilterForm

# Create your views here.
class CatalogView(ListView):
    model = Book
    # путь к шаблону
    template_name = "catalog/catalog.html"
    # название переменной, которая используется в шаблоне
    context_object_name = 'book_list'
    form_class = FilterForm

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)

        if form.is_valid():
            genre_choices = form.cleaned_data.get('genre')
            title_searching = form.cleaned_data.get('search')

            filters = {}
            if genre_choices:
                filters['genre__in'] = genre_choices
            if title_searching:
                filters['title__icontains'] = title_searching
            data = self.model.objects.filter(**filters)  # Unpack filters dictionary

            return render(self.request, self.template_name, {'form': self.form_class, 'book_list': data})

            
        return redirect('catalog:catalog')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем форму в контекст для использования в шаблоне
        context['form'] = self.form_class
        return context

class BookView(DetailView):
    template_name = 'catalog/book.html'
    context_object_name = 'book'
    # название переменной, которая передается через urls.py
    slug_url_kwarg = 'book_slug'
    # этот извлекает объект из базы данных
    def get_object(self, queryset=None):
        return get_object_or_404(Book, slug=self.kwargs[self.slug_url_kwarg])