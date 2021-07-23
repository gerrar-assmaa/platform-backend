from rest_framework import serializers 
from main_app.models import Rapport

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = ('id',
                'stage_ou_projet' ,
                'date_debut_stage' ,
                'date_fin_stage' ,
                'intitulé_stage' ,
                'société_stage' ,
                'secteur_société' ,
                'ville_société' ,
                'pays_société' ,
                'détails_add_société' ,
                'encadrant' ,
                'email_encadrant' ,
                'téléphone_encadrant' ,
                'lien_rapport' ,
                'rapport_confidentiel' )