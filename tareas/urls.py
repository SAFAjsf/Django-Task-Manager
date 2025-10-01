from django.urls import path
from . import views

urlpatterns = [
    path('', views.TareaList.as_view(), name='lista_tareas'),
    path('<int:pk>/', views.TareaDetail.as_view(), name='detalle_tarea'),
    path('nueva/', views.TareaCreate.as_view(), name='crear_tarea'),
    path('<int:pk>/editar/', views.TareaUpdate.as_view(), name='editar_tarea'),
    path('<int:pk>/eliminar/', views.TareaDelete.as_view(), name='eliminar_tarea'),
]