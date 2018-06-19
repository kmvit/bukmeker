from django.db import models
from tinymce.models import HTMLField
from authors.models import Author
from django.utils import timezone
from game.models import Game
# Create your models here.

class UserID(models.Model):
    ids = models.IntegerField(default=0)

class Forecast(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    game = models.ForeignKey(Game, verbose_name='Игра', default=1, on_delete=models.CASCADE)
    meta_description = models.CharField(max_length=150, verbose_name='meta_description')
    slug = models.SlugField(verbose_name='url статьи')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='articles', verbose_name='Изображение', blank=True)
    body = HTMLField(verbose_name='Содержание')
    coefficient = models.CharField(max_length=300, verbose_name='Коэффициент', default='тотал меньше 2.5, коэфф. 1.65')
    published = models.BooleanField(default=False, verbose_name='Опубликовать')
    come_true = models.BooleanField(default=False, verbose_name='Сбылось или нет', blank=True)
    like = models.IntegerField(default=0, verbose_name='Нравится')
    dislike = models.IntegerField(default=0, verbose_name='Не нравится')
    user_id = models.ManyToManyField(UserID, blank=True,verbose_name='Список пользователей, которые оценили прогноз')

    class Meta:
        verbose_name='Прогноз'
        verbose_name_plural='Прогнозы'
        ordering = ['-born']


    def __str__(self):
        return self.title
