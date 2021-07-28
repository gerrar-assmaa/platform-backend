# Generated by Django 3.1.2 on 2021-07-28 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210728_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='email_perso',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='email_perso',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='details_add_societe',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='email_encadrant',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='telephone_encadrant',
            field=models.CharField(blank=True, default=None, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]