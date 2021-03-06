# Generated by Django 4.0 on 2022-03-15 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0026_alter_defesa_infracao_alter_defesa_prazo_manifesto_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defesa',
            options={'ordering': ['prazo_manifesto']},
        ),
        migrations.CreateModel(
            name='Reinspecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inspecao2', models.DateField(verbose_name='Data da reinspeção')),
                ('horario_inspecao2', models.TimeField(verbose_name='Horário de reinspeção')),
                ('foto_inspecao_2', models.FileField(upload_to='fotos/', verbose_name='Foto da reinspeção')),
                ('data_manifesto', models.DateField(verbose_name='Data do manifesto')),
                ('situacao', models.CharField(choices=[('1', 'Defendeu e limpou'), ('2', 'Não defendeu e limpou'), ('3', 'Não defendeu e não limpou')], max_length=25, verbose_name='Situação')),
                ('defesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.defesa', verbose_name='Defesa')),
            ],
        ),
    ]
