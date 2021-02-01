# Generated by Django 3.1.2 on 2021-01-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('correo2', models.EmailField(blank=True, max_length=100)),
                ('telefono', models.IntegerField()),
                ('telefono2', models.IntegerField(default='809-221-3041')),
                ('telefono3', models.IntegerField(default='809-968-9333')),
                ('url_facebook', models.URLField(blank=True)),
                ('url_twitter', models.URLField(blank=True)),
                ('url_instagram', models.URLField(blank=True)),
                ('url_linkedin', models.URLField(blank=True)),
                ('url_youtube', models.URLField(blank=True)),
                ('desc', models.TextField(verbose_name='Descripcion')),
                ('image1', models.ImageField(blank=True, upload_to='Agentes', verbose_name='Imagen 1')),
                ('image2', models.ImageField(blank=True, upload_to='Agentes', verbose_name='Imagen 2')),
                ('image3', models.ImageField(blank=True, upload_to='Agentes', verbose_name='Imagen 3')),
                ('image4', models.ImageField(blank=True, upload_to='Agentes', verbose_name='Imagen 4')),
                ('image5', models.ImageField(blank=True, upload_to='Agentes', verbose_name='Imagen 5')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Utilma modificacion')),
            ],
            options={
                'verbose_name': 'Agente',
                'verbose_name_plural': 'Agentes',
                'ordering': ['-created'],
            },
        ),
    ]