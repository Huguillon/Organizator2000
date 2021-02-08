from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class ui_assets():
    # *************************************************** BOTONES ******************************************************
    # ---- Boton de Proyecto que va en la botonera ----
    def BotonProyecto(self, texto, click_btn_proj, click_btn_del, scrollContainer, layoutContainer):
        # ---- WIDGET de base que contiene al resto de los objetos y da color y forma al fondo del botón
        #      y se lo agrega al contenedor pasado por parametro (scrollContainer) ----
        self.w_base = QWidget(scrollContainer)
        self.w_base.setStyleSheet("background-color:rgb(37, 37, 37); border-radius:18px;")
        self.w_base.setGeometry(QRect(0, 0, 285, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_base.sizePolicy().hasHeightForWidth())
        self.w_base.setSizePolicy(sizePolicy)
        self.w_base.setMinimumSize(QSize(265, 75))

        # ---- HORIZONTAL LAYOUT 1 conteniendo el Boton de Eliminar (btn_del) y el Label con el titulo ----
        self.hL_w_base1 = QHBoxLayout(self.w_base)
        self.hL_w_base1.setContentsMargins(30, 0, 12, 0)
        self.hL_w_base1.setSpacing(0)
        #self.hL_w_base1.setAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)

        # ---- HORIZONTAL LAYOUT 2 conteniendo el Boton de Proyectos (btn_proj) ----
        self.hL_w_base2 = QHBoxLayout(self.w_base)
        self.hL_w_base2.setContentsMargins(0, 0, 0, 0)
        self.hL_w_base2.setSpacing(0)

        # ---- LABEL con el Titulo del Proyecto ----
        self.lbl = QLabel("", self.w_base)
        self.lbl.setStyleSheet("background-color:rgba(255, 0, 0, 0);\n"
                               "color:rgb(85, 85, 85);\n"
                               "border-radius:0px;")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.lbl.sizePolicy().hasHeightForWidth())
        self.lbl.setSizePolicy(sizePolicy)
        self.lbl.setMinimumSize(QSize(0, 75))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        self.lbl.setWordWrap(True)
        self.lbl.setText(texto)
        self.hL_w_base1.addWidget(self.lbl, 0, Qt.AlignRight)

        # ---- PUSH BUTTON para eliminar Proyecto ----
        self.btn_del = QPushButton("", self.w_base)
        self.btn_del.setStyleSheet("QPushButton{\n"
                                    "background-image:url('images/del_project.png');\n"
                                    "background-color:rgba(255, 255, 0, 0);\n"
                                    "border-radius:none;\n"
                                    "width:52px;\n"
                                    "height:52px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{\n"
                                    "background-image:url('images/del_project_over.png');\n"
                                    "color:black;\n"
                                    "}\n"
                                    "QPushButton:Pressed{\n"
                                    "background-image:url('images/del_project.png');\n"
                                    "color:white;\n"
                                    "}")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMinimumSize(QSize(52, 52))
        self.hL_w_base1.addWidget(self.btn_del, 0, Qt.AlignRight)
        self.btn_del.clicked.connect(click_btn_del)

        # ---- PUSH BUTTON para ver el Proyecto ----
        self.btn_proj = QPushButton("", self.w_base)
        self.btn_proj.setGeometry(QRect(0, 0, 285, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_proj.sizePolicy().hasHeightForWidth())
        self.btn_proj.setSizePolicy(sizePolicy)
        self.btn_proj.setMinimumSize(QSize(0, 75))
        self.btn_proj.setStyleSheet("QPushButton{\n"
                                    "background-color:rgba(0, 0, 0, 0);\n"
                                    "border-radius:none;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{\n"
                                    "background-color:rgba(125, 200, 25, 25);\n"
                                    "border-radius:20px;\n"
                                    "}")
        self.hL_w_base2.addWidget(self.btn_proj)
        self.btn_proj.clicked.connect(click_btn_proj)

        # ---- Pone el Boton Eliminar (btn_del) por delante del resto ----
        self.btn_del.raise_()

        # ---- Agrega el Contenedor (w_base) al Layout pasado por parametro (layoutContainer) ----
        layoutContainer.addWidget(self.w_base)

    # ---- Boton de Proyecto ACTIVO, que no es clickeable y muestra el proyecto que se ha seleccionado ----
    def BotonActivo(self, texto, click_btn_del, scrollContainer, layoutContainer):
        # ---- WIDGET de base que contiene al resto de los objetos y da color y forma al fondo del botón
        #      y se lo agrega al contenedor pasado por parametro (scrollContainer) ----
        self.w_base = QWidget(scrollContainer)
        self.w_base.setStyleSheet("background-color:rgba(37, 37, 37, 0); border-radius:18px;")
        self.w_base.setGeometry(QRect(0, 0, 285, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_base.sizePolicy().hasHeightForWidth())
        self.w_base.setSizePolicy(sizePolicy)
        self.w_base.setMinimumSize(QSize(265, 75))
        # ---- HORIZONTAL LAYOUT 1 conteniendo el Boton de Eliminar (btn_del) y el Label con el titulo ----
        self.hL_w_base1 = QHBoxLayout(self.w_base)
        self.hL_w_base1.setContentsMargins(30, 0, 12, 0)
        self.hL_w_base1.setSpacing(0)
        # ---- LABEL con el Titulo del Proyecto ----
        self.lbl = QLabel("", self.w_base)
        self.lbl.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                               "color:rgb(125, 200, 25);\n"
                               "border-radius:none;")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHeightForWidth(self.lbl.sizePolicy().hasHeightForWidth())
        self.lbl.setSizePolicy(sizePolicy3)
        self.lbl.setMinimumSize(QSize(0, 75))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        self.lbl.setWordWrap(True)
        self.lbl.setText(texto)
        self.hL_w_base1.addWidget(self.lbl, 0, Qt.AlignRight)
        # ---- PUSH BUTTON para eliminar Proyecto ----
        self.btn_del = QPushButton("", self.w_base)
        self.btn_del.setStyleSheet("QPushButton{\n"
                                    "background-image:url('images/del_project.png');\n"
                                    "background-color:rgba(0, 0, 0, 0);\n"
                                    "border-radius:none;\n"
                                    "width:52px;\n"
                                    "height:52px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{\n"
                                    "background-image:url('images/del_project_over.png');\n"
                                    "color:black;\n"
                                    "}\n"
                                    "QPushButton:Pressed{\n"
                                    "background-image:url('images/del_project.png');\n"
                                    "color:white;\n"
                                    "}")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMinimumSize(QSize(0, 52))
        self.hL_w_base1.addWidget(self.btn_del, 0, Qt.AlignRight)
        self.btn_del.clicked.connect(click_btn_del)
        # ---- Pone el Boton Eliminar (btn_del) por delante del resto ----
        self.btn_del.raise_()
        # ---- Agrega el Contenedor (w_base) al Layout pasado por parametro (layoutContainer) ----
        layoutContainer.addWidget(self.w_base)

    # ---- Boton para generar un nuevo Proyecto que va en la botonera ----
    def BotonAgregar(self, click_btn_add, scrollContainer, layoutContainer):
        self.btn_add = QPushButton("Nuevo\n Proyecto", scrollContainer)
        self.btn_add.setStyleSheet("QPushButton{\n"
                                    "background-image:url('images/add_project.png');\n"
                                    "background-repeat: no-repeat;\n"
                                    "background-position: right;\n"
                                    "background-color:rgba(125, 0, 0, 255);\n"
                                    "color:rgba(255, 255, 255, 75);\n"
                                    "border-radius:20px;\n"
                                    "font-family:'Calibri';\n"
                                    "font-size:17pt;\n"
                                    "font-weight:normal;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{\n"
                                    "background-color:rgba(82, 131, 16, 255);\n"
                                    "color:rgba(255, 255, 255, 75);\n"
                                    "}\n"
                                    "QPushButton:Pressed{\n"
                                    "background-color:rgba(62, 111, 0, 255);\n"
                                    "color:rgba(255, 255, 255, 75);\n"
                                    "}")
        self.btn_add.setMinimumSize(QSize(265, 75))
        self.btn_add.clicked.connect(click_btn_add)
        layoutContainer.addWidget(self.btn_add)

    def BotonEditar(self, click_btn_edit, scrollContainer, layoutContainer):
        self.btn_edit = QPushButton("", scrollContainer)
        self.btn_edit.setStyleSheet("QPushButton{\n"
                                   "background-image:url('images/edit_project.png');\n"
                                   "background-color:rgba(0, 0, 0, 0);\n"
                                   "border-radius:none;\n"
                                   "width:35px;\n"
                                   "height:35px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:Hover{\n"
                                   "background-image:url('images/edit_project_over.png');\n"
                                   "color:black;\n"
                                   "}\n"
                                   "QPushButton:Pressed{\n"
                                   "background-image:url('images/edit_project.png');\n"
                                   "color:white;\n"
                                   "}")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setMinimumSize(QSize(35, 35))
        self.btn_edit.clicked.connect(click_btn_edit)
        #layoutContainer.addWidget(self.btn_edit, 0, Qt.AlignRight)
        layoutContainer.addWidget(self.btn_edit, 0, Qt.AlignBottom)


    # ******************************************************************************************************************************************************************
    # **************************************************** TICKETS *****************************************************************************************************

    def Ticket(self, tipoSel, titulo, descripcion, click_btn_edit, click_btn_del, posFila, posCol, scrollContainer, layoutContainer):
        # ---- WIDGET contenedor y color base de los tickets ----
        self.w_Ticket = QWidget(scrollContainer)
        self.w_Ticket.setGeometry(QRect(0, 0, 504, 230))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_Ticket.sizePolicy().hasHeightForWidth())
        self.w_Ticket.setSizePolicy(sizePolicy)
        self.w_Ticket.setMinimumSize(QSize(504, 230))
        self.w_Ticket.setStyleSheet("background-color: rgb(204, 204, 204);\n"
                                    "border-radius:24px;")
        self.vL_w_Ticket = QVBoxLayout(self.w_Ticket)
        #self.vL_w_Ticket.setSizeConstraint(QLayout.SetMinimumSize)
        #self.vL_w_Ticket.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vL_w_Ticket.setContentsMargins(3, 3, 3, 1)
        self.vL_w_Ticket.setSpacing(0)
        # ////////////////////////////////// WIDGET BARRA BASE CON HORIZONTAL LAYOUT CONTENIENDO COLOR Y LABEL DE TITULO ////////////////////////
        self.w_Barra = QWidget(self.w_Ticket)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_Barra.sizePolicy().hasHeightForWidth())
        self.w_Barra.setSizePolicy(sizePolicy)
        self.w_Barra.setMinimumSize(QSize(150, 75))
        self.w_Barra.setMaximumSize(QSize(498, 75))
        if tipoSel == 0:
            self.w_Barra.setStyleSheet("background-color: rgb(195, 156, 0);\n"
                                       "background-image:url('images/guion.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 1:
            self.w_Barra.setStyleSheet("background-color: rgb(122, 69, 34);\n"
                                        "background-image:url('images/story.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 2:
            self.w_Barra.setStyleSheet("background-color: rgb(44, 133, 146);\n"
                                       "background-image:url('images/boct.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 3:
            self.w_Barra.setStyleSheet("background-color: rgb(172, 10, 10);\n"
                                       "background-image:url('images/dis2D.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 4:
            self.w_Barra.setStyleSheet("background-color: rgb(159, 0, 74);\n"
                                        "background-image:url('images/ani2D.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 5:
            self.w_Barra.setStyleSheet("background-color: rgb(30, 100, 30);\n"
                                       "background-image:url('images/dis3D.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 6:
            self.w_Barra.setStyleSheet("background-color: rgb(26, 104, 91);\n"
                                       "background-image:url('images/ani3D.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 7:
            self.w_Barra.setStyleSheet("background-color: rgb(107, 114, 16);\n"
                                       "background-image:url('images/ren3D.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 8:
            self.w_Barra.setStyleSheet("background-color: rgb(218, 88, 0);\n"
                                       "background-image:url('images/ediV.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 9:
            self.w_Barra.setStyleSheet("background-color: rgb(7, 50, 135);\n"
                                       "background-image:url('images/audio.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 10:
            self.w_Barra.setStyleSheet("background-color: rgb(90, 0, 91);\n"
                                        "background-image:url('images/renV.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        elif tipoSel == 11:
            self.w_Barra.setStyleSheet("background-color: rgb(84, 84, 84);\n"
                                       "background-image:url('images/otros.png')\n;"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")
        else:
            self.w_Barra.setStyleSheet("background-color: rgb(150, 150, 150);\n"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: right bottom;")

        self.hL_w_Barra = QHBoxLayout(self.w_Barra)
        # ---- Si no agrego un valor al objeto contenido, este duplica el valor original de la propiedad (ej: Margen 3 >> Margen 6)
        self.hL_w_Barra.setContentsMargins(6, 0, 0, 0)
        self.vL_w_Ticket.addWidget(self.w_Barra)
        # ------------------------------------------------------------------------------------------------- WIDGET COLOR -----------------
        self.w_Color = QWidget(self.w_Barra)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_Color.sizePolicy().hasHeightForWidth())
        self.w_Color.setSizePolicy(sizePolicy)
        self.w_Color.setMinimumSize(QSize(32, 60))
        self.w_Color.setStyleSheet("background-color: rgba(255, 255, 255, 50);\n"
                                   "border-radius:15px;\n"
                                   "background-image:url('');")
        self.hL_w_Barra.addWidget(self.w_Color)
        # ------------------------------------------------------------------------------------------------- LABEL TITULO -----------------
        self.l_Titulo = QLabel(self.w_Barra)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l_Titulo.setFont(font)
        #self.l_Titulo.setText("Personaje Tommy un solo renglón y tal vez quede también en dos renglones")
        self.l_Titulo.setText(titulo)
        self.l_Titulo.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "background-image:url('');")
        self.l_Titulo.setWordWrap(True)
        self.hL_w_Barra.addWidget(self.l_Titulo)
        # ///////////////////////////////////// WIDGET CONTENIDO CON HORIZONTAL LAYOUT CONTENIENDO W TRABAJO y W BOTONES ////////////////////////
        self.w_Contenido = QWidget(self.w_Ticket)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_Contenido.sizePolicy().hasHeightForWidth())
        self.w_Contenido.setSizePolicy(sizePolicy)
        self.w_Contenido.setMinimumSize(QSize(0, 0))
        self.w_Contenido.setStyleSheet("background-color: rgba(205, 0, 255, 0);\n"
                                       "border-radius:0px;")
        self.hL_w_Contenido = QHBoxLayout(self.w_Contenido)
        self.hL_w_Contenido.setContentsMargins(0, 0, 0, 0)
        self.hL_w_Contenido.setSpacing(6)
        self.vL_w_Ticket.addWidget(self.w_Contenido)
        # ///////////////////////////// WIDGET CONTENIDO CON VERTICAL LAYOUT CONTENIENDO LABEL DESCRIPCION Y CHECK BOXES /////////////////////////
        self.w_Trabajo = QWidget(self.w_Contenido)
        self.w_Trabajo.setStyleSheet("background-color:rgba(0, 255, 0, 0);")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.w_Trabajo.sizePolicy().hasHeightForWidth())
        self.w_Trabajo.setSizePolicy(sizePolicy)
        self.w_Trabajo.setMinimumSize(QSize(0, 0))
        self.vL_w_Trabajo = QVBoxLayout(self.w_Trabajo)
        self.vL_w_Trabajo.setContentsMargins(15, 12, 0, 0)
        self.vL_w_Trabajo.setSpacing(3)
        self.hL_w_Contenido.addWidget(self.w_Trabajo)
        # --------------------------------------------------------------------------------------------- LABEL DESRIPCION -----------------
        self.l_Descripcion = QLabel(self.w_Trabajo)
        self.l_Descripcion.setStyleSheet("background-color:rgba(255, 215, 0, 0);")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.l_Descripcion.sizePolicy().hasHeightForWidth())
        self.l_Descripcion.setSizePolicy(sizePolicy)
        self.l_Descripcion.setMinimumSize(QSize(0, 15))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.l_Descripcion.setFont(font)
        self.l_Descripcion.setText(descripcion)
        self.l_Descripcion.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.l_Descripcion.setWordWrap(True)
        self.vL_w_Trabajo.addWidget(self.l_Descripcion)
        # ------------------------------------------------------------------------- ESPACIADO ENTRE DESRIPCION Y TICKETS -----------------
        self.spacerItemSepa = QSpacerItem(10, 5, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.vL_w_Trabajo.addItem(self.spacerItemSepa)

        # ///////////////////////////////////// WIDGET BOTONERA CON VERTICAL LAYOUT QUE CONTIENE PB EDITAR Y PB ELIMINAR /////////////////
        self.w_Botones = QWidget(self.w_Contenido)
        self.w_Botones.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_Botones.sizePolicy().hasHeightForWidth())
        self.w_Botones.setSizePolicy(sizePolicy)
        self.w_Botones.setMinimumSize(QSize(70, 130))
        #self.w_Botones.setMinimumWidth(498)
        self.vL_w_Botones = QVBoxLayout(self.w_Botones)
        self.vL_w_Botones.setSpacing(5)
        self.hL_w_Contenido.addWidget(self.w_Botones)
        # ------------------------------------------------------------------------------------------------- BOTON EDITAR -----------------
        self.btn_edit = QPushButton("", self.w_Botones)
        self.btn_edit.setStyleSheet("QPushButton{\n"
                                   "background-image:url('images/edit_ticket.png');\n"
                                   "background-color:rgba(0, 0, 0, 0);\n"
                                   "border-radius:none;\n"
                                   "width:70px;\n"
                                   "height:70px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:Hover{\n"
                                   "background-image:url('images/edit_ticket_over.png');\n"
                                   "color:black;\n"
                                   "}\n"
                                   "QPushButton:Pressed{\n"
                                   "background-image:url('images/edit_ticket.png');\n"
                                   "color:white;\n"
                                   "}")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setMinimumSize(QSize(70, 70))
        self.vL_w_Botones.addWidget(self.btn_edit)
        self.btn_edit.clicked.connect(click_btn_edit)
        # ----------------------------------------------------------------------------------------------- BOTON ELIMINAR -----------------
        self.btn_del = QPushButton("", self.w_Botones)
        self.btn_del.setStyleSheet("QPushButton{\n"
                                    "background-image:url('images/del_ticket.png');\n"
                                    "background-color:rgba(0, 0, 0, 0);\n"
                                    "border-radius:none;\n"
                                    "width:52px;\n"
                                    "height:52px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{\n"
                                    "background-image:url('images/del_ticket_over.png');\n"
                                    "color:black;\n"
                                    "}\n"
                                    "QPushButton:Pressed{\n"
                                    "background-image:url('images/del_ticket.png');\n"
                                    "color:white;\n"
                                    "}")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMinimumSize(QSize(52, 52))
        self.vL_w_Botones.addWidget(self.btn_del, 0, Qt.AlignCenter)
        self.btn_del.clicked.connect(click_btn_del)

        # -------------------------------------------------------------------------- EL LAYOUT DEL MAIN AGREGA EL TICKET -----------------
        layoutContainer.addWidget(self.w_Ticket, posFila, posCol, 1, 1, Qt.AlignTop)


    def BotonTicketNuevo(self, accion, posFila, posCol, scrollContainer, layoutContainer):
        self.btn_tck_add = QPushButton(scrollContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tck_add.sizePolicy().hasHeightForWidth())
        self.btn_tck_add.setSizePolicy(sizePolicy)
        self.btn_tck_add.setMinimumSize(QSize(504, 230))
        self.btn_tck_add.setStyleSheet("QPushButton{\n"
                                       "background-image:url('images/add_ticket.png');\n"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: center;\n"
                                       "background-color: rgba(204, 204, 204, 18);\n"
                                       "color:rgb(255, 255, 255);\n"
                                       "border-radius:24px;\n"
                                       "}\n"
                                       "\n"
                                        "QPushButton:Hover{\n"
                                       "background-image:url('images/add_ticket_over.png');\n"
                                       "background-color:rgba(224, 224, 224, 48);\n"
                                       "}\n"
                                       "QPushButton:Pressed{\n"
                                       "background-color:rgba(125, 200, 25, 48);\n"
                                       "}")
        self.btn_tck_add.clicked.connect(accion)
        layoutContainer.addWidget(self.btn_tck_add, posFila, posCol, 1, 1, Qt.AlignTop)

    def CreaItem(self, texto, estado, chck_click, color):
        self.cBox = QCheckBox(self.w_Trabajo)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.cBox.setFont(font)
        self.cBox.setText(texto)
        self.cBox.setChecked(estado)
        self.cBox.setObjectName("checkBox")
        self.cBox.setStyleSheet(color)
        self.cBox.stateChanged.connect(chck_click)
        #self.cBox.toggle()
        self.vL_w_Trabajo.addWidget(self.cBox, 0, Qt.AlignTop)


    # ******************************************************************************************************************************************************************
    # **************************************************** ITEMS *******************************************************************************************************

    def Items(self, texto, del_btn, edit_btn, wCont, lCont):
        self.w_unItem = QWidget(wCont)
        #self.w_unItem.setStyleSheet("background-color:rgba(165, 220, 165, 0);")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_unItem.sizePolicy().hasHeightForWidth())
        self.w_unItem.setSizePolicy(sizePolicy)
        self.w_unItem.setMinimumSize(QSize(0, 25))
        self.hL_w_unItem = QHBoxLayout(self.w_unItem)
        self.hL_w_unItem.setContentsMargins(0, 0, 0, 0)
        self.hL_w_unItem.setSpacing(10)
        self.ltxt = QLabel(self.w_unItem)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ltxt.setFont(font)
        self.ltxt.setText(str(texto))
        self.editB = QPushButton("Editar", self.w_unItem)
        self.editB.setMaximumSize(80, 25)
        #self.editB.setStyleSheet("color:white; background-color:green; font-family:'Calibri'; font-weight:normal; font-style:italic; font-size:11pt;")
        #self.editB.setStyleSheet("color:green; font-family:'Calibri'; font-weight:normal; font-style:italic; font-size:11pt;")
        self.editB.setStyleSheet("QPushButton{\n"
                                 "color:rgb(0, 135, 0);\n"
                                 "background-color: rgb(224, 224, 224);\n"
                                 "border-color:rgb(151, 206, 151);\n"
                                 "border-width:1px;\n"
                                 "border-radius:none;\n"
                                 "border-style: solid;\n"
                                 "width:80px;\n"
                                 "height:25px;\n"
                                 "font-family:'Calibri';\n"
                                 "font-weight:normal;\n"
                                 "font-style:italic;\n"
                                 "font-size:11pt;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "background-color: rgb(223, 255, 223);\n"
                                 "border-color:rgb(0, 185, 0);\n"
                                 "}")
        #self.editB.clicked.connect(accionEdit)
        self.delB = QPushButton("X", self.w_unItem)
        self.delB.setMaximumSize(30, 25)
        self.delB.setMinimumSize(30, 25)
        #self.delB.setStyleSheet("color:white; background-color:red; font-family:'Calibri'; font-weight:bold; font-size:11pt;")
        self.delB.setStyleSheet("QPushButton{\n"
                                "color:rgb(212, 0, 0);"
                                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);\n"
                                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #CCCCCC, stop: 1 #AAAAAA);\n"
                                "background-color: rgb(225, 214, 214);\n"
                                "border-color:rgb(206, 151, 151);\n"
                                "border-width:1px;\n"
                                "border-radius:none;\n"
                                "border-style: solid;\n"
                                "width:30px;\n"
                                "height:25px;\n"
                                "font-family:'Calibri';\n"
                                "font-weight:bold;\n"
                                "font-size:11pt;\n"
                                "}\n"
                                "\n"
                                "QPushButton:Hover{\n"
                                "background-color: rgb(255, 153, 153);\n"
                                "border-color:rgb(185, 0, 0);\n"
                                "}")

        self.hL_w_unItem.addWidget(self.ltxt)
        self.hL_w_unItem.addWidget(self.editB)
        self.hL_w_unItem.addWidget(self.delB)
        self.delB.clicked.connect(del_btn)
        self.editB.clicked.connect(edit_btn)
        lCont.setSpacing(6)
        lCont.addWidget(self.w_unItem)

    # ******************************************************************************************************************
    # ************************************************* POPUP DIALOG ***************************************************

    def DialogProyecto(self):
        self.dialogP = QDialog()
        self.dialogP.resize(600, 480)
        self.dialogP.setWindowTitle("Dialogo...")

        self.vL_dialoP = QVBoxLayout(self.dialogP)
        self.vL_dialoP.setContentsMargins(30, 30, 30, 30)
        self.vL_dialoP.setSpacing(0)

        self.w_DTitulo = QWidget(self.dialogP)
        self.w_DTitulo.setStyleSheet("background-color:rgba(255, 0, 255, 250);")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.w_DTitulo.sizePolicy().hasHeightForWidth())
        self.w_DTitulo.setSizePolicy(sizePolicy)
        self.w_DTitulo.setMinimumSize(QSize(0, 30))
        #self.w_DTitulo.move(0, 0)
        #self.w_DTitulo.resize(320, 240)
        self.hL_w_DTitulo = QHBoxLayout(self.w_DTitulo)
        self.hL_w_DTitulo.setContentsMargins(10, 10, 10, 10)
        self.hL_w_DTitulo.setSpacing(5)

        self.vL_dialoP.addWidget(self.w_DTitulo)

        self.l_DTitulo = QLabel(self.w_DTitulo)
        #self.l_DTitulo.setStyleSheet("background-color:rgba(255, 215, 0, 250);")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.l_DTitulo.sizePolicy().hasHeightForWidth())
        self.l_DTitulo.setSizePolicy(sizePolicy)
        self.l_DTitulo.setMinimumSize(QSize(70, 30))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(50)
        self.l_DTitulo.setFont(font)
        self.l_DTitulo.setText("Titulo")
        #self.l_DTitulo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignCenter)
        #self.l_DTitulo.setWordWrap(True)
        self.hL_w_DTitulo.addWidget(self.l_DTitulo)

        #self.iB_Titulo = QPlainTextEdit(self.w_DTitulo)
        self.iB_Titulo = QLineEdit(self.w_DTitulo)
        #self.iB_Titulo.setStyleSheet("background-color:rgba(5, 215, 255, 250);")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.iB_Titulo.sizePolicy().hasHeightForWidth())
        self.iB_Titulo.setSizePolicy(sizePolicy)
        self.iB_Titulo.setMinimumSize(QSize(0, 30))
        self.hL_w_DTitulo.addWidget(self.iB_Titulo)

        self.buttonBox = QDialogButtonBox(self.dialogP)
        self.buttonBox.setGeometry(QRect(0, 0, 581, 41))
        #self.buttonBox.setStyleSheet("background-color:rgba(55, 215, 125, 0);")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QSize(0, 50))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vL_dialoP.addWidget(self.buttonBox, 0, Qt.AlignBottom)

        self.buttonBox.accepted.connect(self.dialogP.accept)
        self.buttonBox.rejected.connect(self.dialogP.reject)
        QMetaObject.connectSlotsByName(self.dialogP)

        self.dialogP.show()
        self.dialogP.exec_()

    # ******************************************************************************************************************
    # ************************************************** SCROLL BARS ***************************************************

    def ScrollVStyle(self, scrollV):
        scrollV.setStyleSheet("QScrollBar:vertical {\n"
                               "border: 0px solid #999999;\n"
                               "border-radius:6px;\n"
                               "background:rgb(15, 15, 15);\n"
                               "width:20px;\n"
                               "padding:5px;\n"
                               "}\n"
                               "QScrollBar::handle:vertical {\n"
                               "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
                               "background: rgb(35, 35, 35);\n"
                               "background: rgb(82, 131, 16);\n"
                               "min-height: 0px;\n"
                               "border-radius:5px;\n"
                               "}\n"
                               "QScrollBar::sub-page:vertical {\n"
                               "background: rgb(15, 15, 15);\n"
                               "border-radius:4px;\n"
                               "width:8px;\n"
                               "}\n"
                               "QScrollBar::add-page:vertical {\n"
                               "background: rgb(15, 15, 15);\n"
                               "border-radius:0px;\n"
                               "}\n"
                               "QScrollBar::add-line:vertical {\n"
                               "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                               "height: 0px;\n"
                               "background: green;\n"
                               "subcontrol-position: bottom;\n"
                               "subcontrol-origin: margin;\n"
                               "}\n"
                               "QScrollBar::sub-line:vertical {\n"
                               "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                               "height: 0 px;\n"
                               "background: green;\n"
                               "subcontrol-position: top;\n"
                               "subcontrol-origin: margin;\n"
                               "}\n"
                               "QScrollBar::up-arrow:vertical {\n"
                               "image:url('./icons/up_48.png');\n"
                               "height: 15px;\n"
                               "width: 15px;\n"
                               "}\n"
                               "QScrollBar::down-arrow:vertical {\n"
                               "image:url('./icons/down_48.png');\n"
                               "height: 15px;\n"
                               "width: 15px;\n"
                               "}")

    def ScrollTickets(self, scrollT):
        scrollT.setStyleSheet("QScrollBar:horizontal {\n"
                              "border: 0px solid #999999;\n"
                              "border-radius:6px;\n"
                              "background:rgb(15, 15, 15);\n"
                              "height:20px;\n"
                              "padding:5px;\n"
                              "}\n"
                              "QScrollBar::handle:horizontal {\n"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
                              "background: rgb(35, 35, 35);\n"
                              "background: rgb(82, 131, 16);\n"
                              "min-height: 0px;\n"
                              "border-radius:5px;\n"
                              "}\n"
                              "QScrollBar::sub-page:horizontal {\n"
                              "background: rgb(15, 15, 15);\n"
                              "border-radius:4px;\n"
                              "height:8px;\n"
                              "}\n"
                              "QScrollBar::add-page:horizontal {\n"
                              "background: rgb(15, 15, 15);\n"
                              "border-radius:0px;\n"
                              "}\n"
                              "QScrollBar::add-line:horizontal {\n"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                              "height: 0px;\n"
                              "background: green;\n"
                              "subcontrol-position: bottom;\n"
                              "subcontrol-origin: margin;\n"
                              "}\n"
                              "QScrollBar::sub-line:horizontal {\n"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                              "height: 0 px;\n"
                              "background: green;\n"
                              "subcontrol-position: top;\n"
                              "subcontrol-origin: margin;\n"
                              "}\n"
                              "QScrollBar::up-arrow:horizontal {\n"
                              "image:url('./icons/up_48.png');\n"
                              "height: 15px;\n"
                              "width: 15px;\n"
                              "}\n"
                              "QScrollBar::down-arrow:horizontal {\n"
                              "image:url('./icons/down_48.png');\n"
                              "height: 15px;\n"
                              "width: 15px;\n"
                              "}\n"
                              "QScrollBar:vertical {\n"
                              "border: 0px solid #999999;\n"
                              "border-radius:6px;\n"
                              "background:rgb(15, 15, 15);\n"
                              "width:20px;\n"
                              "padding:5px;\n"
                              "}\n"
                              "QScrollBar::handle:vertical {\n"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
                              "background: rgb(35, 35, 35);\n"
                              "background: rgb(82, 131, 16);\n"
                              "min-height: 0px;\n"
                              "border-radius:5px;\n"
                              "}\n"
                              "QScrollBar::sub-page:vertical {\n"
                              "background: rgb(15, 15, 15);\n"
                              "border-radius:4px;\n"
                              "width:8px;\n"
                              "}\n"
                              "QScrollBar::add-page:vertical {\n"
                              "background: rgb(15, 15, 15);\n"
                              "border-radius:0px;\n"
                              "}\n"
                              "QScrollBar::add-line:vertical {\n"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                              "height: 0px;\n"
                              "background: green;\n"
                              "subcontrol-position: bottom;\n"
                              "subcontrol-origin: margin;\n"
                              "}\n"
                              "QScrollBar::sub-line:vertical {\n"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
                              "height: 0 px;\n"
                              "background: green;\n"
                              "subcontrol-position: top;\n"
                              "subcontrol-origin: margin;\n"
                              "}\n"
                              "QScrollBar::up-arrow:vertical {\n"
                              "image:url('./icons/up_48.png');\n"
                              "height: 15px;\n"
                              "width: 15px;\n"
                              "}\n"
                              "QScrollBar::down-arrow:vertical {\n"
                              "image:url('./icons/down_48.png');\n"
                              "height: 15px;\n"
                              "width: 15px;\n"
                              "}")

    # ******************************************************************************************************************
    # ******************************************** BOTONERA ENCABEZADO Y HORA ******************************************

    def Menues(self, labelStyle, dateStyle, lineStyle):
        labelStyle.setStyleSheet("background-color: rgba(125, 200, 25, 255);\n"
                                 "color:rgba(0, 0, 0, 255);")

        dateStyle.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
                                "background-color: rgba(82, 131, 16, 255);")

        lineStyle.setStyleSheet("color: rgba(255, 255, 255, 55);")