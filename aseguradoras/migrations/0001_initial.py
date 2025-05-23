# Generated by Django 5.2 on 2025-04-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('imagen', models.ImageField(upload_to='aseguradoras', verbose_name='Imagen')),
                ('creado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de creado')),
                ('modificado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de modificado')),
            ],
            options={
                'verbose_name': 'Aseguradora',
                'verbose_name_plural': 'Aseguradoras',
                'db_table': 'aseguradora',
                'ordering': ['-creado'],
                'managed': False,
            },
        ),
    ]
