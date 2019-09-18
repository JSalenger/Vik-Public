from django.urls import path

from .views import HomePageView, TosView, PrivacyPolicyView
app_name = "pages"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tou/', TosView.as_view(), name='tos'),
    path('privacypolicy/', PrivacyPolicyView.as_view(), name='privacy')
]
