# Generated by Django 4.0 on 2021-12-26 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cadastros', '0003_rename_complemento_correspondência_terreno_complemento_correspondencia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=280, verbose_name='Descrição')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
        ),
    ]
