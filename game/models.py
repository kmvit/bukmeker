from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.

class Game(models.Model):
    """docstring for Game."""
    command_a = models.CharField(max_length=300, verbose_name='Команда А')
    command_b = models.CharField(max_length=300, verbose_name='Команда Б')
    score = models.CharField(max_length=10, verbose_name='Счет', blank=True)
    game_date = models.DateField(default=now, verbose_name='Дата игры')
    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игра'
        ordering = ['-game_date']

    def __str__(self):
        return self.command_a + '-' + self.command_b
