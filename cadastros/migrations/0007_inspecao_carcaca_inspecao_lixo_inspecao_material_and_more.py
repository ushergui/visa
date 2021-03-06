# Generated by Django 4.0 on 2022-01-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_fiscal_infracao_inspecao_protocolo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspecao',
            name='carcaca',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='inspecao',
            name='lixo',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='inspecao',
            name='material',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='inspecao',
            name='movel',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='inspecao',
            name='outro',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='inspecao',
            name='pneu',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='inspecao',
            name='entulho',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='inspecao',
            name='foto_inspecao_1',
            field=models.FileField(upload_to='fotos/'),
        ),
        migrations.AlterField(
            model_name='inspecao',
            name='mato',
            field=models.CharField(blank=True, choices=[('', 'NÃO.'), ('X', 'SIM,')], max_length=1, null=True),
        ),
    ]
