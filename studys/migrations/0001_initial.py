# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-07 02:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(verbose_name='Date published')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Methods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(verbose_name='Date published')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('categorys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studys.classification')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='categorys',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studys.classification'),
        ),
    ]