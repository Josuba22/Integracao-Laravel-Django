# Generated by Django 5.0.7 on 2024-08-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_produto_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='data_finalizacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
