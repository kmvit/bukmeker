from django.contrib import admin
from histories.models import *
# Register your models here.

class ClubHistoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(ClubHistory,ClubHistoryAdmin)
