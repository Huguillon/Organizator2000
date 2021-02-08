# from PyQt5.Qt import *
from PyQt5.Qt import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMenuBar, QMetaObject, QSizePolicy, QSize, QScrollArea, QAbstractScrollArea, QLabel, QFrame, QRect, QAction, Qt

# import gui_Spacers
# spacers = gui_Spacers.Ui_Spacers()
# import fileManager
# fileManager = fileManager.FileManager()
# Combobox
# listaItems = ["Guión / Ideas", "Storyboard", "Boceto", "Diseño 2D", "Animación 2D", "Diseño 3D", "Animación 3D", "Render 3D", "Edición Video", "Audio", "Render Video", "Otros", ""]
# pieles = ["Cristal 01", "Cristal 02", "Papel", "Color 01", "Color 02"]

class Ui_MainWindow(object):
    def mainWindow(self, MainWindow, estilo):
        # ---- Inicia el MainWindow ----
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1310, 819)
        # ---- Inicia el centralWidget que va a contener todos los objetos de la pantalla ----
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet(estilo['centralwidget'])
        # ---- Layout Horizontal del centralWidget ----
        self.hL_centralwidget = QHBoxLayout(self.centralwidget)
        self.hL_centralwidget.setContentsMargins(0, 0, 0, 0)
        self.hL_centralwidget.setSpacing(20)

        # ------------------------------------------------- BOTONERA -------------------------------------------------
        # ---- V-Layout Botonera ----
        self.vL_Botonera = QVBoxLayout()
        self.vL_Botonera.setSpacing(0)
        # ---- Widget Botones "Menu" ----
        self.w_Menu = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_Menu.sizePolicy().hasHeightForWidth())
        self.w_Menu.setSizePolicy(sizePolicy)
        self.w_Menu.setMinimumSize(QSize(0, 71))
        self.w_Menu.setStyleSheet(estilo['w_Menu'])
        # ---- H-Layout Botones "Menu" ----
        self.hL_Menu = QHBoxLayout(self.w_Menu)
        self.hL_Menu.setContentsMargins(0, 0, 0, 0)
        self.hL_Menu.setSpacing(0)
        # ---- Agrega el widget "Menu" en el V-Layout "Botonera" ----
        self.vL_Botonera.addWidget(self.w_Menu)

        # ---- Inicia el Widget "Reloj" ----
        self.w_Reloj = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_Reloj.sizePolicy().hasHeightForWidth())
        self.w_Reloj.setSizePolicy(sizePolicy)
        self.w_Reloj.setMinimumSize(QSize(0, 40))
        self.w_Reloj.setStyleSheet(estilo['w_Reloj'])
        # ---- H-Layout "Reloj" ----
        self.hL_Reloj = QHBoxLayout(self.w_Reloj)
        self.hL_Reloj.setContentsMargins(8, 8, 8, 8)
        self.hL_Reloj.setSpacing(0)
        # ---- Agrega el Widget "Reloj" en el V-Layout "Botonera" ----
        self.vL_Botonera.addWidget(self.w_Reloj)

        # ---- Inicia ScrollArea Botones de proyectos ----
        self.sA_Botonera = QScrollArea(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sA_Botonera.sizePolicy().hasHeightForWidth())
        self.sA_Botonera.setSizePolicy(sizePolicy)
        self.sA_Botonera.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sA_Botonera.setMinimumSize(QSize(315, 0))
        self.sA_Botonera.setFrameShape(QFrame.NoFrame)
        self.sA_Botonera.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sA_Botonera.setWidgetResizable(True)
        self.sA_Botonera.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sA_Botonera.setStyleSheet(estilo['sA_Botonera'])

        # ---- Widget Contenedor de los Botones Proyectos ----
        self.sAWC_Botonera = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sAWC_Botonera.sizePolicy().hasHeightForWidth())
        self.sAWC_Botonera.setSizePolicy(sizePolicy)
        self.sAWC_Botonera.setMinimumSize(QSize(0, 0))
        self.sAWC_Botonera.setStyleSheet(estilo['sAWC_Botonera'])
        # ---- V-Layout Contenedor de los Botones Proyectos ----
        self.vL_sAWC_Botonera = QVBoxLayout(self.sAWC_Botonera)
        self.vL_sAWC_Botonera.setContentsMargins(0, 0, 0, 0)
        self.vL_sAWC_Botonera.setSpacing(0)

        # ---- Setea el Widget "sAWC_Botonera" dentro del ScrollArea "sA_Botonera"
        # (en el scroll se pone asi, sino no funciona) ----
        self.sA_Botonera.setWidget(self.sAWC_Botonera)
        # ---- Agrega el widget "sA_Botonera" en el V-Layout "vL_Botonera" ----
        self.vL_Botonera.addWidget(self.sA_Botonera)

        self.hL_centralwidget.addLayout(self.vL_Botonera)
        # ------------------------------------------------- FIN BOTONERA -----------------------------------------------


        # ------------------------------------------------- TICKETS ----------------------------------------------------
        # ---- V-Layout Tickets ----
        self.vL_Tickets = QVBoxLayout()
        self.vL_Tickets.setContentsMargins(0, 5, 20, 20)
        self.vL_Tickets.setSpacing(10)
        # ---- Widget conteniendo el area del "Titulo" (contiene titulo del proyecto) ----
        self.w_ticketsTitulo = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_ticketsTitulo.sizePolicy().hasHeightForWidth())
        self.w_ticketsTitulo.setSizePolicy(sizePolicy)
        self.w_ticketsTitulo.setGeometry(QRect(0, 0, 50, 50))
        self.w_ticketsTitulo.setMinimumSize(QSize(0, 50))
        self.w_ticketsTitulo.setStyleSheet(estilo['w_ticketsTitulo'])
        # ---- H-Layout el area del "Titulo" ----
        self.hL_w_ticketsTitulo = QHBoxLayout(self.w_ticketsTitulo)
        self.hL_w_ticketsTitulo.setContentsMargins(0, 0, 20, 0)
        self.hL_w_ticketsTitulo.setSpacing(10)

        # ---- Inicia Label del "Titulo" ----
        self.l_ticketsTitulo = QLabel("", self.w_ticketsTitulo)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_ticketsTitulo.sizePolicy().hasHeightForWidth())
        self.l_ticketsTitulo.setSizePolicy(sizePolicy)
        self.l_ticketsTitulo.setStyleSheet(estilo['l_ticketsTitulo'])
        # ---- Agrega el label "Titulo" en el H-Layout "Titulo" ----
        self.hL_w_ticketsTitulo.addWidget(self.l_ticketsTitulo)

        self.vL_Tickets.addWidget(self.w_ticketsTitulo)

        self.line_Tickets = QFrame(self.centralwidget)
        self.line_Tickets.setFrameShadow(QFrame.Plain)
        self.line_Tickets.setLineWidth(3)
        self.line_Tickets.setFrameShape(QFrame.HLine)
        self.line_Tickets.setStyleSheet(estilo['line_Tickets'])
        self.vL_Tickets.addWidget(self.line_Tickets)

        self.l_ticketsDescripcion = QLabel("", self.centralwidget)
        self.l_ticketsDescripcion.setWordWrap(True)
        self.l_ticketsDescripcion.setStyleSheet(estilo['l_ticketsDescripcion'])
        self.vL_Tickets.addWidget(self.l_ticketsDescripcion)

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------------------- LA SOLUCION ESTA POR ACA -------------------------------------------

        self.sArea_Tickets = QScrollArea(self.centralwidget)
        self.sArea_Tickets.setStyleSheet(estilo['sArea_Tickets'])
        self.sArea_Tickets.setFrameShape(QFrame.NoFrame)
        self.sArea_Tickets.setWidgetResizable(True)

        self.w_Tickets = QWidget()
        self.w_Tickets.setStyleSheet(estilo['w_Tickets'])
        self.vL_w_Tickets = QGridLayout(self.w_Tickets)
        self.vL_w_Tickets.setContentsMargins(0, 0, 0, 0)
        self.vL_w_Tickets.setSpacing(0)

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.sAWC_Tickets = QWidget(self.w_Tickets)
        self.sAWC_Tickets.setStyleSheet(estilo['sAWC_Tickets'])

        self.vL_sAWC_Tickets = QGridLayout(self.sAWC_Tickets)
        self.vL_sAWC_Tickets.setContentsMargins(20, 20, 20, 20)
        self.vL_sAWC_Tickets.setSpacing(6)


        self.vL_w_Tickets.addWidget(self.sAWC_Tickets)
        # self.sArea_Tickets.setWidget(self.sAWC_Tickets)
        self.sArea_Tickets.setWidget(self.w_Tickets)

        self.vL_Tickets.addWidget(self.sArea_Tickets)
        self.hL_centralwidget.addLayout(self.vL_Tickets)
        # ------------------------------------------------- FIN TICKETS ------------------------------------------------

        MainWindow.setCentralWidget(self.centralwidget)


        # ------------------------------------------------- MENU BAR ---------------------------------------------------
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setGeometry(QRect(0, 0, 1310, 30))
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.setStyleSheet(estilo['menuBar'])

        QMetaObject.connectSlotsByName(MainWindow)

    def menuBarFull(self, quit_trigger, respFile, respTicket):
        self.bar = self.menuBar
        self.file = self.bar.addMenu('Archivo')
        # self.tickets = self.bar.addMenu('Tickets')
        self.presets = self.bar.addMenu('Preseteos')
        self.skins = self.bar.addMenu('Pieles')

        # ---- Agrega los items a FILE / ARCHIVO
        new_action = QAction('Nuevo', self)
        new_action.setShortcut('Ctrl+N')
        # new_action.setCheckable(True)
        # new_action.setChecked(True)
        open_action = QAction('Abrir', self)
        open_action.setShortcut('Ctrl+O')
        save_action = QAction('Guardar', self)
        save_action.setShortcut('Ctrl+S')
        save_as_action = QAction('Guardar como...', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        quit_action = QAction('Salir', self)
        quit_action.setShortcut('Ctrl+Q')
        self.file.addAction(new_action)
        self.file.addAction(open_action)
        self.file.addAction(save_action)
        self.file.addAction(save_as_action)

        # ---- Agrega el menu "Recientes" ----
        self.recents = self.file.addMenu('Recientes')
        self.file.addSeparator()
        # print(fileManager.dataInicial['Recientes'])

        # ---- Agrega la accion "Salir" ----
        self.file.addAction(quit_action)

        # ---- Click de los items de FILE / ARCHIVO ----
        quit_action.triggered.connect(quit_trigger)
        self.file.triggered.connect(respFile)

        # ---- Agrega los sub menus en el menu "Preseteos" ----
        self.projects = self.presets.addMenu('Proyectos')
        self.works = self.presets.addMenu('Trabajos')
        self.tickets = self.presets.addMenu('Tickets')
        # ---- Crea las acciones del menu "Preseteos" ----
        # ---- Proyectos ----
        seriep_action = QAction('Proyecto Serie', self)
        # ---- Trabajos ----
        baseserie_action = QAction('Base de la Serie', self)
        capitulo_action = QAction('Capitulo', self)
        # ---- Tickets ----
        ideas_action = QAction('Ideas Generales', self)
        ideasbocetos_action = QAction('Ideas de la Serie', self)
        guion_action = QAction('Guión', self)
        story_action = QAction('Storyboard', self)
        modelado_action = QAction('Diseño 3D', self)
        render3d_action = QAction('Render 3D', self)
        edicion_action = QAction('Edición', self)
        audio_action = QAction('Audio', self)
        # ---- Agrega los proyectos al sub menu "Proyectos" ----
        self.projects.addAction(seriep_action)
        # ---- Agrega los trabajos al sub menu "Trabajos" ----
        self.works.addAction(baseserie_action)
        self.works.addAction(capitulo_action)
        # ---- Agrega los tickets al sub menu "Tickets" ----
        self.tickets.addAction(ideas_action)
        self.tickets.addAction(guion_action)
        self.tickets.addAction(story_action)
        self.tickets.addAction(ideasbocetos_action)
        self.tickets.addAction(modelado_action)
        self.tickets.addAction(render3d_action)
        self.tickets.addAction(edicion_action)
        self.tickets.addAction(audio_action)

        self.presets.triggered.connect(respTicket)