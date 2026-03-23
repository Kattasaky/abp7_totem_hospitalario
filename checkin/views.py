from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})


def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'form.html', {'form': form})


def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('lista_pacientes')


# 🔥 CHECK-IN
def checkin_view(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')

        try:
            paciente = Paciente.objects.get(rut=rut)
            cita = Cita.objects.filter(paciente=paciente).first()

            if cita:
                registro = RegistroVisita.objects.create(
                    paciente=paciente,
                    doctor=cita.doctor
                )
                return render(request, 'ticket.html', {'registro': registro})

        except:
            return render(request, 'checkin.html', {'error': 'Paciente no encontrado'})

    return render(request, 'checkin.html')
            