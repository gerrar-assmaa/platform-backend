from rest_framework import generics
#necessary imports (models & serializers)
from main_app.models import Utilisateur, Professeur, Etudiant, Insertion, Rapport, MotCle
from main_app.serializers import UtilisateurSerializer, ProfesseurSerializer, EtudiantSerializer, InsertionSerializer, RapportSerializer, MotCleSerializer

#utilisateur
class UtilisateurList(generics.ListCreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
class UtilisateurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer   

#professeur
class ProfesseurList(generics.ListCreateAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
class ProfesseurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer

#etudiant
class EtudiantList(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
class EtudiantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    
#insertion
class InsertionList(generics.ListCreateAPIView):
    queryset = Insertion.objects.all()
    serializer_class = InsertionSerializer
class InsertionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insertion.objects.all()
    serializer_class = InsertionSerializer

#rapport
class RapportList(generics.ListCreateAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer
class RapportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer

#motcle
class MotCleList(generics.ListCreateAPIView):
    queryset = MotCle.objects.all()
    serializer_class = MotCleSerializer
class MotCleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotCle.objects.all()
    serializer_class = MotCleSerializer  

   