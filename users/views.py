from __future__ import unicode_literals
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'signup.html'
