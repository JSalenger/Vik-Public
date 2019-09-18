import random
from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article, Comment
from django.core.mail import send_mail
from django.conf import settings
import operator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def ArticleListView(request):
    template = 'posts/article_list.html'
    try:
        query = request.GET.get('q')
        object_list = Article.objects.filter(Q(title__icontains=query))
    except:
        object_list = Article.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts
    }
    return render(request, template, context)
@login_required
def ArticleDetailView(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    template = 'posts/article_detail.html'
    if request.method == 'POST':
        # A Choice is being added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, template, context)
class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'posts/article_edit.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'posts/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'posts/article_new.html'
    fields = ['title', 'body', 'image',]
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
def search(request):
    template = 'posts/article_list.html'
    try:
        query = request.GET.get('q')
        object_list = Article.objects.filter(Q(title__icontains=query))
    except:
        object_list = Article.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts
    }
    return render(request, template, context)
