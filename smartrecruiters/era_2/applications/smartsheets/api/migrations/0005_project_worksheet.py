# Generated by Django 2.1.7 on 2019-03-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190306_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='worksheet',
            field=models.CharField(max_length=128, null=True, verbose_name='Worksheet Name'),
        ),
    ]
