# Generated by Django 3.2.9 on 2021-11-28 19:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclass', '0008_alter_notification_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=None),
        ),
    ]
