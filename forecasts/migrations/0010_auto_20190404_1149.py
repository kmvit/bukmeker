# Generated by Django 2.0.6 on 2019-04-04 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0009_remove_forecast_meta_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forecast',
            options={'ordering': ['-born'], 'verbose_name': 'Прогноз', 'verbose_name_plural': 'Прогнозы'},
        ),
    ]
