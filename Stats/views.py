from main_app.models import Etudiant, Rapport
import xlwt
from django.http import HttpResponse
from rest_framework.decorators import api_view

class Filters():
    def __init__(self):
        self.filiere = None
        self.promotion = None

@api_view(['GET'])
def download_excel_data(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    #decide file name
    response['Content-Disposition'] = 'attachment; filename="myExcelFile.xls"'

    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("rapports")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    #column header names, you can use your own headers here
    columns = ['code_etudiant', 'nom_prenom', 'filiere', 'promotion','stage_ou_projet','date_debut_stage',
    'date_fin_stage','type_rapport','intitule_stage','societe_stage','secteur_societe','ville_societe',
    'pays_societe','fichier_rapport','rapport_confidentiel' ]

    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #get your data, from database or from a text file...
    data = Rapport.objects.all() #here we have to filter data on demand
    # data = Rapport.objects.prefetch_related('fk_etudiant')
    # print(data[0])
    # nestedData = [  ]

    #creating the filters object
    myFilters = Filters()
    myFilters.promotion = request.GET.get('promotion', None)
    myFilters.filiere = request.GET.get('filiere', None)
    print(myFilters.filiere)
    print(myFilters.promotion)

    #etudiant = request.GET.get('etudiant', None)
    # if etudiant is not None:
    #     data = data.filter(fk_etudiant=etudiant)

    etudiants = Etudiant.objects.all() 
    if myFilters.filiere is not None and myFilters.promotion is not None:
        etudiants = etudiants.filter(filiere = myFilters.filiere,promotion = myFilters.promotion)
    elif myFilters.filiere is not None:
        etudiants = etudiants.filter(filiere = myFilters.filiere)
    elif myFilters.promotion is not None:
        etudiants = etudiants.filter(promotion = myFilters.promotion)
    
    etudiants_ids = []
    for etudiant in etudiants:
        etudiants_ids.append(etudiant.id)
    print(etudiants_ids)

    data = data.filter(fk_etudiant__in = etudiants_ids)    

    # if myFilters.filiere is not None and myFilters.promotion is not None:
    #     data = data.filter(fk_etudiant=Filters(myFilters.filiere,myFilters.promotion))
    # elif myFilters.filiere is not None:
    #     data = data.filter(fk_etudiant=Filters(myFilters.filiere))
    # elif myFilters.promotion is not None:
    #     data = data.filter(Filters(myFilters.promotion))

    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.fk_etudiant.code_etudiant, font_style)
        ws.write(row_num, 1, my_row.fk_etudiant.nom_prenom, font_style)
        ws.write(row_num, 2, my_row.fk_etudiant.filiere, font_style)
        ws.write(row_num, 3, my_row.fk_etudiant.promotion, font_style)
        ws.write(row_num, 4, my_row.stage_ou_projet, font_style)
        ws.write(row_num, 5, my_row.date_debut_stage, font_style)
        ws.write(row_num, 6, my_row.date_fin_stage, font_style)
        ws.write(row_num, 7, my_row.type_rapport, font_style)
        ws.write(row_num, 8, my_row.intitule_stage, font_style)
        ws.write(row_num, 9, my_row.societe_stage, font_style)
        ws.write(row_num, 10, my_row.secteur_societe, font_style)
        ws.write(row_num, 11, my_row.ville_societe, font_style)
        ws.write(row_num, 12, my_row.pays_societe, font_style)
        ws.write(row_num, 13, str(my_row.fichier_rapport.url), font_style)
        ws.write(row_num, 14, my_row.rapport_confidentiel, font_style)

    wb.save(response)
    return response