# Generated by Django 3.2.7 on 2021-10-24 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myvlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='article',
        ),
    ]
