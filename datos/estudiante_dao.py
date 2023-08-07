from pyodbc import IntegrityError, ProgrammingError

from datos.conexion import Conexion
from dominio.estudiante import Estudiante


class EstuadianteDao:
    _INSERTAR = " INSERT INTO Estudiantes (cedula,nombre,apellido,email,carrera,activo) VALUES ( ?,?,?,?,?,?)"
    _SELECCIONAR_X_CEDULA = "select id,cedula,nombre,apellido,email,carrera,activo from Estudiantes where cedula = ? "

    @classmethod
    def insertar_estudiante(cls, estudiante):
        # cursor = datos.conexion.Conexion.obtenerCursor()
        respuesta = {'exito': False, 'mensaje': ''}
        Flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera,estudiante.activo)
                cursor.execute(cls._INSERTAR, datos)
                Flag_exito = True
                mensaje = 'Ingreso exitoso'
        except IntegrityError as e:
            Flag_exito = False
            # print('la cedula que intenta ingresar ya existe')
            print(e)
            print(str(e))
            if e.__str__().find('Cedula') > 0:
                print('Cedula ya ingresada')
                mensaje = 'Cedula ya ingresada'
            elif e.__str__().find('Email') > 0:
                print('Email ya ingresada')
                mensaje = 'Email ya ingresada'
            else:
                print('Error de integridad')
                mensaje = 'Error de integridad'
        except ProgrammingError as e:
            Flag_exito = False
            print('Los datos ingresados no son del tamaño permitido')
            mensaje = 'Los datos ingresados no son del tamaño permitido'
        except Exception as e:
            Flag_exito = False
            print(e)
        finally:
            respuesta['exito'] = Flag_exito
            respuesta['mensaje'] = mensaje
            #cursor.close()
            return respuesta

    @classmethod
    def seleccionar_por_cedula(cls, estudiante):
        persona_encontrada = None
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()
                estudiante.id = persona_encontrada[0]
                estudiante.cedula = persona_encontrada[1]
                estudiante.nombre = persona_encontrada[2]
                estudiante.apellido = persona_encontrada[3]
                estudiante.email = persona_encontrada[4]
                estudiante.carrera = persona_encontrada[5]
                estudiante.activo = persona_encontrada[6]
        except Exception as e:
            print(e)
        finally:
            return estudiante




if __name__ == '__main__':
    e1 = Estudiante()
    e1.cedula = '0996403317'
    e1.nombre = 'Javier'
    e1.apellido = 'Lindao'
    e1.email = 'jlindao@gmail.com'
    e1.carrera = 'Mark'
    e1.activo = True
    #EstuadianteDao.insertar_estudiante(e1)
    #EstuadianteDao.seleccionar_por_cedula(e1)
    #print(e1)
    persona_encontrada = EstuadianteDao.seleccionar_por_cedula(e1)
    print(persona_encontrada)