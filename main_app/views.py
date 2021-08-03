from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
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

@api_view(['GET', 'POST', 'DELETE'])
def InsertionListFiltered(request):
    # GET list of insertions, POST a new insertion, DELETE all insertions
    if request.method == 'GET':
        insertions = Insertion.objects.all()
        
        etudiant = request.GET.get('etudiant', None)
        if etudiant is not None:
            insertions = insertions.filter(fk_etudiant=etudiant)
        
        insertions_serializer = InsertionSerializer(insertions, many=True)
        return JsonResponse(insertions_serializer.data, safe=False)
    
    elif request.method == 'POST':
        insertion_data = JSONParser().parse(request)
        insertion_serializer = InsertionSerializer(data=insertion_data)
        if insertion_serializer.is_valid():
            insertion_serializer.save()
            return JsonResponse(insertion_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(insertion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Insertion.objects.all().delete()
        return JsonResponse({'message': '{} insertions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)        

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

   