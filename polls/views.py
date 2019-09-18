#-*- coding: utf-8 -*-
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Choice, Poll, Voter
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import ChoiceForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy
# Create your views here.
def QuestionListView(request):
    template = 'polls/index.html'
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', '')
        object_list = Poll.objects.filter(Q(question__icontains=search_query))
    context = {
        'object_list': object_list
    }
    return render(request, template, context)

@login_required
def DetailView(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    template = 'polls/detail.html'
    if request.method == 'POST':
        # A Choice is being added
        choice_form = ChoiceForm(data=request.POST)
        if choice_form.is_valid():
            new_choice = choice_form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
    else:
        choice_form = ChoiceForm()
    context = {
        'poll': poll,
        'choice_form': choice_form,
    }
    return render(request, template, context)


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    template_name = 'polls/question_new.html'
    fields = ('question', 'description')
    success_url = reverse_lazy("polls:home")
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
@login_required(login_url='login')
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    voter =  Voter.objects.filter(poll_id=poll_id, user_id=request.user.id,)
    if voter:
        return render(request, 'polls/detail.html', {
        'poll': p,
        'error_message': "Sorry, but you have already voted."
        })
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
        'poll': p,
        'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        v = Voter(user = request.user, poll = p)
        v.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
