from django import forms
from .models import Genre

def get_choices_from_model():
    return [(i['id'], i['name_genre']) for i in Genre.objects.values()]

class FilterForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Название книги...'}), 
        required=False,
        label="Поиск"
        )
    genre = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check'}),
        choices=get_choices_from_model(),
        label="Жанры",
        required=False
        )
