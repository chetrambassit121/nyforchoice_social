# Generated by Django 3.2.9 on 2022-02-04 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operationfreedom', '0017_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
