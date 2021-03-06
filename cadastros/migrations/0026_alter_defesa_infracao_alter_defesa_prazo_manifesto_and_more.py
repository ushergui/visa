# Generated by Django 4.0 on 2022-03-07 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0025_alter_defesa_prazo_manifesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defesa',
            name='infracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.infracao', verbose_name='Auto de Infração'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='prazo_manifesto',
            field=models.DateField(blank=True, verbose_name='Prazo de manifesto'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='protocolo',
            field=models.CharField(max_length=12, verbose_name='Protocolo de defesa'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='quem',
            field=models.CharField(max_length=100, verbose_name='Nome de quem protocoloou'),
        ),
    ]
