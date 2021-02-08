from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

# # Combobox
# listaItems = ["Guión / Ideas", "Storyboard", "Boceto", "Diseño 2D", "Animación 2D", "Diseño 3D", "Animación 3D", "Render 3D", "Edición Video", "Audio", "Render Video", "Otros", ""]
# pieles = ["Cristal 01", "Cristal 02", "Papel", "Color 01", "Color 02"]

class Ui_TrabajoBoton(object):
    def botonTrabajo(self, texto, click_pb_show, click_pb_edit, click_pb_del, container, layoutContainer, estilo):
        self.w_trabajo = QWidget(container)
        self.w_trabajo.setGeometry(QRect(0, 0, 28, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_trabajo.sizePolicy().hasHeightForWidth())
        self.w_trabajo.setSizePolicy(sizePolicy)
        self.w_trabajo.setMinimumSize(QSize(0, 0))
        self.w_trabajo.setStyleSheet(estilo['w_trabajo'])
        # ---- Layout del w_trabajo ----
        self.hL_trabajo = QHBoxLayout(self.w_trabajo)
        self.hL_trabajo.setContentsMargins(0, 0, 0, 0)
        self.hL_trabajo.setSpacing(0)
        # ----------------------------------------------------------------------------------------- BOTON DELETE TRABAJO -----------------
        self.pb_trabajoDel = QPushButton(self.w_trabajo)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_trabajoDel.sizePolicy().hasHeightForWidth())
        self.pb_trabajoDel.setGeometry(QRect(0, 0, 30, 30))
        self.pb_trabajoDel.setMinimumSize(30, 30)
        self.pb_trabajoDel.setMaximumSize(30, 30)
        self.pb_trabajoDel.setStyleSheet(estilo['pb_trabajoDel'])
        self.pb_trabajoDel.clicked.connect(click_pb_del)
        self.hL_trabajo.addWidget(self.pb_trabajoDel)
        # ------------------------------------------------------------------------------------------- BOTON EDIT TRABAJO -----------------
        self.pb_trabajoEdit = QPushButton(self.w_trabajo)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_trabajoEdit.sizePolicy().hasHeightForWidth())
        self.pb_trabajoEdit.setGeometry(QRect(0, 0, 30, 30))
        self.pb_trabajoEdit.setMinimumSize(30, 30)
        self.pb_trabajoEdit.setMaximumSize(30, 30)
        self.pb_trabajoEdit.setStyleSheet(estilo['pb_trabajoEdit'])
        self.pb_trabajoEdit.clicked.connect(click_pb_edit)
        self.hL_trabajo.addWidget(self.pb_trabajoEdit)
        # ------------------------------------------------------------------------------------------- BOTON SHOW TRABAJO -----------------
        self.pb_trabajoShow = QPushButton(texto, self.w_trabajo)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.pb_trabajoShow.sizePolicy().hasHeightForWidth())
        self.pb_trabajoShow.setGeometry(QRect(0, 0, 208, 30))
        self.pb_trabajoShow.setMinimumSize(100, 30)
        self.pb_trabajoShow.setStyleSheet(estilo['pb_trabajoShow'])
        self.pb_trabajoShow.clicked.connect(click_pb_show)
        self.hL_trabajo.addWidget(self.pb_trabajoShow)

        layoutContainer.addWidget(self.w_trabajo)

    def botonTrabActivo(self, texto, click_pb_edit, click_pb_del, container, layoutContainer, estilo):
        self.w_trabajoAct = QWidget(container)
        self.w_trabajoAct.setGeometry(QRect(0, 0, 28, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_trabajoAct.sizePolicy().hasHeightForWidth())
        self.w_trabajoAct.setSizePolicy(sizePolicy)
        self.w_trabajoAct.setMinimumSize(QSize(0, 0))
        self.w_trabajoAct.setStyleSheet(estilo['w_trabajoAct'])
        # ---- Layout del w_trabajo ----
        self.hL_trabajoAct = QHBoxLayout(self.w_trabajoAct)
        self.hL_trabajoAct.setContentsMargins(0, 0, 0, 0)
        self.hL_trabajoAct.setSpacing(0)
        # ----------------------------------------------------------------------------------------- BOTON DELETE TRABAJO -----------------
        self.pb_trabajoActDel = QPushButton(self.w_trabajoAct)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_trabajoActDel.sizePolicy().hasHeightForWidth())
        self.pb_trabajoActDel.setGeometry(QRect(0, 0, 30, 30))
        self.pb_trabajoActDel.setMinimumSize(30, 30)
        self.pb_trabajoActDel.setMaximumSize(30, 30)
        self.pb_trabajoActDel.setStyleSheet(estilo['pb_trabajoActDel'])
        self.pb_trabajoActDel.clicked.connect(click_pb_del)
        # ------------------------------------------------------------------------------------------- BOTON EDIT TRABAJO -----------------
        self.pb_trabajoActEdit = QPushButton(self.w_trabajoAct)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_trabajoActEdit.sizePolicy().hasHeightForWidth())
        self.pb_trabajoActEdit.setGeometry(QRect(0, 0, 30, 30))
        self.pb_trabajoActEdit.setMinimumSize(30, 30)
        self.pb_trabajoActEdit.setMaximumSize(30, 30)
        self.pb_trabajoActEdit.setStyleSheet(estilo['pb_trabajoActEdit'])
        self.pb_trabajoActEdit.clicked.connect(click_pb_edit)

        self.hL_trabajoAct.addWidget(self.pb_trabajoActDel)
        self.hL_trabajoAct.addWidget(self.pb_trabajoActEdit)
        # ------------------------------------------------------------------------------------------- LABEL SHOW TRABAJO -----------------
        self.l_trabajoAct = QLabel(texto, self.w_trabajoAct)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.l_trabajoAct.sizePolicy().hasHeightForWidth())
        self.l_trabajoAct.setGeometry(QRect(0, 0, 208, 30))
        self.l_trabajoAct.setMinimumSize(100, 30)
        self.l_trabajoAct.setAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        self.l_trabajoAct.setWordWrap(False)
        self.l_trabajoAct.setStyleSheet(estilo['l_trabajoAct'])
        self.hL_trabajoAct.addWidget(self.l_trabajoAct)

        layoutContainer.addWidget(self.w_trabajoAct)

    def botonTrabajoNuevo(self, click_pb_add, container, layoutContainer, estilo):
        # ----------------------------------------------------------------------------------------- BOTON AGREGA TRABAJO -----------------
        self.pb_trabajoAdd = QPushButton("+ Nuevo Trabajo", container)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.pb_trabajoAdd.sizePolicy().hasHeightForWidth())
        self.pb_trabajoAdd.setGeometry(QRect(0, 0, 208, 30))
        self.pb_trabajoAdd.setMinimumSize(100, 30)
        self.pb_trabajoAdd.setStyleSheet(estilo['pb_trabajoAdd'])
        self.pb_trabajoAdd.clicked.connect(click_pb_add)

        layoutContainer.addWidget(self.pb_trabajoAdd)