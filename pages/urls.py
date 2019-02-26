from django.urls import path

from .views import HomePageView, TosView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tos/', TosView.as_view(), name='tos')
]
