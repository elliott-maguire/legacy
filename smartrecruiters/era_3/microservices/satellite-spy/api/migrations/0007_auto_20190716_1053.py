# Generated by Django 2.2.1 on 2019-07-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190716_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='competitor',
        ),
        migrations.DeleteModel(
            name='HistoricalProperty',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]