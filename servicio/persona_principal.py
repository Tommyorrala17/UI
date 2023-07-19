from PySide6.QtWidgets import QMainWindow

from UI.vtn_principal import Ui_vtn_principal
from dominio.docente import Docente
from dominio.estudiante import Estudiante


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        self.ui.btn_grabar.clicked.connect(self.grabar)


    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        persona = None
        if tipo_persona == 'Docente':
            persona = Docente()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
        else:
            persona = Estudiante()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()

        archivo = None
        try:
            archivo = open('../venv/archivo.txt', mode='a')
            archivo.write(persona.__str__())
            archivo.write('\n')
        except Exception as e:
            print('No se pudo grabar.')
        finally:
            if archivo:
                archivo.close()
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.stb_estado.showMessage('Grabado con éxito.', 2000)