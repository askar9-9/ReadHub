from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Genre(models.Model):
    name_genre = models.CharField(max_length=50, verbose_name='Название Жанра')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name_genre']

    def __str__(self):
        return str(self.name_genre)


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')

    class Meta:
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    img = models.ImageField(upload_to='book_images/', blank=True, verbose_name='Изображения',
                            default="book_images/none.jpg")
    page_count = models.IntegerField(verbose_name='Количество страниц')
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')
    release_date = models.DateField(default=timezone.now, verbose_name='Дата выпуска')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    author = models.ManyToManyField(Author, verbose_name='Автор')

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"

    def get_absolute_url(self):
        return reverse("catalog:book", kwargs={"book_slug": self.slug})

    def __str__(self):
        return str(self.title)
