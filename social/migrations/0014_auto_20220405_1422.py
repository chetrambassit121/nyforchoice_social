# Generated by Django 3.2.9 on 2022-04-05 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
