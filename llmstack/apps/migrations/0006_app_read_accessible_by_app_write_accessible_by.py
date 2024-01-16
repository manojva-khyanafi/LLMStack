# Generated by Django 4.2.1 on 2023-09-07 03:18

import django.contrib.postgres.fields
from django.db import connection, migrations, models

from llmstack.common.utils.db_models import ArrayField


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_appdata_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='read_accessible_by',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=320),
                blank=True,
                default=list,
                help_text='List of user emails or domains who can access the app',
                size=None) if connection.vendor == 'postgresql' else ArrayField(
                null=True,
                help_text='List of user emails or domains who can access the app',
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name='app',
            name='write_accessible_by',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=320),
                blank=True,
                default=list,
                help_text='List of user emails or domains who can modify the app',
                size=None) if connection.vendor == 'postgresql' else ArrayField(
                null=True,
                help_text='List of user emails or domains who can modify the app',
                blank=True,
            ),
        ),
    ]
