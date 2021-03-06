# Generated by Django 2.2.1 on 2019-06-24 20:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Competitor",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                ("website", models.URLField(verbose_name="Website")),
                (
                    "description",
                    models.TextField(max_length=32000, verbose_name="Description"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Name")),
                ("timestamp", models.DateTimeField(auto_now=True)),
                (
                    "link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Link to Resource"
                    ),
                ),
                ("file", models.FileField(blank=True, null=True, upload_to="")),
                (
                    "uploaded",
                    models.BooleanField(default=False, verbose_name="Uploaded to S3?"),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resources",
                        related_query_name="resource",
                        to="api.Competitor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Name"
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now=True)),
                ("content", models.TextField(max_length=32000, verbose_name="Content")),
                (
                    "competitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="properties",
                        related_query_name="property",
                        to="api.Competitor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Insight",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, verbose_name="Title")),
                ("link", models.URLField(verbose_name="Link")),
                (
                    "description",
                    models.TextField(max_length=32000, verbose_name="Description"),
                ),
                ("type", models.CharField(max_length=64, verbose_name="Type")),
                ("category", models.CharField(max_length=64, verbose_name="Category")),
                (
                    "competitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="insights",
                        related_query_name="insight",
                        to="api.Competitor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now=True)),
                ("content", models.TextField(max_length=2048, verbose_name="Content")),
                (
                    "insight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        related_query_name="comment",
                        to="api.Insight",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Advantage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Title")),
                ("script", models.TextField(max_length=2048, verbose_name="Content")),
                (
                    "competitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="advantages",
                        related_query_name="advantage",
                        to="api.Competitor",
                    ),
                ),
            ],
        ),
    ]
