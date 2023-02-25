# Generated by Django 4.1.2 on 2023-02-25 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_cgpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='user',
            name='course',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roll_number',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]