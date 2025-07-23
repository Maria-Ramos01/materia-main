from data.conexion import leer_datos, insertar_datos
from prettytable import PrettyTable
from auxiliares.mensajes import sin_datos

def mostrar_listado_docentes():
    print()
    print('Listado de Docentes')
    consulta = 'SELECT id, nombre_docente, rut_docente, email_docente FROM docentes WHERE habilitado = 1'
    lista = leer_datos(consulta)
    tabla_docentes = PrettyTable()
    tabla_docentes.field_names = ['Id', 'Nombre Docente', 'RUT Docente', 'Email Docente']
    if lista:
        for docente in lista:
            tabla_docentes.add_row(docente)
        print(tabla_docentes)
    else:
        print(sin_datos)

def agregar_docente():
    nombre = input('Ingrese nombre del docente: ')
    rut = input('Ingrese RUT del docente: ')
    email = input('Ingrese email del docente: ')
    consulta = '''
        INSERT INTO docentes (nombre_docente, rut_docente, email_docente, habilitado)
        VALUES (%s, %s, %s, 1)
    '''
    valores = (nombre.title(), rut, email)
    if nombre and rut and email:
        insertar_datos(consulta, valores)
        print('Docente agregado correctamente.')
    else:
        print('Datos inválidos. No se realizó la operación.')

def editar_docente():
    mostrar_listado_docentes()
    id_docente = input('Ingrese el ID del docente a editar: ')
    nuevo_nombre = input('Ingrese el nuevo nombre: ')
    nuevo_rut = input('Ingrese el nuevo RUT: ')
    nuevo_email = input('Ingrese el nuevo email: ')
    consulta = '''
        UPDATE docentes
        SET nombre_docente = %s,
            rut_docente = %s,
            email_docente = %s
        WHERE id = %s
    '''
    valores = (nuevo_nombre.title(), nuevo_rut, nuevo_email, id_docente)
    if id_docente and nuevo_nombre and nuevo_rut and nuevo_email:
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