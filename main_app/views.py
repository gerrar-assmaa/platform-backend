from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
#necessary imports (models & serializers)
from main_app.models import Professeur, Etudiant, Insertion, Rapport
from main_app.serializers import ProfesseurSerializer, EtudiantSerializer, InsertionSerializer, RapportSerializer, ReadEtudiantSerializer, ReadInsertionSerializer, ReadRapportSerializer
  


#professeur=====================================================================
class ProfesseurList(generics.ListCreateAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
class ProfesseurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer

@api_view(['GET'])
def ProfessorbyEmail(request):
    # GET list of reports, POST a new report, DELETE all reports
    if request.method == 'GET':
        professeurs = Professeur.objects.all()
        
        email = request.GET.get('email', None)
        if email is not None:
          try:
            professeur = professeurs.get(email_pro=email)
          except ObjectDoesNotExist:
            professeur = None
            
        professeur_Serializer = ProfesseurSerializer(professeur, many=False)
        return JsonResponse(professeur_Serializer.data, safe=False)

@api_view(['GET'])
def ProfessorbyUserId(request):
    # GET list of reports, POST a new report, DELETE all reports
    if request.method == 'GET':
        professeurs = Professeur.objects.all()
        
        user = request.GET.get('user', None)
        if user is not None:
          try:
            professeur = professeurs.get(fk_user=user)
          except ObjectDoesNotExist:
            professeur = None
            
        professeur_Serializer = ProfesseurSerializer(professeur, many=False)
        return JsonResponse(professeur_Serializer.data, safe=False)
#===============================================================================


#etudiant=======================================================================
# class EtudiantList(generics.ListCreateAPIView):
#     queryset = Etudiant.objects.all()
#     serializer_class = EtudiantSerializer
class EtudiantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadEtudiantSerializer
        else:
            return EtudiantSerializer

@api_view(['GET']) 
def StudentbyEmail(request):
    # GET list of reports, POST a new report, DELETE all reports
    if request.method == 'GET':
        etudiants = Etudiant.objects.all()
        
        email = request.GET.get('email', None)
        if email is not None:
          try:
            etudiant = etudiants.get(email_pro=email)
          except ObjectDoesNotExist:
            etudiant = None
            
        etudiant_Serializer = ReadEtudiantSerializer(etudiant, many=False)
        return JsonResponse(etudiant_Serializer.data, safe=False)
    # serializer_class = EtudiantSerializer

@api_view(['GET']) 
def StudentbyName(request):
    # GET list of reports, POST a new report, DELETE all reports
    if request.method == 'GET':
        etudiants = Etudiant.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
          try:
            etudiant = etudiants.get(nom_prenom=name)
          except ObjectDoesNotExist:
            etudiant = None
            
        etudiant_Serializer = ReadEtudiantSerializer(etudiant, many=False)
        return JsonResponse(etudiant_Serializer.data, safe=False)
    # serializer_class = EtudiantSerializer

@api_view(['GET', 'POST', 'DELETE'])
def EtudiantListFiltered(request):
    # GET list of etudiants, POST a new etudiant, DELETE all etudiants
    if request.method == 'GET':
        etudiants = Etudiant.objects.all()
        
        user = request.GET.get('user', None)
        if user is not None:
            etudiants = etudiants.filter(fk_user=user)
        
        etudiants_serializer = ReadEtudiantSerializer(etudiants, many=True)
        return JsonResponse(etudiants_serializer.data, safe=False)
    
    elif request.method == 'POST':
        etudiant_data = JSONParser().parse(request)
        etudiant_serializer = EtudiantSerializer(data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant_serializer.save()
            return JsonResponse(etudiant_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(etudiant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Etudiant.objects.all().delete()
        return JsonResponse({'message': '{} etudiants were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)        
#===============================================================================


#insertion=======================================================================
# class InsertionList(generics.ListCreateAPIView):
#     queryset = Insertion.objects.all()
#     serializer_class = InsertionSerializer
class InsertionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insertion.objects.all()
    # serializer_class = InsertionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadInsertionSerializer
        else:
            return InsertionSerializer

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = ReadInsertionSerializer(queryset, many=True)
    #     return response(serializer.data)
        
@api_view(['GET', 'POST', 'DELETE'])
def InsertionListFiltered(request):
    # GET list of insertions, POST a new insertion, DELETE all insertions
    if request.method == 'GET':
        insertions = Insertion.objects.all()
        
        etudiant = request.GET.get('etudiant', None)
        if etudiant is not None:
            insertions = insertions.filter(fk_etudiant=etudiant)
        
        insertions_serializer = ReadInsertionSerializer(insertions, many=True)
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
#===============================================================================

reportSet=Rapport.objects.all().prefetch_related('fk_etudiant')
#rapport=========================================================================
class RapportList(generics.ListCreateAPIView):
    queryset = reportSet
    serializer_class = RapportSerializer
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ReadRapportSerializer
    #     else:
    #         return RapportSerializer
class RapportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = reportSet
    # serializer_class = RapportSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadRapportSerializer
        else:
            return RapportSerializer

@api_view(['GET', 'POST', 'DELETE'])
def ReportListFiltered(request):
    parser_classes = (MultiPartParser, FormParser)
    # GET list of reports, POST a new report, DELETE all reports
    if request.method == 'GET':
        reports = Rapport.objects.all()
        
        etudiant = request.GET.get('etudiant', None)
        if etudiant is not None:
            reports = reports.filter(fk_etudiant=etudiant)
        
        reports_serializer = ReadRapportSerializer(reports, many=True)
        return JsonResponse(reports_serializer.data, safe=False)
    
    elif request.method == 'POST':
        reports_data=request.data
        #reports_data = JSONParser().parse(request)
        reports_serializer = RapportSerializer(data=reports_data)
        if reports_serializer.is_valid():
            reports_serializer.save()
            return JsonResponse(reports_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(reports_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Rapport.objects.all().delete()
        return JsonResponse({'message': '{} reports were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
#===============================================================================


# #motcle========================================================================
# class MotCleList(generics.ListCreateAPIView):
#     queryset = MotCle.objects.all()
#     serializer_class = MotCleSerializer
# class MotCleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MotCle.objects.all()
#     serializer_class = MotCleSerializer  
# #===============================================================================    


   