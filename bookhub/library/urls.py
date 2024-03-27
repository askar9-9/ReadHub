from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library_view, name='library'),
    path('tracker/<slug:book_slug>', views.book_tracker_view, name='tracker'),
    path('add_book/<slug:book_slug>', views.add_book, name='add_book'),
    path('delete_book/<slug:book_slug>', views.delete_book, name='delete_book'),
]