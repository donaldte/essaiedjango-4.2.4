# Generated by Django 4.2.4 on 2023-08-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_produit_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='nom',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
