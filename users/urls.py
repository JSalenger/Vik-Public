from django.urls import path
from .views import SignUpView
from . import views
from django.conf.urls import url
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
