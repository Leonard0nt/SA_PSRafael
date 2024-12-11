"""
URL configuration for psr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from AppAdmin import views as admin_views
from AppCliente import views as client_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Autenticación
    path('', admin_views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Inicio del administrador
    path('administrador/', admin_views.homeAdministrador, name='home_administrador'),

    # Administración de contadores
    path('vAdm_contadores/', admin_views.administrador_contadores, name='vAdm_contador'),
    path('agregarcontador/', admin_views.crear_contador, name='crear_contador'),
    path('eliminar_contador/<str:contador_rut>/', admin_views.eliminar_contador, name='eliminar_contador'),
    path('obtener_contador/<str:contador_rut>/', admin_views.obtener_contador, name='obtener_contador'),
    path('editar_contador/<str:contador_rut>/', admin_views.editar_contador, name='editar_contador'),

    # Administración de cabaleros
    path('vAdm_cabaleros/', admin_views.administrador_cabaleros, name='vAdm_cabalero'),
    path('agregarcabalero/', admin_views.crear_cabalero, name='crear_cabalero'),
    path('eliminar_cabalero/<str:cabalero_rut>/', admin_views.eliminar_cabalero, name='eliminar_cabalero'),
    path('obtener_cabalero/<str:cabalero_rut>/', admin_views.obtener_cabalero, name='obtener_cabalero'),
    path('editar_cabalero/<str:cabalero_rut>/', admin_views.editar_cabalero, name='editar_cabalero'),

    # Administración de cabalas
    path('vAdm_cabalas/', admin_views.administrador_cabalas, name='vAdm_cabalas'),
    path('agregarcabala/', admin_views.crear_cabala, name='crear_cabala'),
    path('eliminar_cabala/<int:idCavala>/', admin_views.eliminar_cabala, name='eliminar_cabala'),
    path('obtener_cabala/<int:idCavala>/', admin_views.obtener_cabala, name='obtener_cabala'),
    path('editar_cabala/<int:idCavala>/', admin_views.editar_cabala, name='editar_cabala'),

    # Administración de clientes
    path('vAdm_clientes/', admin_views.administrador_clientes, name='vAdm_clientes'),
    path('agregarcliente/', admin_views.crear_cliente, name='crear_cliente'),
    path('eliminar_cliente/<str:cliente_rut>/', admin_views.eliminar_cliente, name='eliminar_cliente'),
    path('obtener_cliente/<str:cliente_rut>/', admin_views.obtener_cliente, name='obtener_cliente'),
    path('editar_cliente/<str:cliente_rut>/', admin_views.editar_cliente, name='editar_cliente'),

    # Funcionalidades del cliente
    path('registro_clientes/', client_views.crear_cliente, name='registro_clientes'),
    path('cliente/', client_views.homeCliente, name='home_cliente'),
    path('admin/', admin.site.urls), 
]
