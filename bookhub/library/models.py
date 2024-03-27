
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from catalog.models import Book
# Create your models here.


class Library(models.Model):
    
    class Status(models.TextChoices):
        READING = 'RG', 'Читаю'
        PLANNING = 'PG', 'Планирую'
        READ = 'RD', 'Прочитано'
        POSTPONED = 'PD', 'Отложено'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='library_book')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PLANNING)
    pages_read = models.IntegerField(default=0, verbose_name='Прочитано')
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')
    
    class Meta:
        ordering = ['-date_added']
        indexes = [
            models.Index(fields=['-date_added'])
        ]