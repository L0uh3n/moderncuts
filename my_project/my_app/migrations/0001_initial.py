# Generated by Django 4.1.1 on 2022-11-29 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=100)),
                ('num_telefone', models.CharField(max_length=15)),
                ('data', models.DateField()),
                ('hora', models.CharField(max_length=120)),
                ('observacoes', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=120)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('usuario', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=30)),
                ('num_telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='servicos_agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.agendamento')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.servicos')),
            ],
        ),
        migrations.AddField(
            model_name='servicos',
            name='preenchido',
            field=models.ManyToManyField(through='my_app.servicos_agendamento', to='my_app.agendamento'),
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=254)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='agendamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.usuario'),
        ),
    ]
