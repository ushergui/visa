# Generated by Django 4.0 on 2022-03-28 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0029_infracao_data_entrega_julgamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infracao',
            old_name='protocolo',
            new_name='protocolo_defesa',
        ),
    ]
