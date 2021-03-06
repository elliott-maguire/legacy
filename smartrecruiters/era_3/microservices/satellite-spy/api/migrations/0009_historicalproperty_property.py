# Generated by Django 2.2.1 on 2019-07-16 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_auto_20190716_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Name')),
                ('content', models.TextField(max_length=32000, verbose_name='Content')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', related_query_name='property', to='api.Competitor')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalProperty',
            fields=[
                ('timestamp', models.DateTimeField(blank=True, editable=False)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Name')),
                ('content', models.TextField(max_length=32000, verbose_name='Content')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('competitor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='property', to='api.Competitor')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical property',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
