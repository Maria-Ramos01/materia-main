from data.asignaturas import asignaturas
from data.crear_data import crear_data
from data.conexion import leer_datos, insertar_datos
from data.scripts.scripts_asignaturas import listado_asignaturas
from prettytable import PrettyTable
from auxiliares.mensajes import sin_datos

def cargar_listado_asignaturas():
    lista_asignaturas = leer_datos(listado_asignaturas)
    if listado_asignaturas != None:
        return lista_asignaturas

def mostrar_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    tabla_asignaturas = PrettyTable()
    tabla_asignaturas.field_names = [
        'Id', 'Código Asignatura', 'Nombre Asignatura', 'Descripción Asignatura']
    lista = cargar_listado_asignaturas()
    if lista != None:
        for asignatura in lista:
            asignatura_list = list(asignatura)
            if asignatura_list[3] == None:
                asignatura_list[3] = 'Sin Información'
            tabla_asignaturas.add_row(asignatura_list)  # type: ignore
        print(tabla_asignaturas)
    else:
        print(sin_datos)

# READ
def buscar_asignatura():
    busqueda = input('Ingrese asignatura a buscar: ')
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura

def indice_asignatura(busqueda):
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            return i

# CREATE
def agregar_asignatura():
    mostrar_listado_asignaturas()
    codigo_asignatura = input('Ingrese código asignatura: ')
    nombre_asignatura = input('Ingrese nombre asignatura: ')
    descripcion_asignatura = input('Ingrese descripción asignatura: ')
    consulta = '''
        INSERT INTO asignaturas (codigo_asignatura,nombre_asignatura,descripcion_asignatura,habilitado) VALUES
        (%s,%s,%s,%s)
    '''
    valores = (
        codigo_asignatura.upper(),
        nombre_asignatura.title(),
        descripcion_asignatura,
        1)
    
    if codigo_asignatura and nombre_asignatura != '':
        insertar_datos(consulta,valores)

def editar_asignatura():
    mostrar_listado_asignaturas()
    id_asignatura = input('Ingrese ID de la asignatura a editar: ')
    nuevo_codigo = input('Ingrese el nuevo código asignatura: ')
    nuevo_nombre = input('Ingrese el nuevo nombre asignatura: ')
    nueva_descripcion = input('Ingrese la nueva descripción asignatura: ')
    consulta = '''
        UPDATE asignaturas 
        SET codigo_asignatura = %s,
            nombre_asignatura = %s,
            descripcion_asignatura = %s
        WHERE id = %s
    '''
    valores = (
        nuevo_codigo.upper(),
        nuevo_nombre.title(),
        nueva_descripcion,
        id_asignatura
        )
    
    if id_asignatura and nuevo_codigo and nuevo_nombre != '':
        insertar_datos(consulta, valores)
        print('Asignatura actualizada correctamente.')
    else:
        print('Datos inválidos. No se realizó la actualización.')
    

def eliminar_asignatura():
    mostrar_listado_asignaturas()
    id_asignatura = input('Ingrese ID de la asignatura a eliminar: ')
    consulta = '''
        DELETE FROM asignaturas WHERE id = %s
    '''
    valores = (id_asignatura,)
    if id_asignatura != '':
        insertar_datos(consulta, valores)
        print('Asignatura eliminada correctamente.')
    else:
        print('ID inválido. No se realizó la eliminación.')

    mostrar_listado_asignaturas()

