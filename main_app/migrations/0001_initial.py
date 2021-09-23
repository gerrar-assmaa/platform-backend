# Generated by Django 3.1.2 on 2021-09-22 11:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_etudiant', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('nom_prenom', models.CharField(default='', max_length=200)),
                ('prenom', models.CharField(default='', max_length=200)),
                ('nom', models.CharField(default='', max_length=200)),
                ('email_perso', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('email_pro', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('telephone', models.CharField(blank=True, default=None, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('filiere', models.CharField(default='', max_length=200)),
                ('promotion', models.CharField(default='', max_length=4)),
                ('fk_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_form', models.CharField(default='', max_length=200)),
                ('active_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_ou_projet', models.BooleanField(default=True)),
                ('date_debut_stage', models.DateField(blank=True, default=None, null=True)),
                ('date_fin_stage', models.DateField(blank=True, default=None, null=True)),
                ('type_rapport', models.CharField(default='', max_length=200)),
                ('resume_rapport', models.CharField(blank=True, default=None, max_length=3000, null=True)),
                ('intitule_stage', models.CharField(default='', max_length=200)),
                ('societe_stage', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('secteur_societe', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ville_societe', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pays_societe', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('details_add_societe', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('encadrant', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('email_encadrant', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('telephone_encadrant', models.CharField(blank=True, default=None, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('fichier_rapport', models.FileField(default='', upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('rapport_confidentiel', models.BooleanField(default=False)),
                ('valid_admin', models.BooleanField(default=False)),
                ('fk_etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prenom', models.CharField(default='', max_length=200)),
                ('prenom', models.CharField(default='', max_length=200)),
                ('nom', models.CharField(default='', max_length=200)),
                ('email_perso', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('email_pro', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, default=None, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('departement', models.CharField(default='', max_length=200)),
                ('fk_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Insertion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cursus_post_ensam', models.CharField(default='', max_length=200)),
                ('univ', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pays', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('nature_formation', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('intit_formation', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('intit_poste', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('societe', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ville', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_integration', models.DateField(blank=True, default=None, null=True)),
                ('fk_etudiant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.etudiant')),
            ],
        ),
    ]
