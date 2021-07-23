from rest_framework import generics

#necessary imports (models & serializers)
from main_app.models import Rapport, MotCle
from main_app.serializers import RapportSerializer, MotCleSerializer

#rapport
class RapportList(generics.ListCreateAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer
class RapportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer

#motcle
class MotCleList(generics.ListCreateAPIView):
    queryset = MotCle.objects.all()
    serializer_class = MotCleSerializer
class MotCleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotCle.objects.all()
    serializer_class = MotCleSerializer    