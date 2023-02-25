# Generated by Django 4.1.2 on 2023-01-20 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(60)])),
                ('isverified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('password2', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]