import re
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

#OneToOne => one to one relationship
#foreignKey => one to many relationship
#ManyToMany => many to many relationship


class Utilisateur(models.Model):
    email = models.EmailField(max_length = 254)
    name = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    type = models.CharField(max_length=1,blank=False, default='')
 
    def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        super(Utilisateur, self).save(*args, **kwargs)

class Professeur(models.Model):
    prenom = models.CharField(max_length=200,blank=False, default='')
    nom = models.CharField(max_length=200,blank=False, default='')
    email_perso = models.EmailField(max_length = 254)
    email_pro = models.EmailField(max_length = 254)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")    
    telephone = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    departement = models.CharField(max_length=200,blank=False, default='')
    #one to one relationship (with utilisateur)
    fk_id_user = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,primary_key=True)         

class Etudiant(models.Model):
    code_etudiant = models.IntegerField()
    prenom = models.CharField(max_length=200,blank=False, default='')
    nom = models.CharField(max_length=200,blank=False, default='')
    email_perso = models.EmailField(max_length = 254)
    email_pro = models.EmailField(max_length = 254)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")    
    telephone = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    filiere = models.CharField(max_length=200,blank=False, default='')
    promotion = models.DateField()
    #one to one relationship (with utilisateur)
    fk_id_user = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,primary_key=True)    

class Insertion(models.Model):
    cursus_post_ensam = models.CharField(max_length=200,blank=False, default='')
    univ = models.CharField(max_length=200,blank=False, default='')
    pays_univ= models.CharField(max_length=200,blank=False, default='')
    nature_formation = models.CharField(max_length=200,blank=False, default='')
    intit_formation = models.CharField(max_length=200,blank=True, default='')
    intit_poste = models.CharField(max_length=200,blank=True, default='')
    societe = models.CharField(max_length=200,blank=False, default='')
    ville_societe = models.CharField(max_length=200,blank=False, default='')
    date_integration = models.DateField()
    #one to one relationship (with Etudiant)
    fk_code_etudiant = models.OneToOneField(Etudiant,on_delete=models.CASCADE,primary_key=True)    

class Rapport(models.Model):
    stage_ou_projet = models.BooleanField(default=True)
    date_debut_stage = models.DateField()
    date_fin_stage = models.DateField()
    intitule_stage =models.CharField(max_length=200,blank=False, default='')
    societe_stage =models.CharField(max_length=200,blank=False, default='')
    secteur_societe =models.CharField(max_length=200,blank=False, default='')
    ville_societe =models.CharField(max_length=200,blank=False, default='')
    pays_societe =models.CharField(max_length=200,blank=False, default='')
    details_add_societe =models.CharField(max_length=200,blank=True)
    encadrant =models.CharField(max_length=200)
    email_encadrant = models.EmailField(max_length = 254)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telephone_encadrant = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    lien_rapport = models.URLField(max_length = 200)
    rapport_confidentiel = models.BooleanField(default=True)
    #one to many relationship (with Etudiant)
    fk_id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

class MotCle(models.Model):
    mot = models.CharField(max_length=200,blank=False, default='')
    #many to many relationship (with rapport)
    rapports = models.ManyToManyField(Rapport)



"""    def confirm(request):
        user_name = None
        user_password = None
        if request.method == "POST":
            user_name = request.POST.get("user_name", None)
            user_password = request.POST.get("user_password", None)
        # Get elements in the database
        try:
            item = Utilisateur.objects.get(name=user_name)
        except ObjectDoesNotExist:
            return HttpResponse('username error')

        if check_password(user_password, item.password):
            return HttpResponseRedirect('/automation/')
        return HttpResponse('username or password is wrong')    """


