from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('book/<slug:book_slug>', views.book, name='book'),
]