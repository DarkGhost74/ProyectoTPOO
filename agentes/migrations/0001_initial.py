# Generated by Django 5.2 on 2025-04-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidopaterno', models.CharField(db_column='apellidoPaterno', max_length=50, verbose_name='Apellido paterno')),
                ('apellidomaterno', models.CharField(db_column='apellidoMaterno', max_length=50, verbose_name='Apellido materno')),
                ('creado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de creado')),
                ('modificado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de modificado')),
            ],
            options={
                'verbose_name': 'Agente',
                'verbose_name_plural': 'Agentes',
                'db_table': 'agente',
                'ordering': ['-creado'],
                'managed': False,
            },
        ),
    ]
