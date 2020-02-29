# Generated by Django 2.1.7 on 2019-03-06 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default='', verbose_name='Sheet URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default='requested', max_length=32, verbose_name='Status'),
        ),
    ]