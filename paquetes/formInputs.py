# encoding=utf8

def crearInputTextarea(label, variable, tipo):
    error = "{{ $message }}"

    return """
<div class="form-group col-sm-4">
    <label>
        <b>
            {0}
            <span class="text-danger">*</span>
        </b>

        <textarea wire:model.debounce.500ms="{1}" class="form-control" rows="3">
        </textarea>

        @error('{1}')
            <p class="text-danger mt-1 d-flex justify-content-center">{3}</p>
        @enderror
    </label>
</div>
""".format(label, variable, tipo, error)


def crearInputSelect(label, variable, tipo):
     error = "{{ $message }}"

     return """
<div class="form-group col-sm-4">
    <label>
        <b>
            {0}
            <span class="text-danger">*</span>
        </b>

        <select wire:model="{1}" class="form-control">
            <option value="0" selected=""></option>
            @foreach([] as $value)
                <option value="">
                    $value
                </option>
            @endforeach
        </select>

        @error('{1}')
            <p class="text-danger mt-1 d-flex justify-content-center">{3}</p>
        @enderror
    </label>
</div>
""".format(label, variable, tipo, error)

def crearInputSimple(label, variable, tipo):
    
    error = "{{ $message }}"

    return """
<div class="form-group col-sm-4">
    <label>
        <b>
            {0}
            <span class="text-danger">*</span>
        </b>

        <input wire:model.debounce.500ms="{1}" type="{2}" class="form-control">

        @error('{1}')
            <p class="text-danger mt-1 d-flex justify-content-center">{3}</p>
        @enderror
    </label>
</div>
""".format(label, variable, tipo, error)

def crearInput(label, variable, tipo):
 
    if (tipo == 'textarea') :
        return crearInputTextarea(label, variable, tipo)

    if (tipo == 'select') :
        return crearInputSelect(label, variable, tipo)

    return crearInputSimple(label, variable, tipo)