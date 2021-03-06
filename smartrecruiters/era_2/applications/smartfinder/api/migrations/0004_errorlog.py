# Generated by Django 2.1.7 on 2019-03-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190306_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('traceback', models.TextField(blank=True,
                                               max_length=2048, null=True, verbose_name='Traceback')),
            ],
        ),
    ]
