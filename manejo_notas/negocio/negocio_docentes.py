from data.conexion import leer_datos, insertar_datos
from prettytable import PrettyTable
from auxiliares.mensajes import sin_datos

def mostrar_listado_docentes():
    print()
    print('Listado de Docentes')
    consulta = 'SELECT id, nombre_docente FROM docentes WHERE habilitado = 1'
    lista = leer_datos(consulta)
    tabla_docentes = PrettyTable()
    tabla_docentes.field_names = ['Id', 'Nombre Docente']
    if lista:
        for docente in lista:
            tabla_docentes.add_row(docente)
        print(tabla_docentes)
    else:
        print(sin_datos)

def agregar_docente():
    nombre = input('Ingrese nombre del docente: ')
    consulta = '''
        INSERT INTO docentes (nombre_docente, habilitado)
        VALUES (%s, 1)
    '''
    valores = (nombre.title(),)
    if nombre:
        insertar_datos(consulta, valores)
        print('Docente agregado correctamente.')
    else:
        print('Datos inválidos. No se realizó la operación.')

def editar_docente():
    mostrar_listado_docentes()
    id_docente = input('Ingrese el ID del docente a editar: ')
    nuevo_nombre = input('Ingrese el nuevo nombre: ')
    consulta = '''
        UPDATE docentes
        SET nombre_docente = %s
        WHERE id = %s
    '''
    valores = (nuevo_nombre.title(), id_docente)
    if id_docente and nuevo_nombre:
        insertar_datos(consulta, valores)
        print('Docente actualizado correctamente.')
    else:
        print('Datos inválidos. No se realizó la actualización.')

def eliminar_docente():
    mostrar_listado_docentes()
    id_docente = input('Ingrese el ID del docente a eliminar: ')
    consulta = 'DELETE FROM docentes WHERE id = %s'
    valores = (id_docente,)
    if id_docente:
        insertar_datos(consulta, valores)
        print('Docente eliminado correctamente.')
    else:
        print('ID inválido. No se realizó la eliminación.')