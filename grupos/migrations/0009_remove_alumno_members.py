# Generated by Django 2.0.2 on 2018-05-16 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0008_auto_20180516_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='members',
        ),
    ]