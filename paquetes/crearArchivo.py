def crear(nombreArchivo, contenido):
	fileManager = open(nombreArchivo, 'wb')
	fileManager.write(contenido.encode("ascii"))
	fileManager.close()
