# Generated by Django 4.1.7 on 2023-03-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=15)),
                ('rg', models.CharField(max_length=12)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('numero_cnh', models.CharField(max_length=50)),
            ],
        ),
    ]
