# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('1', 'Python'), ('2', 'HTML5'), ('3', 'JAVA')], default='1', max_length=10, null=True, verbose_name='\u5b66\u79d1')),
                ('type', models.CharField(choices=[('1', '\u9009\u62e9\u9898'), ('2', '\u7f16\u7a0b\u9898')], default='1', max_length=2, verbose_name='\u9898\u76ee\u7c7b\u578b')),
                ('score', models.CharField(max_length=10, verbose_name='\u5206\u6570')),
                ('level', models.CharField(max_length=10, verbose_name='\u96be\u5ea6\u7cfb\u6570')),
                ('title', models.TextField(null=True, verbose_name='\u9898\u76ee\u6807\u9898')),
                ('sub_title', models.TextField(null=True, verbose_name='\u9898\u76ee\u9009\u9879')),
                ('answer', models.CharField(max_length=50, verbose_name='\u7b54\u6848')),
                ('ques_ext', models.CharField(max_length=255, null=True, verbose_name='\u5176\u4ed6')),
            ],
            options={
                'verbose_name': '\u9898\u76ee',
                'verbose_name_plural': '\u9898\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('ques_id', models.CharField(max_length=10, verbose_name='\u9898\u76ee\u5e8f\u53f7')),
                ('status', models.CharField(max_length=10, null=True, verbose_name='\u7b54\u9898\u72b6\u6001')),
                ('score', models.CharField(max_length=10, null=True, verbose_name='\u5206\u6570')),
                ('times', models.CharField(max_length=10, null=True, verbose_name='\u8003\u8bd5\u6b21\u6570')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bb0\u5f55',
                'verbose_name_plural': '\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('class_name', models.CharField(max_length=10, verbose_name='\u6240\u5c5e\u73ed\u7ea7')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
            },
        ),
    ]
