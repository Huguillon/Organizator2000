from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class Ui_Dialogos(object):
    def dialogoProyecto(self, ubicacion, vPlaceHolder, txtTitulo, txtDescripcion, txtEncabezado, ubicacionAnterior, maximo, estilo):
        # ---- Ventana de Dialogo ----
        self.dialogP = QDialog(ubicacion)
        self.dialogP.resize(480, 400)
        self.dialogP.setStyleSheet(estilo['dialogP'])
        self.vL_DialogP = QVBoxLayout(self.dialogP)
        self.vL_DialogP.setContentsMargins(20, 20, 20, 20)
        self.vL_DialogP.setSpacing(15)

        #---- Label del encabezado ----
        self.l_dialogEncP = QLabel(txtEncabezado, self.dialogP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_dialogEncP.sizePolicy().hasHeightForWidth())
        self.l_dialogEncP.setSizePolicy(sizePolicy)
        self.l_dialogEncP.setMinimumSize(QSize(0, 40))
        self.l_dialogEncP.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.l_dialogEncP.setWordWrap(True)
        self.l_dialogEncP.setAlignment(Qt.AlignCenter)
        self.l_dialogEncP.setStyleSheet(estilo['l_dialogEncP'])
        self.vL_DialogP.addWidget(self.l_dialogEncP)
        # ------------------------------------------------------------------------------------------- CAMPO TEXTO TITULO -------------------------
        # ---- Widget base para el campo de texto del "TITULO" ----
        self.w_baseTituloP = QWidget(self.dialogP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_baseTituloP.sizePolicy().hasHeightForWidth())
        self.w_baseTituloP.setMinimumSize(QSize(0, 0))
        self.w_baseTituloP.setStyleSheet(estilo['w_baseTituloP'])
        self.vL_w_baseTituloP = QVBoxLayout(self.w_baseTituloP)
        self.vL_w_baseTituloP.setContentsMargins(10, 10, 10, 10)
        self.vL_w_baseTituloP.setSpacing(10)
        self.vL_DialogP.addWidget(self.w_baseTituloP)

        # ---- Label con texto "Titulo" ----
        self.l_TituloP = QLabel("Titulo", self.w_baseTituloP)
        self.l_TituloP.setStyleSheet(estilo['l_TituloP'])
        self.vL_w_baseTituloP.addWidget(self.l_TituloP, 0, Qt.AlignHCenter)

        # ---- LineEdit con el campo de texto del "TITULO" ----
        self.le_TituloP = QLineEdit(self.w_baseTituloP)
        self.le_TituloP.setStyleSheet(estilo['le_TituloP'])
        self.le_TituloP.setFocusPolicy(Qt.StrongFocus)
        self.le_TituloP.setMaxLength(30)
        unPlaceHolder = vPlaceHolder
        if unPlaceHolder == True:
            # PlaceHolder
            self.le_TituloP.setPlaceholderText(txtTitulo)
        else:
            self.le_TituloP.setText(txtTitulo)
        self.vL_w_baseTituloP.addWidget(self.le_TituloP)
        # -------------------------------------------------------------------------------------- CAMPO TEXTO DESCRIPCION -------------------------
        # ---- Widget base para el campo de texto de la "DESCRIPCION" ----
        self.w_baseDescripcionP = QWidget(self.dialogP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_baseDescripcionP.sizePolicy().hasHeightForWidth())
        self.w_baseDescripcionP.setMinimumSize(QSize(0, 0))
        self.w_baseDescripcionP.setStyleSheet(estilo['w_baseDescripcionP'])
        self.vL_w_baseDescripcionP = QVBoxLayout(self.w_baseDescripcionP)
        self.vL_w_baseDescripcionP.setContentsMargins(10, 10, 10, 10)
        self.vL_w_baseDescripcionP.setSpacing(10)
        self.vL_DialogP.addWidget(self.w_baseDescripcionP)

        # ---- Label con texto "Descripcion" ----
        self.l_DescripcionP = QLabel("Descripcion", self.w_baseDescripcionP)
        self.l_DescripcionP.setStyleSheet(estilo['l_DescripcionP'])
        self.vL_w_baseDescripcionP.addWidget(self.l_DescripcionP, 0, Qt.AlignHCenter)

        # ---- TextEdit con el campo de texto de la "DESCRIPCION" ----
        self.te_DescripcionP = QTextEdit(self.w_baseDescripcionP)
        self.te_DescripcionP.setStyleSheet(estilo['te_DescripcionP'])
        if unPlaceHolder == True:
            # PlaceHolder
            self.te_DescripcionP.setPlaceholderText(txtDescripcion)
        else:
            self.te_DescripcionP.setText(txtDescripcion)
        self.vL_w_baseDescripcionP.addWidget(self.te_DescripcionP)
        # --------------------------------------------------------------------------------------------- SPINBOX POSICION -------------------------
        # ---- Widget base para el campo de texto de la "POSICION" ----
        self.w_basePosicion = QWidget(self.dialogP)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_basePosicion.sizePolicy().hasHeightForWidth())
        self.w_basePosicion.setMinimumSize(QSize(0, 0))
        self.w_basePosicion.setStyleSheet(estilo['w_baseDescripcionP'])
        self.vL_w_basePosicion = QHBoxLayout(self.w_basePosicion)
        self.vL_w_basePosicion.setContentsMargins(10, 10, 10, 10)
        self.vL_w_basePosicion.setSpacing(10)
        self.vL_DialogP.addWidget(self.w_basePosicion)

        # ---- Label con texto "Posición" ----
        self.l_Posicion = QLabel("Posición", self.w_basePosicion)
        self.l_Posicion.setStyleSheet(estilo['l_DescripcionP'])
        self.vL_w_basePosicion.addWidget(self.l_Posicion, 0, Qt.AlignHCenter)

        # ---- Widget base para el "SPINBOX" ----
        self.w_spinBox = QWidget(self.w_basePosicion)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_spinBox.sizePolicy().hasHeightForWidth())
        self.w_spinBox.setMinimumSize(QSize(0, 0))
        self.w_spinBox.setMaximumSize(QSize(75, 50))
        self.w_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hL_w_spinBox = QHBoxLayout(self.w_spinBox)
        self.hL_w_spinBox.setContentsMargins(0, 10, 0, 10)
        self.hL_w_spinBox.setSpacing(10)
        self.vL_w_basePosicion.addWidget(self.w_spinBox)

        # # ---- Label con texto ----
        # self.l_Posicion = QLabel("Mover el objeto a la posición: ", self.w_basePosicion)
        # self.l_Posicion.setStyleSheet(estilo['te_DescripcionP'])
        # self.hL_w_spinBox.addWidget(self.l_Posicion, 0, Qt.AlignHCenter)
        #
        # # ---- mySpinBox ----
        # self.w_mySpinBox = QWidget(self.w_basePosicion)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHeightForWidth(self.w_spinBox.sizePolicy().hasHeightForWidth())
        # # self.w_spinBox.setMinimumSize(QSize(5, 2))
        # # self.w_spinBox.setMaximumSize(QSize(100, 50))
        # self.w_spinBox.setStyleSheet("background-color:red;")
        # self.hL_w_mySpinBox = QHBoxLayout(self.w_mySpinBox)
        # self.hL_w_mySpinBox.setContentsMargins(10, 10, 10, 10)
        # self.hL_w_mySpinBox.setSpacing(10)
        # self.hL_w_spinBox.addWidget(self.w_mySpinBox)
        # # ----

        # ---- SpinBox ----
        self.spinBox = QSpinBox(self.w_spinBox)
        # self.spinBox.setGeometry(QRect(100, 10, 41, 21))
        self.spinBox.setGeometry(QRect(0, 0, 30, 30))
        self.spinBox.setFrame(False)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox.setAccelerated(True)
        self.spinBox.setMinimum(0)
        # self.spinBox.setMaximum(500)
        self.spinBox.setMaximum(maximo)
        self.spinBox.setProperty("value", ubicacionAnterior)
        self.spinBox.setStyleSheet("QSpinBox {\b"
                                   "background-color: yellow;"
                                   "font-color:red;"
                                   "padding-right: 15px;\b"
                                   "border-image: url(:/images/frame.png) 4;\b"
                                   "border-width: 3;}\b"
                                   ""
                                   "QSpinBox::up-button{\b"
                                   "subcontrol-origin: border;\b"
                                   "subcontrol-position: top right;\b"
                                   "width: 16px;\b"
                                   "border-image: url(:/images/spinup.png) 1;\b"
                                   "border-width: 1px;}")
        # self.spinBox.setObjectName("spinBox")
        self.hL_w_spinBox.addWidget(self.spinBox, 0, Qt.AlignHCenter)
        # ----------------------------------------------------------------------------------- BOTONES ACEPTAR / CANCELAR -------------------------
        # ---- Botones ----
        self.bb_dialogP = QDialogButtonBox(self.dialogP)
        self.bb_dialogP.setOrientation(Qt.Horizontal)
        self.bb_dialogP.setStandardButtons(QDialogButtonBox.Cancel| QDialogButtonBox.Ok)
        # ---- Cambia el texto escrito en los Botones
        self.bb_dialogP.button(QDialogButtonBox.Ok).setText("Aceptar")
        self.bb_dialogP.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.bb_dialogP.setStyleSheet(estilo['bb_dialogP'])
        self.vL_DialogP.addWidget(self.bb_dialogP)

        # self.retranslateUi(self.dialog)
        self.bb_dialogP.accepted.connect(self.dialogP.accept)
        self.bb_dialogP.rejected.connect(self.dialogP.reject)
        QMetaObject.connectSlotsByName(self.dialogP)
        self.dialogP.show()
        self.rspDialogP = self.dialogP.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo

    def dialogTicket(self, listaItems, dialogT, vPlaceHolder, indexCombo, txtTitulo, txtDescripcion, txtEncabezado, click_pb_itemAdd, estilo):
        # ---- Ventana de Dialogo ----
        dialogT.resize(480, 400)
        dialogT.setWindowTitle(txtEncabezado)
        self.vL_dialogT = QVBoxLayout(dialogT)
        self.vL_dialogT.setContentsMargins(20, 20, 20, 20)
        self.vL_dialogT.setSpacing(15)

        #---- Label del encabezado ----
        self.l_dialogEncT = QLabel(txtEncabezado, dialogT)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_dialogEncT.sizePolicy().hasHeightForWidth())
        self.l_dialogEncT.setSizePolicy(sizePolicy)
        self.l_dialogEncT.setGeometry(QRect(0, 0, 250, 80))
        self.l_dialogEncT.setMinimumSize(QSize(0, 40))
        self.l_dialogEncT.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.l_dialogEncT.setWordWrap(True)
        self.l_dialogEncT.setAlignment(Qt.AlignCenter)
        self.l_dialogEncT.setStyleSheet(estilo['l_dialogEncT'])
        self.vL_dialogT.addWidget(self.l_dialogEncT)

        # ---- Widget base para el contenido COMPLETO ----
        self.w_baseContenidoT = QWidget(dialogT)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_baseContenidoT.sizePolicy().hasHeightForWidth())
        self.w_baseContenidoT.setSizePolicy(sizePolicy)
        self.w_baseContenidoT.setGeometry(QRect(0, 0, 800, 600))
        self.w_baseContenidoT.setStyleSheet(estilo['w_baseContenidoT'])
        self.vH_w_baseContenidoT = QHBoxLayout(self.w_baseContenidoT)
        self.vH_w_baseContenidoT.setContentsMargins(0, 0, 0, 0)
        self.vH_w_baseContenidoT.setSpacing(20)
        self.vL_dialogT.addWidget(self.w_baseContenidoT, 0, Qt.AlignHCenter)

        # ---- Widget base para el contenido "Tipo", "Titulo" y "Descripcion" ----
        self.w_baseDatosT = QWidget(self.w_baseContenidoT)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_baseDatosT.sizePolicy().hasHeightForWidth())
        self.w_baseDatosT.setSizePolicy(sizePolicy)
        self.w_baseDatosT.setGeometry(QRect(0, 0, 515, 600))
        self.w_baseDatosT.setMinimumSize(QSize(515, 0))
        self.w_baseDatosT.setStyleSheet(estilo['w_baseDatosT'])
        self.vL_w_baseDatosT = QVBoxLayout(self.w_baseDatosT)
        self.vL_w_baseDatosT.setContentsMargins(0, 0, 0, 0)
        self.vL_w_baseDatosT.setSpacing(6)
        self.vH_w_baseContenidoT.addWidget(self.w_baseDatosT)

        # ---- Widget base para el contenido "Tipo" y "Titulo" ----
        self.w_baseTipoTituloT = QWidget(self.w_baseDatosT)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_baseTipoTituloT.sizePolicy().hasHeightForWidth())
        self.w_baseTipoTituloT.setSizePolicy(sizePolicy)
        self.w_baseTipoTituloT.setGeometry(QRect(0, 0, 515, 500))
        self.w_baseDatosT.setMinimumSize(QSize(515, 300))
        self.w_baseTipoTituloT.setStyleSheet(estilo['w_baseTipoTituloT'])
        self.vH_w_baseTipoTituloT = QHBoxLayout(self.w_baseTipoTituloT)
        self.vH_w_baseTipoTituloT.setContentsMargins(0, 0, 0, 0)
        self.vH_w_baseTipoTituloT.setSpacing(6)
        self.vL_w_baseDatosT.addWidget(self.w_baseTipoTituloT)

        # --------------------------------------------------------------------------------------------------------------
        # ---- Widget base para el ComboBox ----
        self.w_baseCombo = QWidget(self.w_baseTipoTituloT)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_baseCombo.sizePolicy().hasHeightForWidth())
        self.w_baseCombo.setSizePolicy(sizePolicy)
        self.w_baseCombo.setGeometry(QRect(0, 0, 200, 100))
        self.w_baseCombo.setMinimumSize(QSize(200, 0))
        self.w_baseCombo.setStyleSheet(estilo['w_baseCombo'])
        self.vL_w_baseCombo = QVBoxLayout(self.w_baseCombo)
        self.vL_w_baseCombo.setContentsMargins(10, 10, 10, 10)
        self.vL_w_baseCombo.setSpacing(10)
        self.vH_w_baseTipoTituloT.addWidget(self.w_baseCombo)

        # ---- Label con texto "Tipo" ----
        self.l_TipoT = QLabel("Tipo", self.w_baseCombo)
        self.l_TipoT.setStyleSheet(estilo['l_TipoT'])
        self.vL_w_baseCombo.addWidget(self.l_TipoT, 0, Qt.AlignHCenter)

        self.comboBox_Tipo = QComboBox(self.w_baseCombo)
        self.comboBox_Tipo.setStyleSheet(estilo['comboBox_Tipo'])
        # Combobox
        for tipo in listaItems:
            self.comboBox_Tipo.addItem(tipo)
        self.comboBox_Tipo.setCurrentIndex(indexCombo)
        self.comboBox_Tipo.setMaxVisibleItems(len(listaItems))
        # self.comboBox_Tipo.setStyleSheet(estilo['comboBox_Tipo'])
        self.vL_w_baseCombo.addWidget(self.comboBox_Tipo)
        # --------------------------------------------------------------------------------------------------------------

        # ---- Widget base para el campo de texto del "TITULO" ----
        self.w_baseTituloT = QWidget(self.w_baseTipoTituloT)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_baseTituloT.sizePolicy().hasHeightForWidth())
        self.w_baseTituloT.setSizePolicy(sizePolicy)
        self.w_baseTituloT.setGeometry(QRect(0, 0, 300, 150))
        self.w_baseTituloT.setMinimumSize(QSize(300, 0))
        self.w_baseTituloT.setStyleSheet(estilo['w_baseTituloT'])
        self.vL_w_baseTituloT = QVBoxLayout(self.w_baseTituloT)
        self.vL_w_baseTituloT.setContentsMargins(10, 10, 10, 10)
        self.vL_w_baseTituloT.setSpacing(10)
        self.vH_w_baseTipoTituloT.addWidget(self.w_baseTituloT)

        # ---- Label con texto "Titulo" ----
        self.l_TituloT = QLabel("Titulo", self.w_baseTituloT)
        self.l_TituloT.setStyleSheet(estilo['l_TituloT'])
        self.vL_w_baseTituloT.addWidget(self.l_TituloT, 0, Qt.AlignHCenter)

        # ---- LineEdit con el campo de texto del "TITULO" ----
        self.le_TituloT = QLineEdit(self.w_baseTituloT)
        self.le_TituloT.setStyleSheet(estilo['le_TituloT'])
        self.le_TituloT.setFocusPolicy(Qt.StrongFocus)
        self.le_TituloT.setMaxLength(30)
        unPlaceHolder = vPlaceHolder
        if unPlaceHolder == True:
            # PlaceHolder
            self.le_TituloT.setPlaceholderText(txtTitulo)
        else:
            self.le_TituloT.setText(txtTitulo)
        self.vL_w_baseTituloT.addWidget(self.le_TituloT)

        # ---- Widget base para el campo de texto de la "DESCRIPCION" ----
        self.w_baseDescripcionT = QWidget(self.w_baseDatosT)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_baseDescripcionT.sizePolicy().hasHeightForWidth())
        self.w_baseTituloT.setSizePolicy(sizePolicy)
        self.w_baseDescripcionT.setMinimumSize(QSize(0, 0))
        self.w_baseDescripcionT.setStyleSheet(estilo['w_baseDescripcionT'])
        self.vL_w_baseDescripcionT = QVBoxLayout(self.w_baseDescripcionT)
        self.vL_w_baseDescripcionT.setContentsMargins(10, 10, 10, 10)
        self.vL_w_baseDescripcionT.setSpacing(10)
        self.vL_w_baseDatosT.addWidget(self.w_baseDescripcionT)

        # ---- Label con texto "Descripcion" ----
        self.l_DescripcionT = QLabel("Descripcion", self.w_baseDescripcionT)
        self.l_DescripcionT.setStyleSheet(estilo['l_DescripcionT'])
        self.vL_w_baseDescripcionT.addWidget(self.l_DescripcionT, 0, Qt.AlignHCenter)

        # ---- TextEdit con el campo de texto de la "DESCRIPCION" ----
        self.te_DescripcionT = QTextEdit(self.w_baseDescripcionT)
        self.te_DescripcionT.setStyleSheet(estilo['te_DescripcionT'])
        if unPlaceHolder == True:
            # PlaceHolder
            self.te_DescripcionT.setPlaceholderText(txtDescripcion)
        else:
            self.te_DescripcionT.setText(txtDescripcion)
        self.vL_w_baseDescripcionT.addWidget(self.te_DescripcionT)

        # -------------------------------------------------------------------------------------------------------- ITEMS ------------------------------------------------
        # ---- Widget base para el contenido "Items" ----
        self.w_baseItemsT = QWidget(self.w_baseContenidoT)
        self.w_baseItemsT.setGeometry(QRect(0, 0, 515, 515))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_baseItemsT.sizePolicy().hasHeightForWidth())
        self.w_baseItemsT.setSizePolicy(sizePolicy)
        self.w_baseItemsT.setMinimumSize(QSize(300, 350))
        self.w_baseItemsT.setStyleSheet(estilo['w_baseItemsT'])
        self.vL_w_baseItemsT = QVBoxLayout(self.w_baseItemsT)
        self.vL_w_baseItemsT.setContentsMargins(10, 10, 10, 10)
        self.vL_w_baseItemsT.setSpacing(0)
        self.vH_w_baseContenidoT.addWidget(self.w_baseItemsT)

        # ---- Label con texto "Items" ----
        self.l_itemsT = QLabel("Items", self.w_baseItemsT)
        self.l_itemsT.setStyleSheet(estilo['l_itemsT'])
        self.vL_w_baseItemsT.addWidget(self.l_itemsT, 0, Qt.AlignHCenter)


        # ---- LineEdit con el campo de texto para tipear los items a agregar ----
        self.le_addItem = QLineEdit(self.w_baseItemsT)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.le_addItem.sizePolicy().hasHeightForWidth())
        self.le_addItem.setSizePolicy(sizePolicy)
        self.le_addItem.setStyleSheet(estilo['le_addItem'])
        self.le_addItem.setFocusPolicy(Qt.StrongFocus)
        self.le_addItem.setPlaceholderText("Tipear el Item que se agregará")
        self.vL_w_baseItemsT.addWidget(self.le_addItem)


        # ---- Boton para crear items ----
        self.pb_itemAdd = QPushButton("+ Agregar Item", self.w_baseItemsT)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.pb_itemAdd.sizePolicy().hasHeightForWidth())
        self.pb_itemAdd.setSizePolicy(sizePolicy)
        self.pb_itemAdd.setStyleSheet(estilo['pb_itemAdd'])
        self.pb_itemAdd.clicked.connect(click_pb_itemAdd)
        self.vL_w_baseItemsT.addWidget(self.pb_itemAdd)

        # -------------------------------------------------------- SCROLL INICIA ---------------------------------------
        self.scrollArea = QScrollArea(self.w_baseItemsT)
        self.scrollArea.setWidgetResizable(True)

        # ---- Widget que contiene los items ----
        self.w_Items = QWidget()
        self.w_Items.setGeometry(QRect(0, 0, 230, 350))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_Items.sizePolicy().hasHeightForWidth())
        self.w_Items.setSizePolicy(sizePolicy)
        self.w_Items.setStyleSheet(estilo['w_Items'])

        self.vL_w_Items = QVBoxLayout(self.w_Items)
        self.vL_w_Items.setContentsMargins(10, 10, 10, 10)
        self.vL_w_Items.setSpacing(6)

        self.scrollArea.setWidget(self.w_Items)
        self.vL_w_baseItemsT.addWidget(self.scrollArea)
        # ------------------------------------------------------- SCROLL TERMINA ---------------------------------------

        # ----------------------------------------------------------------------------------- BOTONES ACEPTAR / CANCELAR ------------------------------------------------
        self.bb_dialogT = QDialogButtonBox(dialogT)
        self.bb_dialogT.setOrientation(Qt.Horizontal)
        self.bb_dialogT.setStandardButtons(QDialogButtonBox.Cancel| QDialogButtonBox.Ok)
        # ---- Cambia el texto escrito en los Botones
        self.bb_dialogT.button(QDialogButtonBox.Ok).setText("Aceptar")
        self.bb_dialogT.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.bb_dialogT.setStyleSheet(estilo['bb_dialogT'])
        self.vL_dialogT.addWidget(self.bb_dialogT)

        self.bb_dialogT.accepted.connect(dialogT.accept)
        self.bb_dialogT.rejected.connect(dialogT.reject)
        QMetaObject.connectSlotsByName(dialogT)

    def btnDialogItem(self, texto, del_btn, edit_btn, wCont, lCont, estilo):
        self.w_unItem = QWidget(wCont)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_unItem.sizePolicy().hasHeightForWidth())
        self.w_unItem.setSizePolicy(sizePolicy)
        self.w_unItem.setMinimumSize(QSize(150, 25))
        self.w_unItem.setStyleSheet(estilo['w_unItem'])
        self.hL_w_unItem = QHBoxLayout(self.w_unItem)
        self.hL_w_unItem.setContentsMargins(0, 0, 0, 0)
        self.hL_w_unItem.setSpacing(2)

        self.ltxt = QLabel(self.w_unItem)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.ltxt.sizePolicy().hasHeightForWidth())
        self.ltxt.setSizePolicy(sizePolicy)
        self.ltxt.setStyleSheet(estilo['ltxt'])
        self.ltxt.setText(str(texto))

        self.editB = QPushButton(self.w_unItem)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editB.sizePolicy().hasHeightForWidth())
        self.editB.setMaximumSize(30, 25)
        self.editB.setMinimumSize(30, 25)
        self.editB.setStyleSheet(estilo['editB'])

        self.delB = QPushButton(self.w_unItem)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delB.sizePolicy().hasHeightForWidth())
        self.delB.setMaximumSize(30, 25)
        self.delB.setMinimumSize(30, 25)
        self.delB.setStyleSheet(estilo['delB'])

        self.hL_w_unItem.addWidget(self.ltxt)
        self.hL_w_unItem.addWidget(self.editB)
        self.hL_w_unItem.addWidget(self.delB)
        self.delB.clicked.connect(del_btn)
        self.editB.clicked.connect(edit_btn)
        lCont.addWidget(self.w_unItem)

    def dialogItem(self, dialogI, itemAnterior, estilo):
        dialogI.resize(240, 95)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogI.sizePolicy().hasHeightForWidth())
        dialogI.setSizePolicy(sizePolicy)
        dialogI.setMinimumSize(QtCore.QSize(240, 95))
        dialogI.setMaximumSize(QtCore.QSize(240, 95))

        self.buttonBox = QDialogButtonBox(dialogI)
        self.buttonBox.setGeometry(QtCore.QRect(20, 50, 199, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        # ---- Cambia el texto escrito en los Botones
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Aceptar")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.buttonBox.setStyleSheet(estilo['buttonBox'])

        self.lE_Item = QLineEdit(dialogI)
        self.lE_Item.setGeometry(QtCore.QRect(20, 20, 201, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lE_Item.sizePolicy().hasHeightForWidth())
        self.lE_Item.setSizePolicy(sizePolicy)
        self.lE_Item.setStyleSheet(estilo['lE_Item'])
        self.lE_Item.setText(itemAnterior)

        self.buttonBox.accepted.connect(dialogI.accept)
        self.buttonBox.rejected.connect(dialogI.reject)
        QMetaObject.connectSlotsByName(dialogI)

    def dialogSort(self, dialogI, ubicacionAnterior, maximo, estilo):
        dialogI.resize(240, 95)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogI.sizePolicy().hasHeightForWidth())
        dialogI.setSizePolicy(sizePolicy)
        dialogI.setMinimumSize(QtCore.QSize(240, 95))
        dialogI.setMaximumSize(QtCore.QSize(240, 95))

        self.buttonBox = QDialogButtonBox(dialogI)
        self.buttonBox.setGeometry(QtCore.QRect(20, 50, 199, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        # ---- Cambia el texto escrito en los Botones
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Re ordenar")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.buttonBox.setStyleSheet(estilo['buttonBox'])

        self.spinBox = QSpinBox(dialogI)
        self.spinBox.setGeometry(QRect(100, 10, 41, 21))
        self.spinBox.setFrame(False)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox.setAccelerated(True)
        self.spinBox.setMinimum(0)
        # self.spinBox.setMaximum(500)
        self.spinBox.setMaximum(maximo)
        self.spinBox.setProperty("value", ubicacionAnterior)
        # self.spinBox.setObjectName("spinBox")

        # self.lE_Item = QLineEdit(dialogI)
        # self.lE_Item.setGeometry(QtCore.QRect(20, 20, 201, 20))
        # sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.lE_Item.sizePolicy().hasHeightForWidth())
        # self.lE_Item.setSizePolicy(sizePolicy)
        # self.lE_Item.setStyleSheet(estilo['lE_Item'])
        # self.lE_Item.setText(ubicacionAnterior)

        self.buttonBox.accepted.connect(dialogI.accept)
        self.buttonBox.rejected.connect(dialogI.reject)
        QMetaObject.connectSlotsByName(dialogI)
