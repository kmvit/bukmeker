from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from authors.models import Author
from articles.models import Article
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.db.models import F
# Create your views here.

class ForecastList(ListView):
    model = Forecast

class ForecastDetailView(DetailView):
    model = Forecast

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = Article.objects.filter(published=True)[:3]
        return context

def add_like(request, slug):
    forecast = Forecast.objects.get(slug=slug)
    user_list = forecast.user_id.all()
    if request.user:
        try:
            for item in user_list:
                if request.user.id == item.ids:
                    return redirect('forecast', slug=slug)
            else:
                forecast.like += 1
                forecast.save()

        except ObjectDoesNotExist:
            return Http404
            like_user = forecast.user_id.get_or_create(ids=request.user.id)
    else:
        return redirect('forecast', slug=slug)
    return redirect('forecast', slug=slug)


def add_dislike(request, slug):
    forecast = Forecast.objects.get(slug=slug)
    user_list = forecast.user_id.all()
    if request.user:
        try:
            for item in user_list:
                if request.user.id == item.ids:
                    return redirect('forecast', slug=slug)
            else:
                forecast.dislike += 1
                forecast.save()

        except ObjectDoesNotExist:
            return Http404
            like_user = forecast.user_id.get_or_create(ids=request.user.id)
    else:
        return redirect('forecast', slug=slug)
    return redirect('forecast', slug=slug)
