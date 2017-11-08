from django.shortcuts import render
from django.contrib.auth.views import login, logout, LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'chat/index.html'

class RegistrationView(CreateView):
    model = User
    template_name = 'chat/form.html'
    form_class = UserCreationForm
    success_url = '/index/'

class UserLoginView(LoginView):
    template_name = 'chat/form.html'

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')

