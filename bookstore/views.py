from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register/signup.html'
