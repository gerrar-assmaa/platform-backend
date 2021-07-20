from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Rapport(models.Model):
    stage_ou_projet = models.BooleanField(default=True)
    date_debut_stage = models.DateField()
    date_fin_stage = models.DateField()
    intitulé_stage =models.CharField(max_length=200,blank=False, default='')
    société_stage =models.CharField(max_length=200,blank=False, default='')
    secteur_société =models.CharField(max_length=200,blank=False, default='')
    ville_société =models.CharField(max_length=200,blank=False, default='')
    pays_société =models.CharField(max_length=200,blank=False, default='')
    détails_add_société =models.CharField(max_length=200,blank=True)
    encadrant =models.CharField(max_length=200)
    email_encadrant = models.EmailField(max_length = 254)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    téléphone_encadrant = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    lien_rapport = models.URLField(max_length = 200)
    rapport_confidentiel = models.BooleanField(default=True)
#   fk_code_apogée