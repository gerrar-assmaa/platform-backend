from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from main_app.models import MotCle, Professeur, Etudiant, Insertion, Rapport,Forms
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" 

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = "__all__"
        extra_kwargs = {
            'email_pro':{ 'validators': [UniqueValidator(queryset= Professeur.objects.all())]}, 
            'nom_prenom':{ 'validators': [UniqueValidator(queryset= Professeur.objects.all())]}
        }  

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = "__all__" 
        extra_kwargs = {
            'email_pro':{ 'validators': [UniqueValidator(queryset= Etudiant.objects.all())]},
            'nom_prenom':{ 'validators': [UniqueValidator(queryset= Etudiant.objects.all())]}
        }   
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
        fields ="__all__"

    # file_url = serializers.SerializerMethodField()
    
    # class Meta:
    #     model = Rapport
    #     fields = ('id','file_url')

    # def get_file_url(self, rapport):
    #     request = self.context.get('request')
    #     file_url = rapport.fichier_rapport.url
    #     return request.build_absolute_uri(file_url)

class MotCleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotCle
        fields = "__all__"

class ReadRapportSerializer(serializers.ModelSerializer):
    fk_etudiant = EtudiantSerializer()
    mots = MotCleSerializer( many=True)
    class Meta:
        model = Rapport
        fields = "__all__"      

      
class FormSerializer(serializers.ModelSerializer):      
    class Meta:
        model = Forms
        fields = "__all__"   
                               