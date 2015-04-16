# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=b' ', max_length=31, null=True)),
                ('last_name', models.CharField(default=b' ', max_length=31, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(to='pgn_web.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=b' ', max_length=31)),
                ('last_name', models.CharField(default=b' ', max_length=31)),
                ('username', models.CharField(max_length=31, null=True)),
                ('password', models.CharField(max_length=31, null=True)),
                ('graduation_year', models.DateField(blank=True, null=True)),
                ('major', models.CharField(default=b'Undeclared', max_length=31)),
                ('linked_in', models.CharField(default=b'', max_length=255)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('authenticated', models.BooleanField(default=False)),
                ('access_token', models.CharField(default=b'', max_length=31)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='member',
            field=models.ForeignKey(to='pgn_web.User'),
        ),
        migrations.AddField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(to='pgn_web.Tag'),
        ),
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.ManyToManyField(to='pgn_web.User'),
        ),
    ]
