# Generated by Django 3.2.18 on 2023-04-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0010_auto_20230401_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='crearCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20)),
                ('municipio', models.CharField(max_length=200)),
                ('tipoEstablecimiento', models.CharField(max_length=200)),
                ('nombreEstablecimiento', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('propietario', models.CharField(max_length=200)),
            ],
        ),
    ]