def getVariables(datosFormulario):
    formulario = ''

    for dato in datosFormulario:

        html       = "\tpublic $%s; \n" % dato['variable']
        formulario = formulario + html

    return formulario

def getValidacion(datosFormulario):
    formulario = ''

    for dato in datosFormulario:

        html       = "\t\t\t'%s' => '',\n" % dato['variable']
        formulario = formulario + html

    return formulario

def getDB(datosFormulario, tipo):
    formulario = ''
    tablaturas =  '\t\t\t' if (tipo == 'crear') else '\t\t\t\t'

    for dato in datosFormulario:

        html       = "%s'' => $this->%s,\n" % (tablaturas, dato['variable'])
        formulario = formulario + html

    return formulario

def getClaseTipoCrear(variables, validaciones, datosDB):
        return """<?php

use App\Src\Traits\Livewire\CrearHelper;
use Livewire\Component;

class ComponenteEjemplo extends ComponentBase
{
    use CrearHelper;
    
%s\tprotected $listeners = ['confirmationAccepted' => 'confirmado'];
    
    public function confirmado()
    {
        $this->validate($this->reglas());

        if ($this->procesar())
        {
            $this->ocutalFormulario();
            $this->showAlertExito('');
            $this->redireccionar('');
        }
    }

    private function reglas()
    {
        return [
%s\t\t];
        /* Reglas de Ejemplo
            required|numeric|min:1|max:99999999999|exists:cuentas,id
            required|numeric|min:1|max:99999999999|unique:cuentas,id
            |between:1,2 |email |date |bool (buleano)
            image:jpeg,jpg,png|max:1024|dimensions:max_width=199,max_height=53
            (telefono) regex:/^([0-9\-\s])12+$/i
            (cedula) regex:/^([0-9\-\s])13+$/i
        */
    }

    private function procesar() : bool
    {
        $creadoCorrectamente = Manager::crear([
%s\t\t]);

        if ($creadoCorrectamente) return true;
        
        $this->showAlertError('Ha occurido un error. !!!');
        return false;
    }

}
""" % (variables, datosDB, validaciones)

def getClaseTipoEditar(variables, validaciones, datosDB):
        return """<?php

use App\Src\Traits\Livewire\EditarHelper;
use Livewire\Component;

class ComponenteEjemplo extends ComponentBase
{
    use EditarHelper;
    
    public $editarId;
%s\tprotected $listeners = ['confirmationAccepted' => 'confirmado'];

    public function mount(int $editarId)
    {
        $this->editarId = $editarId;
    }

     public function setiarDatos()
    {
        if (null)
        {
//            $datos          = Repo::;
//            $this->posicion = $datos->nombreCampo
        }
    }

    public function confirmado()
    {
        $this->validate($this->reglas());
        
        if ($this->procesar())
        {
            $this->successMessage('Definir mensaje');
        }
    }

    private function reglas()
    {
        return [
%s\t\t];
        /* Reglas de Ejemplo
            required|numeric|min:1|max:99999999999|exists:cuentas,id
            required|numeric|min:1|max:99999999999|unique:cuentas,id
             |between:1,2 |email |date |bool (buleano)
            image:jpeg,jpg,png|max:1024|dimensions:max_width=199,max_height=53
            (telefono) regex:/^([0-9\-\s])12+$/i
            (cedula) regex:/^([0-9\-\s])13+$/i
            'posicion' =>[
                'required', 'min:1', 'max:99999999999',
                Rule::unique('empleados_posiciones')
                    ->ignore($this->posicionEmpleadoId)
            ]
        */
    }

    private function procesar()
    {
         Manager::actualizar(
            $this->editarId,
            [
%s\t\t\t]);
        return true;
    }
}
""" % (variables, datosDB, validaciones)

def crear(formulario, tipo):
    variables    = getVariables(formulario);
    datosDB      = getDB(formulario, tipo);
    validaciones = getValidacion(formulario);
    
    if tipo == 'crear':
        return getClaseTipoCrear(variables, datosDB, validaciones)

    if tipo == 'editar':
        return getClaseTipoEditar(variables, datosDB, validaciones)
    
    return ''