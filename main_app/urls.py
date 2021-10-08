from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
 

urlpatterns = [ 

    #User
    path('user/<int:pk>',views.UserDetail.as_view()),
    #professeurs
    path('professeurs/',views.ProfesseurList.as_view()),
    path('professeurs',views.ProfesseurList.as_view()),
    # 'professeurs/email?email=ff@ggg.ss' === #get professor by their email
    path('professeurs/email',views.ProfessorbyEmail), 
    # 'professeurs/user?user=4' === #get professor by fk_user
    path('professeurs/user',views.ProfessorbyUserId), 
    # 'professuers/2' === #get professor by its id
    path('professeurs/<int:pk>',views.ProfesseurDetail.as_view()), 
    
    #etudiants
    # 'etudiants?user=3' === #get etudiants by fk_user
    path('etudiants/',views.EtudiantListFiltered),
    path('etudiants',views.EtudiantListFiltered),
    # 'etudiants/email?email=ff@ggg.ddd' === #get student by their email
    path('etudiants/email',views.StudentbyEmail), 
    # 'etudiants/name?' === # get student by name (nom_prenom)
    path('etudiants/name',views.StudentbyName), 
    # 'etudiants/2' === #get etudiant by its id
    path('etudiants/<int:pk>',views.EtudiantDetail.as_view()), 
    
    #insertions
    # 'insertions?etudiant=3' === #get insertions by fk_etudiant 
    path('insertions',views.InsertionListFiltered),
    path('insertions/',views.InsertionListFiltered),
    # 'insertions/4' === # get insertions by its id
    path('insertions/<int:pk>',views.InsertionDetail.as_view()), 

    #rapports
    path('rapports/<int:pk>',views.RapportDetail.as_view()),
    path('rapports',views.ReportListFiltered),
    path('rapports/',views.ReportListFiltered),
    path('rapports/jury',views.ReportByJurys),
    path('rapports/adminValidated',views.ReportValidatedAdmin),
    path('rapports/validated',views.ReportValidated),
    path('rapports/validatedFiltered',views.ReportValidatedAndFiltered),
    path('rapports/notValidatedFiltered',views.ReportNotValidatedAndFiltered),
    path('rapports/type',views.ReportListFilteredType), #projet ou stage


    #forms
    path('forms/<int:pk>',views.FormDetail.as_view()),

    #mot clés
    path('motCles/',views.MotCleList.as_view()),
    path('motCles/<int:pk>',views.MotCleDetail.as_view()),
    path('motCles/mot',views.getIdMot),
]


urlpatterns = format_suffix_patterns(urlpatterns)