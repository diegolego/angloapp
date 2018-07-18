# Generated by Django 2.0.2 on 2018-03-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectos', '0015_auto_20180328_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospectorazon',
            name='tipo_razon',
        ),
        migrations.AddField(
            model_name='prospectorazon',
            name='tipo_razon',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='prospectos.Razon'),
        ),
    ]
