# Generated by Django 4.0 on 2022-01-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0015_alter_logradouro_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logradouro',
            name='tipo',
            field=models.CharField(choices=[('RUA', 'RUA'), ('AVENIDA', 'AVENIDA'), ('PRAÇA', 'PRAÇA'), ('BECO', 'BECO'), ('ALAMEDA', 'ALAMEDA'), ('ESTRADA', 'ESTRADA'), ('LARGO', 'LARGO'), ('PASSARELA', 'PASSARELA'), ('RODOVIA', 'RODOVIA'), ('SETOR', 'SETOR'), ('TRAVESSA', 'TRAVESSA'), ('TREVO', 'TREVO')], max_length=22),
        ),
    ]
