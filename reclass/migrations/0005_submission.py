# Generated by Django 3.2.9 on 2021-11-25 09:19

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reclass', '0004_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=True)),
                ('attachments', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None)),
                ('submission_note', models.TextField(blank=True, null=True)),
                ('instructor_remark', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='reclass.assignment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submitted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'submissions',
                'unique_together': {('user', 'assignment')},
            },
        ),
    ]
