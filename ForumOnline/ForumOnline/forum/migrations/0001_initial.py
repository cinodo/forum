# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
                'ordering': ['criado'],
            },
        ),
        migrations.CreateModel(
            name='resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('mensagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.mensagem')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'ordering': ['criado'],
            },
        ),
        migrations.CreateModel(
            name='topico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('texto', models.TextField(max_length=255, verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
                'ordering': ['titulo'],
            },
        ),
        migrations.AddField(
            model_name='mensagem',
            name='topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topico'),
        ),
    ]