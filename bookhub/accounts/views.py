from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm


# Create your views here.
class LoginAccount(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'Неправильный логин или пароль.')
        return self.render_to_response(self.get_context_data(form=form))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
