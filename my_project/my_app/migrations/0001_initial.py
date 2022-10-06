# Generated by Django 4.1.2 on 2022-10-06 14:33

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpf_field.models.CPFField(max_length=14, unique=True, verbose_name='cpf')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('usuario', models.CharField(max_length=30, unique=True)),
                ('senha', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('num_telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
