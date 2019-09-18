from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'posts/home.html'
class TosView(TemplateView):
    template_name = 'Termsofuse.html'
class PrivacyPolicyView(TemplateView):
    template_name = 'Privacypolicy.html'
