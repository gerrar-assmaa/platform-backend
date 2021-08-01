from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
from django.views.generic.base import RedirectView
 

urlpatterns = [ 
    #utilisateurs
    path('utilisateurs/',views.UtilisateurList.as_view()),
    path('utilisateurs/<int:pk>/',views.UtilisateurDetail.as_view()),
    #professeurs
    path('professeurs/',views.ProfesseurList.as_view()),
    path('professeurs/<int:pk>/',views.ProfesseurDetail.as_view()),
    #etudiants
    path('etudiants/',views.EtudiantList.as_view()),
    path('etudiants/<int:pk>/',views.EtudiantDetail.as_view()),
    #insertions
    path('insertions',RedirectView.as_view(url='insertions/')),
    path('insertions/',views.InsertionList.as_view()),
    path('insertions/<int:pk>/',views.InsertionDetail.as_view()),
    #rapports
    path('rapports',RedirectView.as_view(url='rapports/')),
    path('rapports/',views.RapportList.as_view()),
    path('rapports/<int:pk>/',views.RapportDetail.as_view()),
    #mot clés
    path('motCles/',views.MotCleList.as_view()),
    path('motCles/<int:pk>/',views.MotCleDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)