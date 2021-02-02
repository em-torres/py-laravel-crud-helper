def crear(nombreArchivo, contenido):
	fileManager = open(nombreArchivo, 'wb')
	fileManager.write(contenido.encode("utf-8"))
	fileManager.close()
