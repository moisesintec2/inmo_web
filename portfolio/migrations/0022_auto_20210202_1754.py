# Generated by Django 3.1.2 on 2021-02-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_auto_20210202_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='moneda_mant',
            field=models.CharField(choices=[('P', 'Pesos'), ('D', 'Dolares')], default='P', max_length=1, verbose_name='Moneda de cuota de mantenimiento'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='piso',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Piso'),
        ),
    ]
