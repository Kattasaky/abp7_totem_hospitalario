from django.contrib import admin
from .models import Paciente, Doctor, Cita, RegistroVisita

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Cita)
admin.site.register(RegistroVisita)