from django.shortcuts import render
from .models import Incidents
from random import randint

# Create your views here.

def incident_create(request):
    return render(request, 'create-incident/incident.html')

def incident_list(request):
    incidente = Incidents()
    incidente.id = randint(100,1000)
    incidente.name = request.POST.get('name')
    incidente.email = request.POST.get('email')
    incidente.number_pedido = request.POST.get('number')
    incidente.assunto = request.POST.get('assunto')
    incidente.description = request.POST.get('description')
    incidente.save()
    incidentes = {
        'incidentes': Incidents.objects.all()
    }
    return render(request, 'list-incident/listincident.html', incidentes)