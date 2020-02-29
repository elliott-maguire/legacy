# Generated by Django 2.1.7 on 2019-04-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_contact_cleaned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sfid',
            field=models.CharField(max_length=64, verbose_name='Salesforce ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='direct',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Direct Line'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='office',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Office Line'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sfid',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Salesforce ID'),
        ),
    ]
