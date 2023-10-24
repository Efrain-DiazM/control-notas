# Generated by Django 3.2.18 on 2023-04-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0012_delete_crearcurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='crearCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCurso', models.CharField(max_length=10)),
                ('nombreCurso', models.CharField(max_length=30)),
                ('numeroCreditos', models.CharField(max_length=3)),
                ('tipoPrograma', models.CharField(max_length=10)),
                ('programaPertenece', models.CharField(max_length=30)),
                ('semestre', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
