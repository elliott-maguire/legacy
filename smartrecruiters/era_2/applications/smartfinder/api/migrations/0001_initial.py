# Generated by Django 2.1.5 on 2019-02-28 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(
                    auto_now=True, verbose_name='Date Added')),
                ('sfid', models.CharField(max_length=32, verbose_name='Salesforce ID')),
                ('doid', models.CharField(blank=True, max_length=256,
                                          null=True, verbose_name='DiscoverOrg ID')),
                ('prep', models.CharField(blank=True, max_length=64,
                                          null=True, verbose_name='Prospecting Rep')),
                ('status', models.CharField(default='enrich',
                                            max_length=16, verbose_name='Status')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('domain', models.URLField(verbose_name='Domain')),
                ('phone', models.CharField(blank=True, max_length=64,
                                           null=True, verbose_name='Office Phone')),
                ('hierarchy', models.TextField(blank=True, max_length=65536,
                                               null=True, verbose_name='Org Hierarchy')),
                ('insight', models.TextField(blank=True,
                                             max_length=2048, null=True, verbose_name='Insight')),
                ('summary', models.TextField(blank=True, max_length=256,
                                             null=True, verbose_name='Enrichment Summary')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('sfid', models.CharField(blank=True, max_length=32,
                                          null=True, verbose_name='Salesforce ID')),
                ('doid', models.CharField(blank=True, max_length=256,
                                          null=True, verbose_name='DiscoverOrg ID')),
                ('ctype', models.CharField(default='new',
                                           max_length=16, verbose_name='Type')),
                ('status', models.CharField(default='enrich',
                                            max_length=16, verbose_name='Status')),
                ('patched', models.BooleanField(
                    default=False, verbose_name='Patched')),
                ('rating', models.CharField(blank=True, default=4,
                                            max_length=8, null=True, verbose_name='Rating')),
                ('priority', models.CharField(blank=True, default=6,
                                              max_length=8, null=True, verbose_name='Priority')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('title', models.CharField(blank=True, default='',
                                           max_length=128, null=True, verbose_name='Title')),
                ('email', models.EmailField(blank=True,
                                            max_length=254, null=True, verbose_name='Email')),
                ('office', models.CharField(blank=True, default='',
                                            max_length=32, null=True, verbose_name='Office Line')),
                ('direct', models.CharField(blank=True, default='',
                                            max_length=32, null=True, verbose_name='Direct Line')),
                ('mobile', models.CharField(blank=True, default='',
                                            max_length=32, null=True, verbose_name='Mobile Phone')),
                ('account', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
            ],
        ),
    ]