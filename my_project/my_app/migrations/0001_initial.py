# Generated by Django 4.1.2 on 2022-10-27 14:13

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
                ('data_horario', models.DateTimeField()),
                ('observacoes', models.TextField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=50)),
                ('valor_servico', models.DecimalField(decimal_places=2, max_digits=5)),
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
                ('senha', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
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
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.servicos'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.usuario'),
        ),
    ]
