from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Poliza
from .forms import PolizaForm
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

@login_required
def poliza_detalle(request, Poliza_id, modo=None):
    poliza = get_object_or_404(Poliza, id=Poliza_id)

    if request.method == 'GET':
        form = PolizaForm(instance=poliza)
        return render(request, 'polizas/poliza_detalle.html', {
            'poliza': poliza,
            'form': form,
            'modo': modo
        })    
    else:
        try:
            form = PolizaForm(request.POST, instance=poliza)
            form.save()
            return redirect('poliza_ver', Poliza_id=Poliza_id)
        except ValueError:
            return render(request, 'polizas/poliza_detalle.html', {
                'poliza': poliza,
                'form': form,
                'modo': 'editar',
                'error': 'Datos inválidos'
            })