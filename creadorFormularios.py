# encoding=utf8
import json
import paquetes.crearArchivo as crearArchivo
import paquetes.htmlCreador as htmlCreador
import paquetes.crearClaseBase as crearClaseBase

datos      = json.loads(open('datos.json').read())
formulario = htmlCreador.getHtml(datos['formulario'])
crearArchivo.crear('__formulario.html', formulario)

claseEjemplo = crearClaseBase.crear(datos['formulario'], datos['tipo']) #tipos: crear, editar
crearArchivo.crear('__ComponenteEjemplo.php', claseEjemplo)

""" tipos de input
text = texto
number = numero
textarea = cuadro de texto
select = seleccionm multiple
"""

""" {
    "formulario":
    [    
        {
            "label": "Nombre", 
            "variable": "nombre", 
            "tipo": "text"
        },
        {
            "label": "Apellido", 
            "variable": "apellido", 
            "tipo": "text"
        },
        {
            "label": "Edad", 
            "variable": "edad", 
            "tipo": "number"
        },
        {
            "label": "Comentario", 
            "variable": "comentario", 
            "tipo": "textarea"
        },
        {
            "label": "Ciudad", 
            "variable": "ciudad", 
            "tipo": "select"
        },
        {
            "label": "Pais", 
            "variable": "pais", 
            "tipo": "select"
        }

    ],
    "tipo": "crear" 
} """