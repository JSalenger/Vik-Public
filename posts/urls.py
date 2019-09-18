from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    search,
)
urlpatterns = [
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    url(r'^(?P<article_id>\d+)/$', ArticleDetailView, name='article_detail'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView, name='article_list'),
    path(r'^results/$', search, name='search'),
    path(r'^results/$', search, name='search'),
]
