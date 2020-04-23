# Generated by Django 3.0.4 on 2020-04-22 17:50

import autoslug.fields
from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_es', models.CharField(max_length=255, null=True)),
                ('title_bn', models.CharField(max_length=255, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title')),
                ('slug_en', autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title')),
                ('slug_es', autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title')),
                ('slug_bn', autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title')),
                ('published', models.BooleanField()),
                ('content', martor.models.MartorField(blank=True, null=True)),
                ('content_en', martor.models.MartorField(blank=True, null=True)),
                ('content_es', martor.models.MartorField(blank=True, null=True)),
                ('content_bn', martor.models.MartorField(blank=True, null=True)),
                ('internal_notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]