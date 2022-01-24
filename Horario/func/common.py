from Horario.models import set_Horario





def Set_Mult_Horario(hour = 24,data = None,medicamento = None,usuario = None):
    """Crea multiples horarios pasandole como variable:
    hour: son las horas en las vas a partir el dia
    data: Son los datos del formulario
    medicamento: es el registro del medicamento a registrar 
    usuario: es el registro del usuario que registra el horario
    """
    
    part = (24 // hour) - 1
    if (int (data.get('Hora')) + part) < 24:

        for i in range(data.get('Hora'),24,hour):

            print("Hago algo %d"%i)

            New_Horario = set_Horario(

                Hora = i,
                Minutos = data.get('Minutos'),
                Num_Dia = int (data.get('Dia')),
                Medicamento = medicamento,
                Dosis = data.get('Dosis'),
                Usuario = usuario
            )

            New_Horario.save()

    else:
        return False
    return True