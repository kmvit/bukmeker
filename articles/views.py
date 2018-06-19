from django.shortcuts import render,get_object_or_404, redirect
from articles.models import Article
from authors.models import Author
from forecasts.models import Forecast
from histories.models import ClubHistory
from game.models import Game
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    article_list_premium = Article.objects.filter(published=True, premium=True)
    article_list = Article.objects.filter(published=True, premium=False)
    forecast_list = Forecast.objects.filter(published=True)
    game_list = Game.objects.all()
    history_list = ClubHistory.objects.all()
    context = {'history_list':history_list, 'game_list':game_list,'forecast_list':forecast_list, 'article_list':article_list, 'article_list_premium':article_list_premium}
    return render(request, 'home.html', context)

class ArticleList(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forecast_list'] = Forecast.objects.filter(published=True)
        return context

class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forecast_list'] = Forecast.objects.filter(published=True)
        return context
