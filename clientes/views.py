from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm

@login_required
def clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(
            id__icontains=query
        ) | Cliente.objects.filter(
            nombre__icontains=query
        ) | Cliente.objects.filter(
            appaterno__icontains=query
        ) | Cliente.objects.filter(
            apmaterno__icontains=query
        )
    else:
        clientes = Cliente.objects.all()
    return render(request, "clientes/clientes.html", {'clientes':clientes})

@login_required
def crear_cliente(request):
    if request.method == 'GET':
        return render(request, 'clientes/crear.html', {'form': ClienteForm})
    else:
        try:
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit=False)
            nuevo_cliente.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'clientes/crear.html', {
                'form': ClienteForm,
                'error': 'Datos inválidos'
            })
        
@login_required
def cliente_detalle(request, Cliente_id, modo=None):
    cliente = get_object_or_404(Cliente, id=Cliente_id)

    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/cliente_detalle.html', {
            'cliente': cliente,
            'form': form,
            'modo': modo
        })    
    else:
        try:
            form = ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect('cliente_ver', Cliente_id=Cliente_id)
        except ValueError:
            return render(request, 'clientes/cliente_detalle.html', {
                'cliente': cliente,
                'form': form,
                'modo': 'editar',
                'error': 'Datos inválidos'
            })