
def crear(nombreArchivo, contenido):
    fileManager = open(nombreArchivo,'wb')
    fileManager.write(contenido)
    fileManager.close()