# Generated by Django 3.1.2 on 2021-02-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20210120_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='telefono3',
        ),
        migrations.AlterField(
            model_name='agent',
            name='telefono2',
            field=models.PositiveIntegerField(default='8099689333'),
        ),
    ]