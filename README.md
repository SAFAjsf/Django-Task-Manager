# Evaluación Práctica: Gestor de Tareas con Django

Este proyecto es la implementación de un Gestor de Tareas simple utilizando el framework **Django**.

El proyecto incluye:
* Configuración de la aplicación (`gestor_tareas`/`tareas`) y la base de datos (SQLite).
* Definición del modelo de datos (`Tarea`) con el Django ORM.
* Uso y personalización del **Django Admin**.
* Implementación completa de las operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) mediante Vistas Basadas en Clases (VBC) genéricas.

---

## Configuración e Instalación

### Requisitos

* Python 3.x
* pip

### Pasos de Configuración

1.  **Crear Entorno Virtual e Instalar Django:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate  # Para Windows
    # source .venv/bin/activate # Para Linux/macOS
    pip install django
    ```

2.  **Crear Proyecto y Aplicación (Siguiendo el Requisito de Nombres):**
    ```bash
    django-admin startproject evaluacion_tareas
    cd evaluacion_tareas
    python manage.py startapp tareas
    # NOTA: Se debe agregar 'tareas' a INSTALLED_APPS en settings.py
    ```

3.  **Ejecutar Migraciones:**
    ```bash
    python manage.py makemigrations tareas
    python manage.py migrate
    ```

4.  **Crear Superusuario (para Django Admin):**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Ejecutar el Servidor:**
    ```bash
    python manage.py runserver
    ```

---

## Código del Modelo y Admin

### 1. Código del Modelo Tarea (`tareas/models.py`)

```python
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    prioridad = models.IntegerField(default=3)
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
```

### 2. Configuración de Django Admin (tareas/admin.py)

```python
from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    # Mejora: Columnas visibles en el listado
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_limite', 'fecha_creacion')
    
    # Mejora: Filtros laterales
    list_filter = ('vigente', 'prioridad', 'fecha_creacion')
    
    # Mejora: Campos disponibles para la búsqueda
    search_fields = ('titulo', 'descripcion')
# Registrar el modelo Tarea con su clase de configuración
admin.site.register(Tarea, TareaAdmin)
```

### 3. Código de Vistas CRUD (VBC)

Código de Vistas (tareas/views.py)
```python

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Tarea
from django.urls import reverse_lazy

# READ: Muestra lista de tareas
class TareaList(ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'tareas/tarea_list.html'

# READ: Muestra el detalle de una tarea
class TareaDetail(DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'tareas/tarea_detail.html'

# CREATE: Crea una nueva tarea
class TareaCreate(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('lista_tareas')

# UPDATE: Edita una tarea existente
class TareaUpdate(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('lista_tareas')

# DELETE: Elimina una tarea
class TareaDelete(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('lista_tareas')
```

### 4. Consultas ORM en Django Shell
A continuación, se registran las consultas fundamentales ejecutadas en el python manage.py shell, demostrando la interacción con el ORM de Django.

**from tareas.models import Tarea**	
*Importación del Modelo*	
**Tarea.objects.all()**	
*READ (Todas)*	*Lista todos los objetos Tarea disponibles en la base de datos*.
**Tarea.objects.filter(vigente=True).order_by('-prioridad')**	
*READ (Filtro y Orden)	Filtra las tareas donde vigente=True y las ordena por prioridad de mayor a menor.*
**Tarea.objects.create(titulo="Renovar licencia de conducir", descripcion="Renovar la licencia", prioridad=2)**	
*CREATE (ORM) Crea e inserta un nuevo registro en la base de datos.*
**tarea_urgente = Tarea.objects.get(titulo="Hacer copia de seguridad")**
*Obtiene el objeto para ser modificado.*
**tarea_urgente.prioridad = 5**
*UPDATE* Cambia el valor del campo prioridad en la instancia.*
**tarea_urgente.save()**
*(Sin output). Persiste los cambios de la instancia a la base de datos.*
**Tarea.objects.get(titulo="Renovar licencia de conducir").delete()** 
**(1, {'tareas.Tarea': 1})**
*Elimina la tarea y confirma el número de objetos eliminados.*