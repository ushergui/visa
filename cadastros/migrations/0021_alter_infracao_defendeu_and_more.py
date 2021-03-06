# Generated by Django 4.0 on 2022-02-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0020_alter_terreno_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='defendeu',
            field=models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=15, null=True, verbose_name='Apresentou defesa?'),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='status_protocolo',
            field=models.CharField(choices=[('ABERTO', 'ABERTO'), ('PENDENTE', 'PENDENTE'), ('AGUARDANDO EDITAL', 'AGUARDANDO EDITAL'), ('AGUARDANDO RETORNO DA AR', 'AGUARDANDO RETORNO DA AR'), ('FINALIZADO', 'FINALIZADO'), ('INSPECIONADO', 'INSPECIONADO'), ('PRAZO DE DEFESA AR', 'PRAZO DE DEFESA AR'), ('PRAZO DE DEFESA EDITAL', 'PRAZO DE DEFESA EDITAL'), ('PRAZO PARA JULGAMENTO AR', 'PRAZO PARA JULGAMENTO AR'), ('PRAZO DE JULGAMENTO EDITAL', 'PRAZO DE JULGAMENTO EDITAL')], max_length=26),
        ),
    ]
