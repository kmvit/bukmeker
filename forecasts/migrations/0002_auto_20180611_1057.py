# Generated by Django 2.0.6 on 2018-06-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='dislike',
            field=models.IntegerField(default=0, verbose_name='Не нравится'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='like',
            field=models.IntegerField(default=0, verbose_name='Нравится'),
        ),
    ]