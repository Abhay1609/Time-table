# Generated by Django 4.1.2 on 2023-03-04 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_profile_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]