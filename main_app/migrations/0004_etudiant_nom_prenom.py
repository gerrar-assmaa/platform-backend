# Generated by Django 3.1.2 on 2021-08-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210822_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='nom_prenom',
            field=models.CharField(default='', max_length=200),
        ),
    ]