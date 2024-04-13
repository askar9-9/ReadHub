from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name_genre']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    # Отображаемые данные
    list_display = ['title', 'slug', 'date_added']
    
    list_filter = ['genre']
    # Поисковик по книгам и описанием
    search_fields = ['title', 'description']
    # При написание title в django-admin, slug автоматический создаётся
    prepopulated_fields = {'slug': ('title',)}
    # Поисковой виджет. Упрощает поиск нужных данных при добавление новой книги.
    raw_id_fields = ['author', 'genre']

