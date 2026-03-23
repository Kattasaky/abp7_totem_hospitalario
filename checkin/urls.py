from django.urls import path
from . import views

urlpatterns = [ #se usa path para definir la urls de la app checkin
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'), #ruta para listar pacientes
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),#ruta para crear pacientes
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'), #ruta para
    path('checkin/', views.checkin_view, name='checkin'), #ruta para el check-in    
           
]