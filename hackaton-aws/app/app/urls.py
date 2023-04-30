from incidentes import views
from django.urls import path

urlpatterns = [
    # rota, view responsável, nome de referência 
    path('incidentes/criar', views.incident_create, name='incident_create'),
    path('incidentes/list', views.incident_list, name='incident_list')
]

