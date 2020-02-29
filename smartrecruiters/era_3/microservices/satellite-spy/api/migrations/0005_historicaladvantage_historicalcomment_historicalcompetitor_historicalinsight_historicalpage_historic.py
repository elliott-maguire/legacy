# Generated by Django 2.2.1 on 2019-07-10 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0004_auto_20190710_1222"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalResource",
            fields=[
                ("timestamp", models.DateTimeField(blank=True, editable=False)),
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Name")),
                (
                    "link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Link to Resource"
                    ),
                ),
                ("file", models.TextField(blank=True, max_length=100, null=True)),
                (
                    "uploaded",
                    models.BooleanField(default=False, verbose_name="Uploaded to S3?"),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="resource",
                        to="api.Competitor",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical resource",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalProperty",
            fields=[
                ("timestamp", models.DateTimeField(blank=True, editable=False)),
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Name"
                    ),
                ),
                ("content", models.TextField(max_length=32000, verbose_name="Content")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="property",
                        to="api.Competitor",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical property",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalPage",
            fields=[
                (
                    "datestamp",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Datestamp"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
                    ),
                ),
                ("url", models.URLField(verbose_name="Page URL")),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        max_length=32000,
                        null=True,
                        verbose_name="Page Content",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="page",
                        to="api.Competitor",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical page",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalInsight",
            fields=[
                (
                    "timestamp",
                    models.DateTimeField(
                        blank=True, editable=False, verbose_name="Timestamp"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
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
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="insight",
                        to="api.Competitor",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical insight",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalCompetitor",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                ("website", models.URLField(verbose_name="Website")),
                (
                    "description",
                    models.TextField(max_length=32000, verbose_name="Description"),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical competitor",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalComment",
            fields=[
                ("timestamp", models.DateTimeField(blank=True, editable=False)),
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
                    ),
                ),
                ("content", models.TextField(max_length=2048, verbose_name="Content")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "insight",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="comment",
                        to="api.Insight",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical comment",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalAdvantage",
            fields=[
                (
                    "datestamp",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Datestamp"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Title")),
                ("script", models.TextField(max_length=2048, verbose_name="Content")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "competitor",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="advantage",
                        to="api.Competitor",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical advantage",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
