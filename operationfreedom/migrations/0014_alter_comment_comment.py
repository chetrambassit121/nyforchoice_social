# Generated by Django 3.2.9 on 2022-01-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationfreedom', '0013_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=225),
        ),
    ]
