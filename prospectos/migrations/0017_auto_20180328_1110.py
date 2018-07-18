# Generated by Django 2.0.2 on 2018-03-28 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prospectos', '0016_auto_20180328_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospectorazon',
            name='tipo_razon',
        ),
        migrations.AddField(
            model_name='prospectorazon',
            name='tipo_accion',
            field=models.ForeignKey(help_text='Selecciona la razón principal de desinterés', null=True, on_delete=django.db.models.deletion.SET_NULL, to='prospectos.Razon'),
        ),
    ]