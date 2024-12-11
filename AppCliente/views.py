from django.shortcuts import render, redirect, get_object_or_404
from forms.adminForms import ClienteForm

from django.contrib import messages
from AppAdmin.models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime

def crear_cliente(request):
    """
    Vista para registrar un cliente desde una página pública o interna.
    """
    if request.method == 'GET':
        # Renderiza el formulario vacío para el registro
        form = ClienteForm()
        return render(request, 'clienteTemplates/registro_Cliente.html', {'form': form})

    if request.method == 'POST':
        # Procesa el formulario enviado
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Guarda el nuevo cliente
            cliente = form.save()
            cliente.tipo_usuario = 'cliente'
            cliente.save()
            messages.success(request, "Registro completado con éxito. ¡Bienvenido!")
            return redirect('login')  # Redirige a la página de inicio de sesión o donde prefieras
        else:
            # Muestra los errores del formulario
            messages.error(request, "Hubo errores en el registro. Por favor corrige los campos indicados.")
            return render(request, 'clienteTemplates/registro_Cliente.html', {'form': form})


@login_required
def homeCliente(request):
    """
    Vista principal para los clientes registrados.
    """
    current_date = datetime.now().date()

    # Filtrar usuarios y objetos relacionados
    clientes = User.objects.filter(tipo_usuario='cliente')
    cabaleros = User.objects.filter(tipo_usuario='cabalero')
    contadores = User.objects.filter(tipo_usuario='contador')
    cabalas = Cavalas.objects.all()

    # Filtrar arriendos del día actual
    arriendosT = Arriendo.objects.all()
    arriendosC = [arriendo for arriendo in arriendosT if arriendo.fecha_arriendo == current_date]

    # Contexto para la plantilla
    contexto = {
        'clientes': clientes,
        'cabaleros': cabaleros,
        'contadores': contadores,
        'cabalas': cabalas,
        'current_day': current_date,
        'arriendos': arriendosC
    }

    return render(request, 'clienteTemplates/clienteBase.html', contexto)
