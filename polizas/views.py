from django.shortcuts import render
from django.db.models import Q
from .models import Poliza
from django.contrib.auth.decorators import login_required

@login_required
def polizas(request):
    query = request.GET.get('q')
    if query:
        polizas = Poliza.objects.select_related(
            'clienteid', 'agenteid', 'aseguradoraid', 'tipopolizaid', 'formapagoid', 'metodopagoid'
        ).filter(
            Q(id__icontains=query) |
            Q(clienteid__nombre__icontains=query) |
            Q(clienteid__appaterno__icontains=query) |
            Q(clienteid__apmaterno__icontains=query) |
            Q(agenteid__nombre__icontains=query) |
            Q(agenteid__apellidopaterno__icontains=query) |
            Q(agenteid__apellidomaterno__icontains=query) |
            Q(aseguradoraid__nombre__icontains=query) |
            Q(tipopolizaid__nombre__icontains=query) |
            Q(formapagoid__forma__icontains=query) |
            Q(metodopagoid__metodo__icontains=query)
        )
    else:
        polizas = Poliza.objects.all()
    return render(request, "polizas/polizas.html", {'polizas':polizas})