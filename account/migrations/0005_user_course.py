# Generated by Django 4.1.2 on 2023-02-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(default='B.TECH', max_length=10),
            preserve_default=False,
        ),
    ]