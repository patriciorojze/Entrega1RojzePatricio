# Generated by Django 4.1 on 2022-09-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaApp', '0003_alter_paciente_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Genero',
            field=models.CharField(max_length=10),
        ),
    ]
