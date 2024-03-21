from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Логин',
                               error_messages={'required': 'Логин не заполнен!'})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Пароль',
                               error_messages={'required': 'Пароль не заполнен!'})

    class Meta:
        # Best practice
        model = get_user_model()
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Логин')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {
            'email': 'E-mail',
            'first_name': "Имя",
            'last_name': "Фамилия",
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Извините, пользователь с таким логином уже зарегистрирован.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже используется.")
        return email

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Введённые пароли не совпадают. Пожалуйста, попробуйте еще раз.")
        return self.cleaned_data['password1']
