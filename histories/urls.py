from django.conf.urls import url
from django.urls import path
from .views import *
urlpatterns = [
    path('', HistoryList.as_view(), name='histories'),
    path('<slug:slug>/', HistoryDetail.as_view(), name='history'),
]
