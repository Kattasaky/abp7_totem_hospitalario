from django.db import models

# Modelo Paciente
class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre  

# Modelo Doctor
class Doctor(models.Model):    
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre  

# Modelo Cita
class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()          
    hora = models.TimeField()   

    def __str__(self):        
        return f"Cita de {self.paciente} con {self.doctor} el {self.fecha} a las {self.hora}"

# Modelo RegistroVisita
class RegistroVisita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="En espera")

    def __str__(self):
        return f"{self.paciente} - {self.estado}"


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()          
    hora = models.TimeField()   

def __str__(self):        
        return f"Cita de{self.paciente} con {self.doctor} el {self.fecha} a las {self.hora}"

class RegistroVisita(models.Model):
     paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
     fecha_hora = models.DateTimeField(auto_now_add=True)
     estado = models.CharField(max_length=20, default="En espera")

def __str__(self):
        return f"{self.paciente} - {self.estado}"