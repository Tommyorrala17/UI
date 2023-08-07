# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(800, 600)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(270, 100, 281, 41))
        self.txt_nombre.setMaxLength(50)
        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(270, 170, 291, 41))
        self.txt_apellido.setMaxLength(50)
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(170, 95, 61, 41))
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(170, 170, 61, 41))
        self.vtn_grabar = QPushButton(self.centralwidget)
        self.vtn_grabar.setObjectName(u"vtn_grabar")
        self.vtn_grabar.setGeometry(QRect(310, 470, 93, 28))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(164, 260, 71, 21))
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(164, 320, 81, 31))
        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(270, 250, 291, 41))
        self.txt_cedula.setMaxLength(10)
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(270, 320, 291, 41))
        self.txt_email.setMaxLength(100)
        self.lbl_tipo_persona = QLabel(self.centralwidget)
        self.lbl_tipo_persona.setObjectName(u"lbl_tipo_persona")
        self.lbl_tipo_persona.setGeometry(QRect(170, 40, 55, 16))
        self.cb_tipo_persona = QComboBox(self.centralwidget)
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.setObjectName(u"cb_tipo_persona")
        self.cb_tipo_persona.setGeometry(QRect(270, 30, 281, 41))
        self.lbl_carrera = QLabel(self.centralwidget)
        self.lbl_carrera.setObjectName(u"lbl_carrera")
        self.lbl_carrera.setEnabled(True)
        self.lbl_carrera.setGeometry(QRect(160, 400, 81, 31))
        self.txt_carrera = QLineEdit(self.centralwidget)
        self.txt_carrera.setObjectName(u"txt_carrera")
        self.txt_carrera.setGeometry(QRect(270, 390, 291, 41))
        self.txt_carrera.setAcceptDrops(False)
        self.txt_carrera.setMaxLength(50)
        self.btn_buscar_cedula = QPushButton(self.centralwidget)
        self.btn_buscar_cedula.setObjectName(u"btn_buscar_cedula")
        self.btn_buscar_cedula.setGeometry(QRect(630, 260, 121, 31))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.mnb_menu_principal = QMenuBar(vtn_principal)
        self.mnb_menu_principal.setObjectName(u"mnb_menu_principal")
        self.mnb_menu_principal.setGeometry(QRect(0, 0, 800, 26))
        vtn_principal.setMenuBar(self.mnb_menu_principal)
        self.stb_estado = QStatusBar(vtn_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_principal.setStatusBar(self.stb_estado)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"ventana principal", None))
        self.txt_nombre.setText("")
        self.txt_apellido.setText("")
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"NOMBRE:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"APELLIDO:", None))
        self.vtn_grabar.setText(QCoreApplication.translate("vtn_principal", u"GRABAR", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"CEDULA:", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"EMAIL:", None))
        self.txt_cedula.setText("")
        self.txt_email.setText("")
        self.lbl_tipo_persona.setText(QCoreApplication.translate("vtn_principal", u"TIPO:", None))
        self.cb_tipo_persona.setItemText(0, QCoreApplication.translate("vtn_principal", u"DOCENTE", None))
        self.cb_tipo_persona.setItemText(1, QCoreApplication.translate("vtn_principal", u"ESTUDIANTE", None))

        self.lbl_carrera.setText(QCoreApplication.translate("vtn_principal", u"Carrera:", None))
        self.txt_carrera.setText("")
        self.btn_buscar_cedula.setText(QCoreApplication.translate("vtn_principal", u"Consultar Cedula", None))
    # retranslateUi

