from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView,
    search,
)
urlpatterns = [
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/detail', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView, name='article_list'),
    path('<int:pk>/comment', CommentCreateView.as_view(), name='comment_create'),
    path(r'^results/$', search, name='search')
]
