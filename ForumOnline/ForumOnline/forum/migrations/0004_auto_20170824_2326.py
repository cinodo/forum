# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170824_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens', to='forum.Topico', verbose_name='Tópico'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='mensagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='forum.Mensagem', verbose_name='Mensagem'),
        ),
    ]
