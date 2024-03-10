from django.db import models
from django.utils import timezone
# Create your models here.

class Genre(models.Model):
    name_genre = models.CharField(max_length=50, verbose_name = 'Название Жанра')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self) -> str:
        return self.name_genre
    

class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name = 'Имя')
    last_name = models.CharField(max_length=50, verbose_name = 'Фамилия')

    class Meta:
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    img = models.ImageField(upload_to='book_images/', blank=True, verbose_name='Изображения', default="book_images/none.jpg")
    page_count = models.IntegerField(verbose_name = 'Количество страниц')
    date_added = models.DateTimeField(default=timezone.now, verbose_name = 'Дата добавления')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Автор')

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description

    def get_img_url(self):
        return self.img.url
    
    def get_page_count(self):
        return self.page_count

    def get_genre(self):
        return self.genre.values()[0]['name_genre'] 

    def get_author(self):
        return self.author
    
    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"
    
    def __str__(self) -> str:
        return self.title