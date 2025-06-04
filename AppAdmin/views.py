from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from forms.adminForms import ClienteForm, ContadorForm, CabaleroForm, CavalaForm, CustomAuthenticationForm
from AppAdmin.models import *
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Vista para el inicio del administrador
@login_required
def homeAdministrador(request):
    current_date = datetime.now().date()
    clientes = User.objects.filter(tipo_usuario='cliente')
    cabaleros = User.objects.filter(tipo_usuario='cabalero')
    contadores = User.objects.filter(tipo_usuario='contador')
    cabalas = Cavalas.objects.all()
    arriendosT = Arriendo.objects.all()
    arriendosC = [arriendo for arriendo in arriendosT if arriendo.fecha_arriendo.date() == current_date]
    
    contexto = {
        'clientes': clientes,
        'cabaleros': cabaleros,
        'contadores': contadores,
        'cabalas': cabalas,
        'current_day': current_date,
        'arriendos': arriendosC
    }
    return render(request, "../templates/administradorTemplates/adminBase.html", contexto)


# Vista de inicio de sesión personalizada

def login(request):
    return render(request, 'login/login.html', {'form': LoginView.form_class()})

class CustomLoginView(LoginView):
    template_name = 'login/login.html'  # Ajusta según tu estructura de carpetas
    success_url = reverse_lazy('/')  # Ajusta según tu URL de redirección exitosa

    def get_success_url(self):
        # Verifica si el usuario es administrador y redirige en consecuencia
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return '/administrador/'  # Ajusta según tu URL de administrador
            else:
                return '/cliente/'  # Ajusta según tu URL de voluntario
        return '/'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if not any(message.tags == messages.ERROR for message in messages.get_messages(self.request)):
            messages.error(self.request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')  # Mensaje de error
        return response


# Vistas relacionadas con contadores
@login_required
def administrador_contadores(request):
    contadores = User.objects.filter(tipo_usuario='contador')
    form = ContadorForm()
    contexto = {'contadores': contadores, 'form': form}
    return render(request, "../templates/administradorTemplates/adm_Contador.html", contexto)


@login_required
def crear_contador(request):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    if request.method == 'POST':
        form = ContadorForm(request.POST)
        if form.is_valid():
            contador = form.save()
            contador.tipo_usuario = 'contador'
            contador.save()
            return redirect('vAdm_contador')
        else:
            messages.error(request, 'Hubo un error al agregar el contador.')
    else:
        form = ContadorForm()

    return render(request, "../templates/administradorTemplates/adm_Contador.html", {'form': form})


@login_required
def eliminar_contador(request, contador_rut):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    contador = get_object_or_404(User, rut=contador_rut)
    contador.delete()
    return redirect('vAdm_contador')


@login_required
def obtener_contador(request, contador_rut):
    contador = get_object_or_404(User, rut=contador_rut)
    contador_data = {
        'rut': contador.rut,
        'nombres': contador.nombres,
        'apellidos': contador.apellidos,
        'telefono': contador.telefono,
        'direccion': contador.direccion
    }
    return JsonResponse(contador_data)


@login_required
def editar_contador(request, contador_rut):
    contador = get_object_or_404(User, rut=contador_rut)
    if request.method == 'POST':
        contador.nombres = request.POST.get('nombres')
        contador.apellidos = request.POST.get('apellidos')
        contador.telefono = request.POST.get('telefono')
        contador.direccion = request.POST.get('direccion')
        contador.save()
        messages.success(request, 'Contador actualizado correctamente.')
        return redirect('vAdm_contador')


# Vistas relacionadas con cabaleros
@login_required
def administrador_cabaleros(request):
    cabaleros = User.objects.filter(tipo_usuario='cabalero')
    form = CabaleroForm()
    contexto = {'cabaleros': cabaleros, 'form': form}
    return render(request, "../templates/administradorTemplates/adm_Cabalero.html", contexto)


@login_required
def crear_cabalero(request):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    if request.method == 'POST':
        form = CabaleroForm(request.POST)
        if form.is_valid():
            cabalero = form.save()
            cabalero.tipo_usuario = 'cabalero'
            cabalero.save()
            return redirect('vAdm_cabalero')
        else:
            messages.error(request, 'Hubo un error al agregar el cabalero.')
    else:
        form = CabaleroForm()

    return render(request, "../templates/administradorTemplates/adm_Cabalero.html", {'form': form})


@login_required
def eliminar_cabalero(request, cabalero_rut):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    cabalero = get_object_or_404(User, rut=cabalero_rut)
    cabalero.delete()
    return redirect('vAdm_cabalero')


@login_required
def obtener_cabalero(request, cabalero_rut):
    cabalero = get_object_or_404(User, rut=cabalero_rut)
    cabalero_data = {
        'rut': cabalero.rut,
        'nombres': cabalero.nombres,
        'apellidos': cabalero.apellidos,
        'telefono': cabalero.telefono,
        'direccion': cabalero.direccion
    }
    return JsonResponse(cabalero_data)


@login_required
def editar_cabalero(request, cabalero_rut):
    cabalero = get_object_or_404(User, rut=cabalero_rut)
    if request.method == 'POST':
        cabalero.nombres = request.POST.get('nombres')
        cabalero.apellidos = request.POST.get('apellidos')
        cabalero.telefono = request.POST.get('telefono')
        cabalero.direccion = request.POST.get('direccion')
        cabalero.save()
        messages.success(request, 'Cabalero actualizado correctamente.')
        return redirect('vAdm_cabalero')


# Vistas relacionadas con cabalas
@login_required
def administrador_cabalas(request):
    cabalas = Cavalas.objects.all()
    form = CavalaForm()
    contexto = {'cabalas': cabalas, 'form': form}
    return render(request, "../templates/administradorTemplates/adm_Cabala.html", contexto)


@login_required
def crear_cabala(request):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    if request.method == 'POST':
        form = CavalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vAdm_cabalas')
        else:
            messages.error(request, 'Hubo un error al agregar la cabala.')
    else:
        form = CavalaForm()

    return render(request, "../templates/administradorTemplates/adm_Cabala.html", {'form': form})


@login_required
def eliminar_cabala(request, idCavala):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    cabala = get_object_or_404(Cavalas, idCavala=idCavala)
    cabala.delete()
    return redirect('vAdm_cabalas')


@login_required
def obtener_cabala(request, idCavala):
    cabala = get_object_or_404(Cavalas, idCavala=idCavala)
    cabala_data = {
        'idCavala': cabala.idCavala,
        'sectorCavala': cabala.sectorCavala,
    }
    return JsonResponse(cabala_data)


@login_required
def editar_cabala(request, idCavala):
    cabala = get_object_or_404(Cavalas, idCavala=idCavala)
    if request.method == 'POST':
        cabala.sectorCavala = request.POST.get('sector')
        cabala.save()
        messages.success(request, 'Cabala actualizada correctamente.')
        return redirect('vAdm_cabalas')


# Vistas relacionadas con clientes
@login_required
def administrador_clientes(request):
    clientes = User.objects.filter(tipo_usuario='cliente')
    form = ClienteForm()
    contexto = {'clientes': clientes, 'form': form}
    return render(request, "../templates/administradorTemplates/adm_Cliente.html", contexto)


@login_required
def crear_cliente(request):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.tipo_usuario = 'cliente'
            cliente.save()
            return redirect('vAdm_clientes')
        else:
            messages.error(request, 'Hubo un error al agregar el cliente.')
    else:
        form = ClienteForm()

    return render(request, "../templates/administradorTemplates/adm_Cliente.html", {'form': form})


@login_required
def eliminar_cliente(request, cliente_rut):
    if not request.user.is_superuser:
        return redirect('customLoginView')

    cliente = get_object_or_404(User, rut=cliente_rut)
    cliente.delete()
    return redirect('vAdm_clientes')


@login_required
def obtener_cliente(request, cliente_rut):
    cliente = get_object_or_404(User, rut=cliente_rut)
    cliente_data = {
        'rut': cliente.rut,
        'nombres': cliente.nombres,
        'apellidos': cliente.apellidos,
        'telefono': cliente.telefono,
        'direccion': cliente.direccion
    }
    return JsonResponse(cliente_data)


@login_required
def editar_cliente(request, cliente_rut):
    cliente = get_object_or_404(User, rut=cliente_rut)
    if request.method == 'POST':
        cliente.nombres = request.POST.get('nombres')
        cliente.apellidos = request.POST.get('apellidos')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect('vAdm_clientes')

