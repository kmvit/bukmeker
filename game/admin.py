from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ['command_a','command_b','game_date',]
# Register your models here.
admin.site.register(Game, GameAdmin)
