from django.shortcuts import render
from django.contrib.auth.mixins import (

    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article, Comment
import operator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
# Create your views here.
def ArticleListView(request):
    template = 'article_list.html'
    query = ''
    object_list = Article.objects.filter(Q(title__icontains=query))
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment', 'article')
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
def search(request):
    template = 'article_list.html'
    query = request.GET.get('q')
    object_list = Article.objects.filter(Q(title__icontains=query))
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
