# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 16:15
from __future__ import unicode_literals

import AutoGrade.models
import AutoGrade.storage
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=32)),
                ('description', models.TextField(default=None, max_length=512, null=True)),
                ('instructor_test', models.FileField(default=None, storage=AutoGrade.storage.OverwriteStorage(), upload_to=AutoGrade.models.assignment_directory_path)),
                ('student_test', models.FileField(default=None, storage=AutoGrade.storage.OverwriteStorage(), upload_to=AutoGrade.models.assignment_directory_path)),
                ('assignment_file', models.FileField(default=None, storage=AutoGrade.storage.OverwriteStorage(), upload_to=AutoGrade.models.assignment_directory_path)),
                ('total_points', models.IntegerField(default=25)),
                ('timeout', models.IntegerField(default=3)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='due date')),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('enroll_key', models.CharField(default=AutoGrade.models.enroll_key, max_length=8, unique=True)),
                ('course_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_pass', models.CharField(default=AutoGrade.models.submission_key, max_length=12)),
                ('courses', models.ManyToManyField(to='AutoGrade.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_file', models.FileField(upload_to=AutoGrade.models.submission_directory_path)),
                ('passed', models.IntegerField(default=0)),
                ('failed', models.IntegerField(default=0)),
                ('percent', models.FloatField(default=0)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Instructor'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Course'),
        ),
    ]
