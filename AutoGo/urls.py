"""
URL configuration for AutoGo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from reservas.views import VehiculoListView, VehiculoDetailView, VehiculoCreateView, VehiculoUpdateView, VehiculoDeleteView, UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, home
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', home, name='home'),
    path('usuarios/', include('usuarios.urls')),  # Ruta para usuarios
    path('vehiculos/', include('vehiculos.urls')),  # Ruta para vehículos
    ##########################################
    # Vehiculo
    ##########################################
    path('vehiculos/', VehiculoListView.as_view(), name='vehiculo_list'),
    path('vehiculos/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('vehiculos/nuevo/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculos/<int:pk>/editar/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', VehiculoDeleteView.as_view(), name='vehiculo_delete'),
    ##########################################
    # Usuario
    ##########################################
    path('usuario/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuario/nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]
