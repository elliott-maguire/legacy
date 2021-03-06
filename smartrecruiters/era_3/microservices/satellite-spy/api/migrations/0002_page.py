# Generated by Django 2.2.1 on 2019-07-09 21:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "datestamp",
                    models.DateField(auto_now_add=True, verbose_name="Datestamp"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(verbose_name="Page URL")),
                (
                    "content",
                    models.TextField(
                        default="", max_length=32000, verbose_name="Page Content"
                    ),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pages",
                        related_query_name="page",
                        to="api.Competitor",
                    ),
                ),
            ],
        )
    ]
