from django.shortcuts import render
from .models import *
from articles.models import Article
from django.views.generic import ListView, DetailView
# Create your views here.

class HistoryList(ListView):
    model = ClubHistory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = Article.objects.filter(published=True)[:3]
        return context

class HistoryDetail(DetailView):
    model = ClubHistory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = Article.objects.filter(published=True)[:3]
        return context
