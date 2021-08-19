from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
 

urlpatterns = [ 
    #professeurs
    path('professeurs/',views.ProfesseurList.as_view()),
    path('professeurs',views.ProfesseurList.as_view()),
    path('professeurs/email',views.ProfessorbyEmail),
    path('professeurs/<int:pk>',views.ProfesseurDetail.as_view()),
    #etudiants
    path('etudiants/',views.EtudiantList.as_view()),
    path('etudiants',views.EtudiantList.as_view()),
    path('etudiants/email',views.StudentbyEmail),
    path('etudiants/<int:pk>',views.EtudiantDetail.as_view()),
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