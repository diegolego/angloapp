# Generated by Django 2.0.2 on 2018-03-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectos', '0011_auto_20180327_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospectorazon',
            name='tipo_accion',
        ),
        migrations.AddField(
            model_name='prospectorazon',
            name='tipo_accion',
            field=models.ManyToManyField(help_text='Selecciona la razón por la cuál abandonó', to='prospectos.Razon'),
        ),
    ]
