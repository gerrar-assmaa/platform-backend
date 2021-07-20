from rest_framework import generics

#for Rapport
from main_app.models import Rapport
from main_app.serializers import RapportSerializer


class TutorialList(generics.ListCreateAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer


class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer