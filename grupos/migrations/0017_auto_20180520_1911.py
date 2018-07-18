# Generated by Django 2.0.2 on 2018-05-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0016_remove_alumno_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.CharField(blank=True, choices=[('i', 'Inscrito'), ('p', 'Pre-inscrito')], default='p', help_text='Status del alumno', max_length=1),
        ),
    ]