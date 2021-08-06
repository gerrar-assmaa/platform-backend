from django.urls import path
from django.views.generic.base import RedirectView
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
    path('insertions',views.InsertionListFiltered),
    path('insertions/',views.InsertionListFiltered),
    path('insertions/<int:pk>',views.InsertionDetail.as_view()),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #rapports
    path('rapports/<int:pk>',views.RapportDetail.as_view()),
    path('rapports',views.ReportListFiltered),
    path('rapports/',views.ReportListFiltered),
    #mot clés
    path('motCles/',views.MotCleList.as_view()),
    path('motCles/<int:pk>/',views.MotCleDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)