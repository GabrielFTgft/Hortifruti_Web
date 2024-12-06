# Generated by Django 5.1.3 on 2024-12-02 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
        ('usuarios', '0003_alter_cliente_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='atualizado_em',
        ),
        migrations.AddField(
            model_name='pedido',
            name='endereco',
            field=models.CharField(default='padrao', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.cliente'),
        ),
    ]