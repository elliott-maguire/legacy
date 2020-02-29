# Generated by Django 2.2.1 on 2019-07-10 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("api", "0003_auto_20190710_1201")]

    operations = [
        migrations.AddField(
            model_name="advantage",
            name="datestamp",
            field=models.DateField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Datestamp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="insight",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Timestamp",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="resource",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
