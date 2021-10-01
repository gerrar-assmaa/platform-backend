# Generated by Django 3.1.2 on 2021-09-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotCle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='rapport',
            name='mots',
            field=models.ManyToManyField(blank=True, related_name='fk_mot', to='main_app.MotCle'),
        ),
    ]