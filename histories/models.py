from django.db import models
from tinymce.models import HTMLField
from articles.models import Author
from django.utils import timezone
# Create your models here.

class ClubHistory(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(verbose_name='url статьи')
    meta_description = models.CharField(max_length=150, verbose_name='meta_description')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='articles', verbose_name='Изображение', blank=True)
    body = HTMLField(verbose_name='Содержание')
    published = models.BooleanField(default=False, verbose_name='Опубликовать')
    class Meta:
        verbose_name='История клубов'
        verbose_name_plural='Истории клубов'
        ordering = ['born']

    def __str__(self):
        return self.title
