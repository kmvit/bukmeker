# Generated by Django 2.0.6 on 2018-06-15 00:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180614_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата игры'),
        ),
    ]
