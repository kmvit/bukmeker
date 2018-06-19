from django.conf.urls import url
from django.urls import path
from .views import *
urlpatterns = [
    path('', ForecastList.as_view(), name='forecasts'),
    path('<slug:slug>', ForecastDetailView.as_view(), name='forecast'),
    path('<slug>/addlike/', add_like, name='add_like'),
    path('<slug>/adddislike/', add_dislike, name='add_dislike'),
]
