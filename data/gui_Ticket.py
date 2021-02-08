from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import sys

# ---- Importa los modulos que estan dentro del directorio "data" ----
sys.path.insert(0, '/data/')
from data import gui_Spacers
spacers = gui_Spacers.Ui_Spacers()

class Ui_Ticket(object):
    def ticket(self, listaItems, tipoSel, titulo, descripcion, click_pb_del, click_pb_edit, click_pb_copy, click_pb_sort, click_pb_infoT, numIndex, container, layoutContainer, posFila, posCol, estilo):
        # ---- WIDGET contenedor y color base de los tickets ----
        self.w_Ticket = QWidget(container)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_Ticket.sizePolicy().hasHeightForWidth())
        self.w_Ticket.setSizePolicy(sizePolicy)
        self.w_Ticket.setGeometry(QRect(0, 0, 300, 188))
        self.w_Ticket.setMinimumSize(QSize(300, 188))
        self.hL_w_Ticket = QHBoxLayout(self.w_Ticket)
        self.hL_w_Ticket.setContentsMargins(12, 12, 12, 0)
        self.hL_w_Ticket.setSpacing(0)
        # ////////////////////////////////////////////////////////////////////////////////////////// WIDGET DE CONTENIDO /////////////////
        self.w_tktData = QWidget(self.w_Ticket)
        self.w_tktData.setStyleSheet(estilo['w_tktData'])
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_tktData.sizePolicy().hasHeightForWidth())
        self.w_tktData.setSizePolicy(sizePolicy)
        self.w_tktData.setMinimumSize(QSize(0, 0))
        self.vL_w_tktData = QVBoxLayout(self.w_tktData)
        self.vL_w_tktData.setContentsMargins(0, 0, 0, 0)
        self.vL_w_tktData.setSpacing(0)
        self.hL_w_Ticket.addWidget(self.w_tktData)
        # ------------------------------------------------------------------------------------------------- LABEL TITULO -----------------
        self.l_Titulo = QLabel(self.w_tktData)
        self.l_Titulo.setText(titulo)
        self.l_Titulo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.l_Titulo.setWordWrap(True)
        self.vL_w_tktData.addWidget(self.l_Titulo)
        # --------------------------------------------------------------------------------------------------- LABEL TIPO -----------------
        self.l_Tipo = QLabel(self.w_tktData)
        # self.l_Tipo.setText(listaItems[tipoSel])
        self.l_Tipo.setText(listaItems[tipoSel])
        self.l_Tipo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.l_Tipo.setWordWrap(True)
        self.vL_w_tktData.addWidget(self.l_Tipo)
        # ---------------------------------------------------------------------------------------- WIDGET CONTIENE ITEMS -----------------
        self.w_itemContainer = QWidget(self.w_tktData)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_itemContainer.sizePolicy().hasHeightForWidth())
        self.w_itemContainer.setSizePolicy(sizePolicy)
        self.w_itemContainer.setMinimumSize(QSize(0, 50))
        self.w_itemContainer.setStyleSheet(estilo['w_itemContainer'])
        self.vL_w_itemContainer = QVBoxLayout(self.w_itemContainer)
        self.vL_w_itemContainer.setContentsMargins(0, 0, 0, 0)
        self.vL_w_itemContainer.setSpacing(3)

        self.vL_w_tktData.addWidget(self.w_itemContainer)
        # --------------------------------------------------------------------------------- ESPACIADO AJUSTA DATA ARRIBA -----------------
        spacers.spacer(20, 20, self.vL_w_tktData)

        # /////////////////////////////////////////////////////////////////////////////////////////// WIDGET DE BOTONERA /////////////////
        self.w_Botones = QWidget(self.w_Ticket)
        self.w_Botones.setStyleSheet(estilo['w_Botones'])
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_Botones.sizePolicy().hasHeightForWidth())
        self.w_Botones.setSizePolicy(sizePolicy)
        self.w_Botones.setMinimumSize(QSize(30, 90))
        self.vL_w_Botones = QVBoxLayout(self.w_Botones)
        self.vL_w_Botones.setContentsMargins(0, 0, 0, 0)
        self.vL_w_Botones.setSpacing(0)
        self.hL_w_Ticket.addWidget(self.w_Botones)
        # ---------------------------------------------------------------------------------------- BOTON ELIMINAR TICKET -----------------
        self.pb_delT = QPushButton("", self.w_Botones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_delT.sizePolicy().hasHeightForWidth())
        self.pb_delT.setMinimumSize(QSize(30, 30))
        self.pb_delT.setStyleSheet(estilo['pb_delT'])
        self.pb_delT.clicked.connect(click_pb_del)
        self.vL_w_Botones.addWidget(self.pb_delT)
        # -------------------------------------------------------------------------------------------- BOTON EDIT TICKET -----------------
        self.pb_editT = QPushButton("", self.w_Botones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_editT.sizePolicy().hasHeightForWidth())
        self.pb_editT.setMinimumSize(QSize(30, 30))
        self.pb_editT.setStyleSheet(estilo['pb_editT'])
        self.pb_editT.clicked.connect(click_pb_edit)
        self.vL_w_Botones.addWidget(self.pb_editT)
        # ---------------------------------------------------------------------------------------- BOTON DUPLICAR TICKET -----------------
        self.pb_copyT = QPushButton("", self.w_Botones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_copyT.sizePolicy().hasHeightForWidth())
        self.pb_copyT.setMinimumSize(QSize(30, 30))
        self.pb_copyT.setStyleSheet(estilo['pb_copyT'])
        self.pb_copyT.clicked.connect(click_pb_copy)
        self.vL_w_Botones.addWidget(self.pb_copyT)
        # ------------------------------------------------------------------------------------------- BOTON MOVER TICKET -----------------
        self.pb_sortT = QPushButton(numIndex, self.w_Botones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_sortT.sizePolicy().hasHeightForWidth())
        self.pb_sortT.setMinimumSize(QSize(30, 30))
        self.pb_sortT.setStyleSheet(estilo['pb_sortT'])
        self.pb_sortT.clicked.connect(click_pb_sort)
        self.vL_w_Botones.addWidget(self.pb_sortT)
        # -------------------------------------------------------------------------------------------- BOTON INFO TICKET -----------------
        self.pb_infoT = QPushButton(self.w_Botones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_infoT.sizePolicy().hasHeightForWidth())
        self.pb_infoT.setMinimumSize(QSize(30, 30))
        self.pb_infoT.setToolTip(descripcion)
        self.pb_infoT.setEnabled(True)
        self.pb_infoT.setStyleSheet(estilo['pb_infoT'])
        self.pb_infoT.clicked.connect(click_pb_infoT)
        self.vL_w_Botones.addWidget(self.pb_infoT)
        # ------------------------------------------------------------------------------ ESPACIADO AJUSTA BOTONES ARRIBA -----------------
        spacers.spacer(10, 5, self.vL_w_Botones)

        if tipoSel == 0:
            # # -------- COLOR A
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_0'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_0'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_0'])
        elif tipoSel == 1:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_1'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_1'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_1'])
        elif tipoSel == 2:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_2'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_2'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_2'])
        elif tipoSel == 3:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_3'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_3'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_3'])
        elif tipoSel == 4:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_4'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_4'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_4'])
        elif tipoSel == 5:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_5'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_5'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_5'])
        elif tipoSel == 6:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_6'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_6'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_6'])
        elif tipoSel == 7:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_7'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_7'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_7'])
        elif tipoSel == 8:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_8'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_8'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_8'])
        elif tipoSel == 9:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_9'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_9'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_9'])
        elif tipoSel == 10:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_10'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_10'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_10'])
        elif tipoSel == 11:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_11'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_11'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_11'])
        else:
            self.w_Ticket.setStyleSheet(estilo['w_Ticket_else'])
            self.l_Titulo.setStyleSheet(estilo['l_Titulo_else'])
            self.l_Tipo.setStyleSheet(estilo['l_Tipo_else'])

        # -------------------------------------------------------------------------- EL LAYOUT DEL MAIN AGREGA EL TICKET -----------------
        layoutContainer.addWidget(self.w_Ticket, posFila, posCol, 1, 1, Qt.AlignTop)

    def ticketNuevo(self, click_pb_add, container, layoutContainer, posFila, posCol, estilo):
        self.pb_addTicket = QPushButton("+ Nuevo Ticket", container)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.pb_addTicket.sizePolicy().hasHeightForWidth())
        self.pb_addTicket.setSizePolicy(sizePolicy)
        self.pb_addTicket.setGeometry(QRect(0, 0, 300, 188))
        self.pb_addTicket.setMinimumSize(QSize(300, 188))
        self.pb_addTicket.setStyleSheet(estilo['pb_addTicket'])
        self.pb_addTicket.clicked.connect(click_pb_add)
        layoutContainer.addWidget(self.pb_addTicket, posFila, posCol, 1, 1, Qt.AlignTop)

    def items(self, texto, estado, chck_click, color):
        self.cBox = QCheckBox(texto, self.w_itemContainer)
        self.cBox.setChecked(estado)
        self.cBox.setStyleSheet(color)
        self.cBox.toggle()
        self.cBox.stateChanged.connect(chck_click)
        self.vL_w_itemContainer.addWidget(self.cBox, 0, Qt.AlignTop)
