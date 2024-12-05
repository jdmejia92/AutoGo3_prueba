from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehiculo, Usuario

####################################################
# VEHICULO
####################################################
# Listar todos los vehículos
class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculo_list.html'
    context_object_name = 'vehiculos'

# Detalle de un vehículo
class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculo_detail.html'

# Crear un nuevo vehículo
class VehiculoCreateView(CreateView):
    model = Vehiculo
    template_name = 'vehiculo_form.html'
    fields = ['Placa', 'Modelo', 'Marca', 'Anno', 'CantidadAsientos', 'Tipo', 'EstadoReserva']
    success_url = reverse_lazy('vehiculo_list')

# Editar un vehículo existente
class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    template_name = 'vehiculo_form.html'
    fields = ['Placa', 'Modelo', 'Marca', 'Anno', 'CantidadAsientos', 'Tipo', 'EstadoReserva']
    success_url = reverse_lazy('vehiculo_list')

# Eliminar un vehículo
class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')

####################################################
# USUARIO
####################################################

# Listar todos los usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = 'usuarios'

# Detalle de un usuario
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuario_detail.html'

# Crear un nuevo usuario
class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuario_form.html'
    fields = ['DNI', 'Tier', 'Nombres', 'Correo', 'Contraseña']
    success_url = reverse_lazy('usuario_list')

# Editar un usuario existente
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuario_form.html'
    fields = ['DNI', 'Tier', 'Nombres', 'Correo', 'Contraseña']
    success_url = reverse_lazy('usuario_list')

# Eliminar un usuario
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')