from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, Max, Min, Count

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True)

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'

    def user_raking(self):
        likes = self.forecast_set.values_list('like', flat=True)
        dislikes = self.forecast_set.values_list('dislike', flat=True)
        return likes[0] - dislikes[0]

    def __str__(self):
        return self.user.username
