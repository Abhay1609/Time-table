# Generated by Django 4.1.2 on 2023-03-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_department_dept_alter_department_deptid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, unique=True)),
                ('sub_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
