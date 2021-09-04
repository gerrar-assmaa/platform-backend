from main_app import views
from django.urls import path
from . import views

urlpatterns = [
  path('reportsFile',views.download_excel_data)
]