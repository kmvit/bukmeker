from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from authors.models import Author

class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(verbose_name='url категории')
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, default=1)
    slug = models.SlugField(verbose_name='url статьи')
    meta_description = models.CharField(max_length=150, verbose_name='meta_description', blank=True)
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='articles', verbose_name='Изображение', blank=True)
    body = HTMLField(verbose_name='Содержание')
    published = models.BooleanField(default=False, verbose_name='Опубликовать')
    premium = models.BooleanField(default=False, verbose_name='В большом блоке на главной')
    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'
        ordering = ['-born']

    def __str__(self):
        return self.title
