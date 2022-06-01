# Generated by Django 4.0.4 on 2022-05-31 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60, verbose_name='Título')),
                ('autor', models.CharField(max_length=60, verbose_name='Autor')),
                ('paginas', models.IntegerField(verbose_name='Numero de Páginas')),
                ('data_publicacao', models.DateField(verbose_name='Data de Publicação')),
                ('criacao_dados', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'livros',
            },
        ),
    ]
