from pyodbc import IntegrityError, ProgrammingError

from datos.conexion import Conexion
from dominio.estudiante import Estudiante


class EstuadianteDao:
    _INSERTAR = " INSERT INTO Estudiantes (cedula,nombre,apellido,email,carrera,activo) VALUES ( ?,?,?,?,?,?)"
    @classmethod
    def insertar_estudiante(cls, estudiante):
      #cursor = datos.conexion.Conexion.obtenerCursor()
      respuesta = { 'exito': False, 'mensaje': ''}
      Flag_exito = False
      mensaje = ''
      try:
          with Conexion.obtenerCursor() as cursor:
              datos= (estudiante.cedula, estudiante.nombre, estudiante.apellido,estudiante.email, estudiante.carrera,estudiante.activo)
              cursor.execute(cls._INSERTAR, datos)
              mensaje = 'Ingreso exitoso'
      except IntegrityError as e:
          Flag_exito= True
          #print('la cedula que intenta ingresar ya existe')
          print(e)
          print(str(e))
          if e.__str__().find ('Cedula') > 0:
              print('Cedula ya ingresada')
              mensaje = 'Cedula ya ingresada'
          elif e.__str__().find ('Email') > 0:
              print('Email ya ingresada')
              mensaje = 'Email ya ingresada'
          else:
              print('Error de integridad')
              mensaje = 'Error de integridad'
      except ProgrammingError as e:
          Flag_exito= False
          print('Los datos ingresados no son del tamaño permitido')
          mensaje= 'Los datos ingresados no son del tamaño permitido'
      except Exception as e:
          Flag_exito= False
          print(e)
          respuesta['exito'] = flag_exito
          respuesta['mensaje'] = mensaje
      finally:
          return respuesta



if __name__ == '__main__':
  e1= Estudiante()
  e1.cedula = '0996403317'
  e1.nombre = 'Javier'
  e1.apellido = 'Lindao'
  e1.email = 'jlindao@gmail.com'
  e1.carrera = 'Mark'
  e1.activo = True
  EstuadianteDao.insertar_estudiante(e1)
