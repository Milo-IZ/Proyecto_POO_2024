# Generated by Django 5.1 on 2024-08-22 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('año', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo_usurio', models.EmailField(max_length=254)),
                ('psswd', models.CharField(max_length=255)),
                ('rol', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('correo_usurio', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('año', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('contenido', models.TextField()),
                ('fuentes', models.TextField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.materia')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador', models.IntegerField()),
                ('motivo', models.TextField()),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.contenido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Votar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador', models.IntegerField()),
                ('valido', models.BooleanField()),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.contenido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario')),
            ],
        ),
    ]
