document.addEventListener("DOMContentLoaded",
    ()=>{
        if(!Notification){
            return;
        }

        if(Notification.permission !== "granted")
        {
            Notification.requestPermission();
        }

    });

function get_Hours()
{

    hora = new Date()

    horas = hora.getHours()
    minutos  = hora.getMinutes()

    var mensaje = `Estos medicamentos tocan en esta hora: `

    fetch("/hor/g/").then(
        (response) =>
        {
            if (response.ok)
            {
                response.json().then(
                    (data)=>{
                        tos = data.Medicamentos
                        if (tos.length)
                        {

                            tos.forEach(element => {

                                mensaje = mensaje.concat("\n" + element)
    
                            });
    
                            var notificacion = new Notification(
                                "Medicamentos a tomar",
                                {
                                    body: mensaje
                                }
                            )

                        }
                        
                    }
                )
            }
        }
    );
    

}


var popoverTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="popover"]')
    )

var popoverList = popoverTriggerList.map(
    function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })

function editar_Campo(id)
{
    search_Cancel()

    var input_Medicinas = document.getElementById("Medicamento")
    var input_Unidades = document.getElementById("Unidades")
    var input_Registro = document.getElementById("Registro")

    var table_Medicinas = document.getElementById(`${id}_Medicamento`)
    var table_Unidades = document.getElementById(`${id}_Unidades`)
    var table_Registro = document.getElementById(`${id}_Registro`)

    var button = document.getElementById(`inv_Send`)
    var button_Org = document.getElementById(`${id}_Edit`)

    var formulario = document.getElementById("medicamento")

    button.textContent = "Actualizar"

    button_Org.setAttribute("class","btn btn-danger mb-3")
    button_Org.setAttribute("id","Cancel")
    button_Org.setAttribute("onclick","search_Cancel()")
    button_Org.value = id
    button_Org.textContent = "Cancelar"

    input_Medicinas.value = table_Medicinas.textContent
    input_Unidades.value = parseFloat( table_Unidades.textContent )
    input_Registro.checked =  table_Registro.textContent.replace(/^\s+|\s+$/g, '') == 'x'

    var input = document.createElement("input")
    input.setAttribute("type","hidden")
    input.setAttribute("name","Temp_ID")
    input.setAttribute("value",id)
    input.setAttribute("id","Temp")

    formulario.setAttribute("action","/inv/update/")
    formulario.appendChild(input)

    console.log(button_Org)


}

function search_Cancel()
{

    var button_Org = document.getElementById(`Cancel`)
    var formulario = document.getElementById("medicamento")
    formulario.setAttribute("action","")
    

    if (button_Org == null)
    {

        return

    }
    var input = document.getElementById("Temp")
    formulario.removeChild(input)

    var input_Medicinas = document.getElementById("Medicamento")
    var input_Unidades = document.getElementById("Unidades")
    var input_Registro = document.getElementById("Registro")

    var button = document.getElementById(`inv_Send`)

    var id  = button_Org.value

    button.textContent = "Nuevo Medicamento"
    button_Org.setAttribute("class","btn btn-primary mb-3")
    button_Org.setAttribute("id",`${id}_Edit`)
    button_Org.setAttribute("onclick",`editar_Campo(${id})`)
    button_Org.textContent = "Editar"

    input_Medicinas.value = ""
    input_Unidades.value = null
    input_Registro.checked =  false


}