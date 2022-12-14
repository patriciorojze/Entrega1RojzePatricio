# Generated by Django 4.1 on 2022-08-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.IntegerField()),
                ('CodigoPlan', models.CharField(max_length=15)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.IntegerField()),
                ('NroMedico', models.IntegerField()),
                ('FechaHora', models.DateTimeField()),
                ('Cancelada', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoEspecialidad', models.IntegerField()),
                ('NombreEspecialidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NroMedico', models.IntegerField()),
                ('DNI', models.IntegerField()),
                ('FechaNota', models.DateTimeField()),
                ('Notas', models.CharField(max_length=1600)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NroMedico', models.IntegerField()),
                ('Nombre', models.CharField(max_length=45)),
                ('Apellido', models.CharField(max_length=45)),
                ('CodigoEspecialidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('DNI', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('Apellido', models.CharField(max_length=45)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=60)),
                ('Telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoPlan', models.CharField(max_length=15)),
                ('FechaPago', models.DateField()),
                ('Monto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('CodigoPlan', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('FechaAfiliacion', models.DateField()),
                ('TipoPlan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPlan',
            fields=[
                ('NroPlan', models.IntegerField(primary_key=True, serialize=False)),
                ('NombrePlan', models.CharField(max_length=30)),
                ('MaxPersonas', models.IntegerField()),
            ],
        ),
    ]
