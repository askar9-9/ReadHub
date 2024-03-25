from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('book/<slug:book_slug>', views.BookView.as_view(), name='book'),
]