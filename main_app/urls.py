from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
 

urlpatterns = [ 
    path('rapports/',views.RapportList.as_view()),
    path('rapports/<int:pk>/',views.RapportDetail.as_view()),
    #mot clés
    path('motCles/',views.MotCleList.as_view()),
    path('motCles/<int:pk>/',views.MotCleDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)