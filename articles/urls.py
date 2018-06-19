from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleList.as_view(), name='articles'),
    path('<slug:slug>/', ArticleDetail.as_view(), name='article'),
]
