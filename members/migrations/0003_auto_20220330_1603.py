# Generated by Django 3.2.9 on 2022-03-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20220330_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
