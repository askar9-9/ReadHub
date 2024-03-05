from django.urls import path
from . import views

urlpatterns = [
    path('book/<slug:book_slug>', views.book_details, name='book_details'),
]