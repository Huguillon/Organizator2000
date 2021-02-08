from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class Ui_Reloj(object):
    def reloj(self, wCont, lCont, estilo):
        # ---- Inicia el DateTimeEdit Reloj y Fecha ----
        self.dateTimeEdit = QDateTimeEdit(wCont)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setMinimumSize(QSize(0, 0))
        self.dateTimeEdit.setFocusPolicy(Qt.NoFocus)
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setTimeSpec(Qt.LocalTime)
        self.dateTimeEdit.setStyleSheet(estilo['dateTimeEdit'])
        # self.hL_Reloj.addWidget(self.dateTimeEdit)
        lCont.addWidget(self.dateTimeEdit)