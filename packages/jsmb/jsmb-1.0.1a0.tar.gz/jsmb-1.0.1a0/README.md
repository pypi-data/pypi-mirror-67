# JSMB

Paquete de ayuda para usar SAMBA con Python con smb.

Con el puedes listar, descargar, subir y remover archivos de directorios.

Usando cualquier sistema operacional.

Ejemplos:

Conexión:

con = jsmb.jsmb('ip','user','pass')

Listar Archivos
list = con.list('Nombre de Carpeta')
for i in range(len(list)):
    print(a[i].filename)

Subir archivos a servidor
list = con.upload('Carpeta Compartida Inicial', 'archivo en tu maquina', 'Ubicacion del Archivo dentro de la carpeta')

Descargar archivos del servidor
list = con.download('Carpeta Compartida Inicial', 'Nombre del archivo en tu maquina', 'Ubicacion del Archivo en Carpeta Inicial')

Eliminar archivos del servidor
list = con.delete('Carpeta Compartida Inicial', 'Ubicacion del Archivo en Carpeta Inicial')


Esta es la versión 0.1 de este modulo.

Saludos Jonatan dos Santos.