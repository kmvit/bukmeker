from django.contrib import admin
from forecasts.models import *
# Register your models here.

class ForecastAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Forecast, ForecastAdmin)
admin.site.register(UserID)
