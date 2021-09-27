from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.deletion import DO_NOTHING
from django_rest_passwordreset.signals import reset_password_token_created

#instantiate the storage on you models.py file before using into the models:
# from gdstorage.storage import GoogleDriveStorage

# # Define Google Drive Storage
# gd_storage = GoogleDriveStorage()

#OneToOne => one to one relationship
#foreignKey => one to many relationship
#ManyToMany => many to many relationship

class Professeur(models.Model):
    nom_prenom=models.CharField(max_length=200,blank=False, default='')#ADDED
    prenom = models.CharField(max_length=200,blank=False, default='')
    nom = models.CharField(max_length=200,blank=False, default='')
    email_perso = models.EmailField(max_length = 254, default=None, blank=True, null=True)
    email_pro = models.EmailField(max_length = 254)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")    
    telephone = models.CharField(validators = [phoneNumberRegex], max_length = 16, default=None, blank=True, null=True)
    departement = models.CharField(max_length=200,blank=False, default='')
    #one to one relationship (with utilisateur)
    fk_user = models.OneToOneField(User,on_delete=models.CASCADE,  default=None, blank=True, null=True)#CHANGED         

class Etudiant(models.Model):
    code_etudiant = models.CharField(max_length=200,default=None,blank=True, null=True)#CHANGED
    nom_prenom=models.CharField(max_length=200,blank=False, default='')#ADDED
    prenom = models.CharField(max_length=200,blank=False, default='')
    nom = models.CharField(max_length=200,blank=False, default='')
    email_perso = models.EmailField(max_length = 254, default=None, blank=True, null=True)
    email_pro = models.EmailField(max_length = 254,default=None, blank=True, null=True)#CHANGED
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")    
    telephone = models.CharField(validators = [phoneNumberRegex], max_length = 16, default=None, blank=True, null=True)
    filiere = models.CharField(max_length=200,blank=False, default='')
    promotion = models.CharField(max_length=4,blank=False, default='')
    #one to one relationship (with utilisateur)
    fk_user = models.OneToOneField(User,on_delete=models.CASCADE,default=None, blank=True, null=True)#CHANGED 

class Insertion(models.Model):
    cursus_post_ensam = models.CharField(max_length=200, blank=False, default='')
    univ = models.CharField(max_length=200, default=None, blank=True, null=True)
    pays= models.CharField(max_length=200, default=None, blank=True, null=True)
    nature_formation = models.CharField(max_length=200, default=None, blank=True, null=True)
    intit_formation = models.CharField(max_length=200, default=None, blank=True, null=True)
    intit_poste = models.CharField(max_length=200, default=None, blank=True, null=True)
    societe = models.CharField(max_length=200, default=None, blank=True, null=True)
    ville = models.CharField(max_length=200, default=None, blank=True, null=True)
    date_integration = models.DateField(default=None, blank=True, null=True)
    #one to one relationship (with Etudiant)
    #nom_prenom=models.CharField(max_length=200,blank=False, default='')#ADDED
    fk_etudiant = models.OneToOneField(Etudiant,on_delete=models.CASCADE)    

class Rapport(models.Model):
    horodateur = models.DateField(default=None)#CHANGED
    stage_ou_projet = models.BooleanField(default=True)
    date_debut_stage = models.DateField(default=None, blank=True, null=True)#CHANGED
    date_fin_stage = models.DateField(default=None, blank=True, null=True)#CHANGED
    type_rapport = models.CharField(max_length=200,blank=False, default='')
    resume_rapport = models.CharField(max_length=3000, default=None, blank=True, null=True)#CHANGED
    intitule_stage =models.CharField(max_length=200,blank=False, default='')
    societe_stage = models.CharField(max_length=200, default=None, blank=True, null=True)
    secteur_societe = models.CharField(max_length=200, default=None, blank=True, null=True)
    ville_societe = models.CharField(max_length=200, default=None, blank=True, null=True)
    pays_societe = models.CharField(max_length=200, default=None, blank=True, null=True)
    details_add_societe = models.CharField(max_length=200, default=None, blank=True, null=True)
    parrain = models.CharField(max_length=200, default=None, blank=True, null=True)
    email_parrain = models.EmailField(max_length = 254, default=None, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telephone_parrain = models.CharField(validators = [phoneNumberRegex], max_length = 16, default=None, blank=True, null=True)
    fichier_rapport = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        blank=False, default='',
        upload_to='media')
        #storage=gd_storage,)#CHANGED
    rapport_confidentiel = models.BooleanField(default=False)
    jurys  = models.ManyToManyField(Professeur, blank=True,related_name="fk_jury")
    #one to many relationship (with Etudiant)
    #nom_prenom=models.CharField(max_length=200,blank=False, default='')#ADDED
    valid_admin = models.BooleanField(default=False,blank=False,null=False) #admin validation field
    valid_encadrant = models.BooleanField(default=None, blank=True, null=True) #professor validation field
    fk_encadrant_univ = models.ForeignKey(Professeur, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    fk_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

class Forms(models.Model):
    nom_form = models.CharField(max_length=200,blank=False, default='')
    active_status = models.BooleanField(default=True)


# class MotCle(models.Model):
#     mot = models.CharField(max_length=200,blank=False, default='')
#     #many to many relationship (with rapport)
#     rapports = models.ManyToManyField(Rapport)
