# Generated by Django 4.0 on 2022-02-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_alter_logradouro_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='lote',
            field=models.CharField(max_length=10),
        ),
    ]
