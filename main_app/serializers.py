from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from main_app.models import Professeur, Etudiant, Insertion, Rapport, MotCle

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = "__all__"
        extra_kwargs = {
            'email_pro':{ 'validators': [
                UniqueValidator(queryset= Professeur.objects.all())
            ] 
        }
    }  

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = "__all__" 
        extra_kwargs = {
            'email_pro':{ 'validators': [
                UniqueValidator(queryset= Etudiant.objects.all())
            ] 
            }
        }   

class InsertionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insertion
        fields = "__all__"                               

class RapportSerializer(serializers.ModelSerializer):
    #Etudiant = serializers.IntegerField(source = 'Etudiant.id')
    
    class Meta:
        model = Rapport
        fields = "__all__"

class MotCleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotCle
        fields = "__all__"

          

                               