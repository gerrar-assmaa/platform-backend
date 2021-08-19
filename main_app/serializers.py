from django.contrib.auth.models import User
from rest_framework import serializers 
from main_app.models import Professeur, Etudiant, Insertion, Rapport, MotCle
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" 

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = "__all__"  

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = "__all__" 
class ReadEtudiantSerializer(serializers.ModelSerializer):
    fk_user = UserSerializer()
    class Meta:
        model = Etudiant
        fields = "__all__"            

class InsertionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insertion
        fields = "__all__"
class ReadInsertionSerializer(serializers.ModelSerializer):
    fk_etudiant = EtudiantSerializer()
    class Meta:
        model = Insertion
        fields = "__all__"      

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = "__all__"
class ReadRapportSerializer(serializers.ModelSerializer):
    fk_etudiant = EtudiantSerializer()
    class Meta:
        model = Rapport
        fields = "__all__"        

class MotCleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotCle
        fields = "__all__"

          

                               