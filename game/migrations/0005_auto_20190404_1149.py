# Generated by Django 2.0.6 on 2019-04-04 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_game_game_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-game_date'], 'verbose_name': 'Игры', 'verbose_name_plural': 'Игра'},
        ),
    ]