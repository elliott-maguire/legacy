# Generated by Django 2.1.7 on 2019-03-16 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190316_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endpoint',
            name='auth',
        ),
    ]
