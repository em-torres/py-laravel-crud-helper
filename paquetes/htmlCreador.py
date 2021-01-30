import paquetes.formInputs as formInputs

def getHtml(datosFormulario):
    formulario = """@extends('layouts.formulario-base')

@section('titulo', 'Crear | Editar')
@section('tituloBoton', 'Enviar')
@section('confirmacionMensaje', 'Defina su mensaje')

@section('inputs')
    """

    for dato in datosFormulario:

        html       = formInputs.crearInput(dato['label'], dato['variable'], dato['tipo'])
        formulario = formulario + html

    formulario = formulario + """
@endsection"""
    
    return formulario