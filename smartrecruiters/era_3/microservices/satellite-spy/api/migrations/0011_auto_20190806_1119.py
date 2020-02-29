# Generated by Django 2.2.1 on 2019-08-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190716_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalinsight',
            name='category',
        ),
        migrations.RemoveField(
            model_name='historicalinsight',
            name='type',
        ),
        migrations.RemoveField(
            model_name='historicalresource',
            name='file',
        ),
        migrations.RemoveField(
            model_name='historicalresource',
            name='name',
        ),
        migrations.RemoveField(
            model_name='historicalresource',
            name='uploaded',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='category',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='type',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='file',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='name',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='uploaded',
        ),
        migrations.AddField(
            model_name='historicalinsight',
            name='status',
            field=models.CharField(default='approved', max_length=64, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='historicalresource',
            name='description',
            field=models.TextField(default='', max_length=32000, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='historicalresource',
            name='status',
            field=models.CharField(default='approved', max_length=64, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='historicalresource',
            name='title',
            field=models.CharField(default='New Resource', max_length=256, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='insight',
            name='status',
            field=models.CharField(default='approved', max_length=64, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.TextField(default='', max_length=32000, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='resource',
            name='status',
            field=models.CharField(default='approved', max_length=64, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(default='New Resource', max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='historicalinsight',
            name='description',
            field=models.TextField(default='', max_length=32000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalinsight',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='historicalinsight',
            name='title',
            field=models.CharField(default='New Insight', max_length=64, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='historicalresource',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='insight',
            name='description',
            field=models.TextField(default='', max_length=32000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='insight',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='insight',
            name='title',
            field=models.CharField(default='New Insight', max_length=64, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
    ]
