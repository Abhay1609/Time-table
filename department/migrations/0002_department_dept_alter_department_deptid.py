# Generated by Django 4.1.2 on 2023-03-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dept',
            field=models.CharField(default='Computer Science & Engineering', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='deptid',
            field=models.IntegerField(unique=True),
        ),
    ]
