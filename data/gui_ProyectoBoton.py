from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import gui_Spacers
guiSpacers = gui_Spacers.Ui_Spacers()
# # Combobox
# listaItems = ["Guión / Ideas", "Storyboard", "Boceto", "Diseño 2D", "Animación 2D", "Diseño 3D", "Animación 3D", "Render 3D", "Edición Video", "Audio", "Render Video", "Otros", ""]
# pieles = ["Cristal 01", "Cristal 02", "Papel", "Color 01", "Color 02"]


class Ui_ProyectoBoton(object):
    def botonProyecto(self, texto, toolTip, click_pb_show, click_pb_edit, click_pb_del, container, layoutContainer, estilo):
        # --------------------------------------------- Widget base
        self.w_baseP = QWidget(container)
        self.w_baseP.setStyleSheet(estilo['w_baseP'])
        self.w_baseP.setGeometry(QRect(0, 0, 285, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_baseP.sizePolicy().hasHeightForWidth())
        self.w_baseP.setSizePolicy(sizePolicy)
        self.w_baseP.setMinimumSize(QSize(265, 75))
        # --------------------------------------------- Layout de base
        self.hL_baseP = QHBoxLayout(self.w_baseP)
        self.hL_baseP.setContentsMargins(0, 0, 0, 0)
        self.hL_baseP.setSpacing(0)

        # ------------------------------------------------------------------------------------- BASE BOTON EDIT PROYECTO -----------------
        # --------------------------------------------- Widget botones base
        self.w_botonesPBase = QWidget(self.w_baseP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_botonesPBase.sizePolicy().hasHeightForWidth())
        self.w_botonesPBase.setMinimumSize(QSize(37, 75))
        self.w_botonesPBase.setMaximumSize(QSize(37, 75))
        self.w_botonesPBase.setStyleSheet(estilo['w_botonesPBase'])
        # --------------------------------------------- Layout de botones base
        self.vL_botonesPBase = QVBoxLayout(self.w_botonesPBase)
        self.vL_botonesPBase.setContentsMargins(0, 0, 0, 0)
        self.vL_botonesPBase.setSpacing(0)
        self.hL_baseP.addWidget(self.w_botonesPBase, 0, Qt.AlignTop)

        # ------------------------------------------------------------------------------------------ BOTON EDIT PROYECTO -----------------
        self.pb_edit = QPushButton(self.w_baseP)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_edit.sizePolicy().hasHeightForWidth())
        self.pb_edit.setGeometry(QRect(0, 0, 37, 37))
        self.pb_edit.setStyleSheet(estilo['pb_edit_P'])
        # ---------------------------------------------------------------------------------------- BOTON DELETE PROYECTO -----------------
        self.pb_del = QPushButton(self.w_baseP)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_del.sizePolicy().hasHeightForWidth())
        self.pb_del.setGeometry(QRect(0, 0, 37, 37))
        self.pb_del.setStyleSheet(estilo['pb_del_P'])
        self.pb_edit.clicked.connect(click_pb_edit)
        self.pb_del.clicked.connect(click_pb_del)
        self.vL_botonesPBase.addWidget(self.pb_edit)
        self.vL_botonesPBase.addWidget(self.pb_del)

        # ---------------------------------------------------------------------------------------- LABEL NOMBRE PROYECTO -----------------
        self.l_proyecto = QLabel(texto, self.w_baseP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.l_proyecto.sizePolicy().hasHeightForWidth())
        self.l_proyecto.setMinimumSize(QSize(0, 75))
        self.l_proyecto.setAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        self.l_proyecto.setWordWrap(True)
        self.l_proyecto.setToolTip(toolTip)
        self.l_proyecto.setToolTipDuration(50000)
        self.l_proyecto.setStyleSheet(estilo['l_proyecto'])

        # ------------------------------------------------------------------------------------------ BOTON SHOW PROYECTO -----------------
        self.pb_show = QPushButton(self.w_baseP)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_show.sizePolicy().hasHeightForWidth())
        self.pb_show.setMaximumSize(QSize(50, 75))
        self.pb_show.setStyleSheet(estilo['pb_show_P'])
        self.hL_baseP.addWidget(self.l_proyecto)
        self.hL_baseP.addWidget(self.pb_show)
        self.pb_show.clicked.connect(click_pb_show)

        # ---- Agrega el Contenedor (w_base) al Layout pasado por parametro (layoutContainer) --------------------------
        layoutContainer.addWidget(self.w_baseP)

    def botonProyActivo(self, texto, toolTip, click_pb_edit, click_pb_del, container, layoutContainer, estilo):
        # --------------------------------------------- Widget w_baseActivoP
        self.w_baseActivoP = QWidget(container)
        self.w_baseActivoP.setStyleSheet(estilo['w_baseActivoP'])
        self.w_baseActivoP.setGeometry(QRect(0, 0, 285, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_baseActivoP.sizePolicy().hasHeightForWidth())
        self.w_baseActivoP.setSizePolicy(sizePolicy)
        self.w_baseActivoP.setMinimumSize(QSize(265, 75))
        # --------------------------------------------- Layout del w_base
        self.hL_baseActivoP = QHBoxLayout(self.w_baseActivoP)
        self.hL_baseActivoP.setContentsMargins(0, 0, 0, 0)
        self.hL_baseActivoP.setSpacing(0)

        self.w_botonesActBase = QWidget(self.w_baseActivoP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_botonesActBase.sizePolicy().hasHeightForWidth())
        self.w_botonesActBase.setMinimumSize(QSize(37, 75))
        self.w_botonesActBase.setMaximumSize(QSize(37, 75))
        self.w_botonesActBase.setStyleSheet(estilo['w_botonesActBase'])
        self.vL_botonesActBase = QVBoxLayout(self.w_botonesActBase)
        self.vL_botonesActBase.setContentsMargins(0, 0, 0, 0)
        self.vL_botonesActBase.setSpacing(0)
        self.hL_baseActivoP.addWidget(self.w_botonesActBase, 0, Qt.AlignTop)

        self.w_trabajoActBase = QWidget(self.w_baseActivoP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_trabajoActBase.sizePolicy().hasHeightForWidth())
        self.w_trabajoActBase.setMinimumSize(QSize(37, 75))
        self.w_trabajoActBase.setStyleSheet(estilo['w_trabajoActBase'])
        self.vL_trabajoActBase = QVBoxLayout(self.w_trabajoActBase)
        self.vL_trabajoActBase.setContentsMargins(0, 0, 0, 0)
        self.vL_trabajoActBase.setSpacing(0)
        self.hL_baseActivoP.addWidget(self.w_trabajoActBase)

        # ----------------------------------------------------------------------------------- BOTON EDIT PROYECTO ACTIVO -----------------
        self.pb_editAct = QPushButton(self.w_botonesActBase)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_editAct.sizePolicy().hasHeightForWidth())
        self.pb_editAct.setGeometry(QRect(0, 0, 37, 37))
        self.pb_editAct.setStyleSheet(estilo['pb_edit_Pa'])
        # --------------------------------------------------------------------------------- BOTON DELETE PROYECTO ACTIVO -----------------
        self.pb_delAct = QPushButton(self.w_botonesActBase)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_delAct.sizePolicy().hasHeightForWidth())
        self.pb_delAct.setGeometry(QRect(0, 0, 37, 37))
        self.pb_delAct.setStyleSheet(estilo['pb_del_Pa'])
        self.pb_editAct.clicked.connect(click_pb_edit)
        self.pb_delAct.clicked.connect(click_pb_del)
        self.vL_botonesActBase.addWidget(self.pb_editAct)
        self.vL_botonesActBase.addWidget(self.pb_delAct)

        # ---------------------------------------------------------------------------------------- LABEL PROYECTO ACTIVO -----------------
        self.l_proyectoActivo = QLabel(texto, self.w_trabajoActBase)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.l_proyectoActivo.sizePolicy().hasHeightForWidth())
        self.l_proyectoActivo.setMinimumSize(QSize(0, 75))
        self.l_proyectoActivo.setAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        self.l_proyectoActivo.setWordWrap(True)
        self.l_proyectoActivo.setToolTip(toolTip)
        self.l_proyectoActivo.setToolTipDuration(50000)
        self.l_proyectoActivo.setStyleSheet(estilo['l_proyectoActivo'])
        self.vL_trabajoActBase.addWidget(self.l_proyectoActivo)

        self.w_btnTrabContainer = QWidget(self.w_trabajoActBase)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_btnTrabContainer.sizePolicy().hasHeightForWidth())
        self.w_btnTrabContainer.setMinimumSize(QSize(30, 30))
        self.w_btnTrabContainer.setStyleSheet(estilo['w_btnTrabContainer'])
        self.vL_btnTrabContainer = QVBoxLayout(self.w_btnTrabContainer)
        self.vL_btnTrabContainer.setContentsMargins(0, 0, 5, 0)
        self.vL_btnTrabContainer.setSpacing(5)

        self.vL_trabajoActBase.addWidget(self.w_btnTrabContainer)

        # ---- AGREGA UN "Spacer" PARA ALINEAR LA LISTA DE BOTONES A LA PARTE SUPERIOR DEL CONTENEDOR DE LA BOTONERA ----
        guiSpacers.spacer(20, 20, self.vL_trabajoActBase)

        # ---- Agrega el Contenedor (w_base) al Layout pasado por parametro (layoutContainer) --------------------------
        layoutContainer.addWidget(self.w_baseActivoP)

    def botonProyNuevo(self, click_pb_add, container, layoutContainer, estilo):
        self.pb_addProy = QPushButton("+ Nuevo Proyecto", container)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_addProy.sizePolicy().hasHeightForWidth())
        self.pb_addProy.setStyleSheet(estilo['pb_addProy'])
        self.pb_addProy.clicked.connect(click_pb_add)
        # ---- Agrega el boton al Layout ScrollArea de la botonera
        layoutContainer.addWidget(self.pb_addProy)