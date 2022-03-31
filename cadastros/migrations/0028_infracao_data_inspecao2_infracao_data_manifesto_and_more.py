# Generated by Django 4.0 on 2022-03-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0027_alter_defesa_options_reinspecao'),
    ]

    operations = [
        migrations.AddField(
            model_name='infracao',
            name='data_inspecao2',
            field=models.DateField(blank=True, null=True, verbose_name='Data da reinspeção'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='data_manifesto',
            field=models.DateField(blank=True, null=True, verbose_name='Data do manifesto'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='entrada_protocolo',
            field=models.DateField(blank=True, null=True, verbose_name='Data de entrada'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='foto_inspecao_2',
            field=models.FileField(blank=True, upload_to='fotos/', verbose_name='Foto da reinspeção'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='grau',
            field=models.CharField(blank=True, choices=[('PROPRIO', 'PROPRIO'), ('CORRESPONSAVEL', 'CORRESPONSAVEL'), ('OUTROS', 'OUTROS')], max_length=50, null=True, verbose_name='Grau de relação'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='horario_inspecao2',
            field=models.TimeField(blank=True, null=True, verbose_name='Horário de reinspeção'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='julgamento',
            field=models.DateField(blank=True, null=True, verbose_name='Data do julgamento'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='prazo_manifesto',
            field=models.DateField(blank=True, null=True, verbose_name='Prazo de manifesto'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='protocolo',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Protocolo de defesa'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='quem',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome de quem protocoloou'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='situacao',
            field=models.CharField(blank=True, choices=[('1', 'Defendeu e limpou'), ('2', 'Não defendeu e limpou'), ('3', 'Não defendeu e não limpou'), ('4', 'Defendeu fora do prazo e limpou')], max_length=25, null=True, verbose_name='Situação'),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='observacoes',
            field=models.CharField(blank=True, max_length=660, null=True),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='numero_format_ano',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Auto de Infração'),
        ),
        migrations.AlterField(
            model_name='reinspecao',
            name='situacao',
            field=models.CharField(choices=[('1', 'Defendeu e limpou'), ('2', 'Não defendeu e limpou'), ('3', 'Não defendeu e não limpou'), ('4', 'Defendeu fora do prazo e limpou')], max_length=25, verbose_name='Situação'),
        ),
    ]
