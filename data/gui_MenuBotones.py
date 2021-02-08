from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class Ui_MenuBotones(object):
    def menuBotones(self, wCont, lCont, click_pb_New, click_pb_Open, click_pb_Save, click_pb_SaveAs, estilo):
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.pb_menuNew = QPushButton("", wCont)
        self.pb_menuNew.setSizePolicy(sizePolicy)
        self.pb_menuNew.setStyleSheet(estilo['pb_menuNew'])
        self.pb_menuNew.clicked.connect(click_pb_New)
        lCont.addWidget(self.pb_menuNew)

        self.pb_menuOpen = QPushButton("", wCont)
        self.pb_menuOpen.setSizePolicy(sizePolicy)
        self.pb_menuOpen.setStyleSheet(estilo['pb_menuOpen'])
        self.pb_menuOpen.clicked.connect(click_pb_Open)
        lCont.addWidget(self.pb_menuOpen)

        self.pb_menuSave = QPushButton("", wCont)
        self.pb_menuSave.setSizePolicy(sizePolicy)
        self.pb_menuSave.setStyleSheet(estilo['pb_menuSave'])
        self.pb_menuSave.clicked.connect(click_pb_Save)
        lCont.addWidget(self.pb_menuSave)

        self.pb_menuSaveAs = QPushButton("", wCont)
        self.pb_menuSaveAs.setSizePolicy(sizePolicy)
        self.pb_menuSaveAs.setStyleSheet(estilo['pb_menuSaveAs'])
        self.pb_menuSaveAs.clicked.connect(click_pb_SaveAs)
        lCont.addWidget(self.pb_menuSaveAs)
