from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
#necessary imports (models & serializers)
from main_app.models import MotCle, Professeur, Etudiant, Insertion, Rapport, Forms
from main_app.serializers import MotCleSerializer, ProfesseurSerializer, EtudiantSerializer, InsertionSerializer, RapportSerializer, ReadEtudiantSerializer, ReadInsertionSerializer, ReadRapportSerializer,FormSerializer, UserSerializer

  
#User=====================================================================
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
        promotion = request.GET.get('promotion', None)
        if user is not None:
            etudiants = etudiants.filter(fk_user=user)
        if promotion is not None and promotion!="Tout":
            promotions=[]
            for i in range(3):
                val = int(promotion)-i
                promotions.append(val)
            print(promotions)    
            etudiants = etudiants.filter(promotion__in=promotions)    

        
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

@api_view(['GET'])
def ReportByJurys(request):
    if request.method == 'GET':
        reports = Rapport.objects.all()
        
        jury = request.GET.get('jury', None)
        if jury is not None:
          try:
            report = reports.filter(jurys=jury)
          except ObjectDoesNotExist:
            report = None
            
        rapport_Serializer = ReadRapportSerializer(report, many=True)
        return JsonResponse(rapport_Serializer.data, safe=False)

#rapports validés par admin (et encadrées par un certain professeur)
@api_view(['GET'])
def ReportValidatedAdmin(request):
    if request.method == 'GET':
        reports = Rapport.objects.all()
        
        #first get all admin validated reports
        reports = reports.filter(valid_admin=True) 

        fk_encadrant_univ = request.GET.get('fk_encadrant_univ', None)
        if fk_encadrant_univ is not None:
            report = reports.filter(fk_encadrant_univ=fk_encadrant_univ)

        rapport_Serializer = ReadRapportSerializer(report, many=True)
        return JsonResponse(rapport_Serializer.data, safe=False)


        
@api_view(['GET'])
def ReportValidated(request):
    if request.method == 'GET':
        reports = Rapport.objects.all()
        
        #first get all admin validated reports
        reports_AV = reports.filter(valid_admin=True) #admin validated reports
        # PFEreports_NV = reports_AV.filter(type_rapport="PFE",valid_encadrant=False) #PFE NOT VALIDATED == PFE admin validated reports,non validated by professor
        reports_V = reports_AV.exclude(type_rapport="PFE",valid_encadrant=False) #rapports validés n'importe le type

        rapport_Serializer = ReadRapportSerializer(reports_V, many=True)
        return JsonResponse(rapport_Serializer.data, safe=False)
        
        
@api_view(['GET'])
def ReportValidatedAndFiltered(request):
    if request.method == 'GET':
        reports = Rapport.objects.all()
        
        #first get all admin validated reports
        reports_AV = reports.filter(valid_admin=True) #admin validated reports
        # PFEreports_NV = reports_AV.filter(type_rapport="PFE",valid_encadrant=False) #PFE NOT VALIDATED == PFE admin validated reports,non validated by professor
        reports_V = reports_AV.exclude(type_rapport="PFE",valid_encadrant=False) #rapports validés n'importe le type

        year = request.GET.get('year', None)
        filiere = request.GET.get('filiere', None)
        type_rapport = request.GET.get('type_rapport', None)
        if year is not None and year != "Tout":
            reports_V = reports_V.filter(horodateur__startswith=year)
        if filiere is not None and filiere != "Tout":
            etudiant_filiere = Etudiant.objects.filter(filiere=filiere)
            reports_V = reports_V.filter(fk_etudiant__in=etudiant_filiere)
        if type_rapport is not None and type_rapport != "Tout":
            reports_V = reports_V.filter(type_rapport=type_rapport)

        rapport_Serializer = ReadRapportSerializer(reports_V, many=True)
        return JsonResponse(rapport_Serializer.data, safe=False)


@api_view(['GET'])
def ReportNotValidatedAndFiltered(request):
    if request.method == 'GET':
        reports = Rapport.objects.all()
        
        #first get all admin validated reports
        reports_NV = reports.filter(valid_admin=False) #admin validated reports

        year = request.GET.get('year', None)
        filiere = request.GET.get('filiere', None)
        type_rapport = request.GET.get('type_rapport', None)
        promotion = request.GET.get('promotion', None)
        code = request.GET.get('code', None)

        if year is not None and year != "Tout":
            reports_NV = reports_NV.filter(horodateur__startswith=year)
        if filiere is not None and filiere != "Tout":
            etudiant_filiere = Etudiant.objects.filter(filiere=filiere)
            reports_NV = reports_NV.filter(fk_etudiant__in=etudiant_filiere)
        if promotion is not None and promotion != "Tout":
            etudiant_promotion = Etudiant.objects.filter(promotion=promotion)
            reports_NV = reports_NV.filter(fk_etudiant__in=etudiant_promotion)
        if code is not None and code != "Tout":
            etudiant_code = Etudiant.objects.filter(code_etudiant=code)
            reports_NV = reports_NV.filter(fk_etudiant__in=etudiant_code)
        if type_rapport is not None and type_rapport != "Tout":
            reports_NV = reports_NV.filter(type_rapport=type_rapport)

        rapport_Serializer = ReadRapportSerializer(reports_NV, many=True)
        return JsonResponse(rapport_Serializer.data, safe=False)

@api_view(['GET'])
def ReportListFilteredType(request):
    parser_classes = (MultiPartParser, FormParser)
    # GET list of reports, POST a new report, DELETE all reports
    if request.method == 'GET':
        reports = Rapport.objects.all() 
        
        type = request.GET.get('type', None)
        if type is not None:
            reports = reports.filter(stage_ou_projet=type)
        
        reports_serializer = ReadRapportSerializer(reports, many=True)
        return JsonResponse(reports_serializer.data, safe=False)        
#===============================================================================


#motcle========================================================================
class MotCleList(generics.ListCreateAPIView):
    queryset = MotCle.objects.all()
    serializer_class = MotCleSerializer
class MotCleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotCle.objects.all()
    serializer_class = MotCleSerializer

@api_view(['GET'])
def getIdMot(request):
    if request.method == 'GET':
        motCles = MotCle.objects.all()
        
        mot = request.GET.get('mot', None)
        if mot is not None:
          try:
            motCle = motCles.get(mot=mot)
          except ObjectDoesNotExist:
            motCle = None
            
        motCle_Serializer = MotCleSerializer(motCle, many=False)
        return JsonResponse(motCle_Serializer.data, safe=False)  
#===============================================================================    

#form
class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forms.objects.all()
    serializer_class = FormSerializer

   