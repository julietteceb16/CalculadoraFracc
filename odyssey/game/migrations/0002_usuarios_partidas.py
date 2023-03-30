# Generated by Django 4.1 on 2023-03-30 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Partidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=30)),
                ('minutos_jugados', models.CharField(max_length=30)),
                ('puntaje', models.CharField(max_length=30)),
                ('id_ususario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.usuarios')),
            ],
        ),
    ]
