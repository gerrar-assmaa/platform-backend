from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
 

urlpatterns = [ 
    path('rapports/',views.TutorialList.as_view()),
    path('rapports/<int:pk>/',views.TutorialDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)