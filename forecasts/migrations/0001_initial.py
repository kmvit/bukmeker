# Generated by Django 2.0.6 on 2018-06-10 06:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('meta_title', models.CharField(max_length=70, verbose_name='meta_title')),
                ('meta_description', models.CharField(max_length=150, verbose_name='meta_description')),
                ('slug', models.SlugField(verbose_name='url статьи')),
                ('born', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('image', models.ImageField(blank=True, upload_to='articles', verbose_name='Изображение')),
                ('body', tinymce.models.HTMLField(verbose_name='Содержание')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Прогноз',
                'verbose_name_plural': 'Прогнозы',
            },
        ),
    ]
