# Generated by Django 4.1.2 on 2023-03-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptid', models.IntegerField(max_length=3, unique=True)),
            ],
        ),
    ]
