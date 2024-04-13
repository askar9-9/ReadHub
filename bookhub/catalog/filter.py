from django import forms
from django_filters import FilterSet, CharFilter, MultipleChoiceFilter
from .models import Book, Genre


def get_choices_from_model():
    return [(i['id'], i['name_genre']) for i in Genre.objects.values()]


class CatalogFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',
                       widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название книги...'}),
                       required=False,
                       label="Поиск")
    genre = MultipleChoiceFilter(field_name='genre', choices=get_choices_from_model(),
                                 widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}), required=False,
                                 label="Жанры")

    class Meta:
        model = Book
        fields = ['title', 'genre']
