# Generated by Django 4.1.2 on 2023-03-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_subject'),
        ('account', '0008_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.ManyToManyField(to='department.subject'),
        ),
    ]
