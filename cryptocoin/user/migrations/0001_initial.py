# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.CharField(max_length=100)),
                ('answer2', models.CharField(max_length=100)),
                ('answer3', models.CharField(max_length=100)),
                ('was_hacked', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='useranswers',
            name='userdata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserData'),
        ),
    ]
