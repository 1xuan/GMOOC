# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180207_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='课程机构'),
        ),
    ]
