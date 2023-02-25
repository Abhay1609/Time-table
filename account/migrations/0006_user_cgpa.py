# Generated by Django 4.1.2 on 2023-02-12 07:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cgpa',
            field=models.FloatField(default=9.2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]
