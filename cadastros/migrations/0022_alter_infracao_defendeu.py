# Generated by Django 4.0 on 2022-02-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0021_alter_infracao_defendeu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='defendeu',
            field=models.CharField(blank=True, choices=[('PENDENTE', 'PENDENTE'), ('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=15, null=True, verbose_name='Apresentou defesa?'),
        ),
    ]
