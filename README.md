#  Sistema de Check-in Hospitalario

Este proyecto consiste en el desarrollo de un sistema de check-in hospitalario utilizando Django, cuyo objetivo es automatizar el registro de llegada de pacientes.

##  Funcionalidades

- Registro de pacientes (CRUD)
- Validación de pacientes mediante RUT
- Registro automático de visitas (check-in)
- Generación de ticket de atención
- Exportación de datos a Excel

##  Tecnologías utilizadas

- Python
- Django
- SQLite
- Bootstrap (para estilos)

##  Modelos principales

- Paciente
- Doctor
- Cita
- RegistroVisita

##  Flujo del sistema

1. El paciente ingresa su RUT
2. El sistema valida su existencia
3. Se verifica si tiene una cita agendada
4. Se registra su llegada automáticamente
5. Se genera un ticket con la información

##  Exportación de datos

El sistema permite exportar los registros a Excel para su análisis externo.

## ▶ Cómo ejecutar el proyecto

```bash
python manage.py runserver

###########################################################################

# Katherine Vergara 2026
# ABP-7
# Profesor Gustvo Madariaga