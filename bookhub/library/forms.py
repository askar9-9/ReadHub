from django import forms
from library.models import Library


class StatusForm(forms.Form):
    CHOICES = (
        ('ALL', '---------------'),
        ('RG', 'Читаю'),
        ('PG', 'Планирую'),
        ('RD', 'Прочитано'),
        ('PD', 'Отложено'),
    )
    status_field = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


class LibraryForm(forms.ModelForm):
    status = forms.ChoiceField( choices=Library.Status.choices,
                                widget=forms.Select(attrs={'class': 'form-select form-select-sm'}),
                                label="Статус")
    pages_read = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min' : '0'}), label="Прочитано")

    class Meta:
        model = Library
        fields = ['status', 'pages_read']