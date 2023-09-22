# Generated by Django 4.2.4 on 2023-09-21 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.cours')),
            ],
        ),
    ]
