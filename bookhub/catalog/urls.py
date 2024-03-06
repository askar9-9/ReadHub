from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/book/<slug:book_slug>', views.book, name='book'),
]