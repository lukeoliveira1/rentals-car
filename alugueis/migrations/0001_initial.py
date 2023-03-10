# Generated by Django 4.1.7 on 2023-03-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_retirada', models.DateField()),
                ('data_entrega', models.DateField()),
                ('valor', models.FloatField()),
                ('carro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carros.carro')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.cliente')),
            ],
        ),
    ]
