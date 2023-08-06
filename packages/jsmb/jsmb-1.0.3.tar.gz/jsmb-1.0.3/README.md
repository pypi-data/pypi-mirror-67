# JSMB

Paquete de ayuda para usar SAMBA con Python con smb.
Con el puedes listar, descargar, subir y remover archivos de directorios.

Lo primero es definir siempre la conexión y usala como base para todos procesos.

###### Conexion basica:
con = jsmb.jsmb('ip','user','pass')

###### Listar Archivos
list = con.list('Nombre de Carpeta')
for i in range(len(list)):
    print(list[i].filename)


###### Subir archivos a servidor
con.upload('Carpeta Compartida Inicial', 'archivo en tu maquina', 'Ubicacion del Archivo dentro de la carpeta')

###### Descargar archivos del servidor
con.download('Carpeta Compartida Inicial', 'Nombre del archivo en tu maquina', 'Ubicacion del Archivo en Carpeta Inicial')

###### Eliminar archivos del servidor
con.delete('Carpeta Compartida Inicial', 'Ubicacion del Archivo en Carpeta Inicial')

###### Crear carpeta
con.mkdir('Carpeta Compartida Inicial', 'carpeta/subcarpeta/subcarpeta')


Esta es la versión 0.1 de este modulo.

Saludos 
###### Jonatan dos Santos.