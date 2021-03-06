# Generated by Django 2.1 on 2018-10-29 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsActive', models.BooleanField(default=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobhunt.Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsActive', models.BooleanField(default=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('salary', models.CharField(blank=True, max_length=120, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('headline', models.CharField(blank=True, max_length=120, null=True)),
                ('age', models.CharField(blank=True, max_length=120, null=True)),
                ('facebook', models.CharField(blank=True, max_length=120, null=True)),
                ('google', models.CharField(blank=True, max_length=120, null=True)),
                ('pintrest', models.CharField(blank=True, max_length=120, null=True)),
                ('twitter', models.CharField(blank=True, max_length=120, null=True)),
                ('git', models.CharField(blank=True, max_length=120, null=True)),
                ('instagram', models.CharField(blank=True, max_length=120, null=True)),
                ('youtube', models.CharField(blank=True, max_length=120, null=True)),
                ('dribbble', models.CharField(blank=True, max_length=120, null=True)),
                ('identity', models.OneToOneField(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
