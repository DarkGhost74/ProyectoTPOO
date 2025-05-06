from django.shortcuts import render
from .models import Aseguradora
from django.contrib.auth.decorators import login_required

@login_required
def aseguradoras(request):
    query = request.GET.get('q')
    if query:
        aseguradoras = Aseguradora.objects.filter(
            id__icontains=query
        ) | Aseguradora.objects.filter(
            nombre__icontains=query
        )
    else:
        aseguradoras = Aseguradora.objects.all()
    return render(request, "aseguradoras/aseguradoras.html", {'aseguradoras':aseguradoras})