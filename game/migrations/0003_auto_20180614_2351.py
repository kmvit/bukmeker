# Generated by Django 2.0.6 on 2018-06-14 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20180614_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Игры', 'verbose_name_plural': 'Игра'},
        ),
        migrations.RemoveField(
            model_name='game',
            name='forecast',
        ),
    ]
