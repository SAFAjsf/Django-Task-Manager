from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea
from django.urls import reverse_lazy
# Create your views here.
# C-R-U-D

# READ: Mostrar la lista de tareas (List)
class TareaList(ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'tareas/tarea_list.html'

# READ: Mostrar una tarea en detalle (Detail)
class TareaDetail(DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'tareas/tarea_detail.html'

# CREATE: Crear una nueva tarea (Create)
class TareaCreate(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('lista_tareas') # Redirecciona a la lista después de crear

# UPDATE: Editar una tarea existente (Update)
class TareaUpdate(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('lista_tareas') # Redirecciona a la lista después de editar

# DELETE: Eliminar una tarea (Delete)
class TareaDelete(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('lista_tareas') # Redirecciona a la lista después de eliminar