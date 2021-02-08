from PyQt5 import QtCore
from PyQt5.Qt import *

import gui_Spacers
spacers = gui_Spacers.Ui_Spacers()
import fileManager
fileManager = fileManager.FileManager()

class Ui_Splash(object):
    def Splash(self, d_Splash, pixmap, clicked_pb_close, estilo):
        d_Splash.resize(760, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(d_Splash.sizePolicy().hasHeightForWidth())
        d_Splash.setSizePolicy(sizePolicy)
        d_Splash.setMinimumSize(QtCore.QSize(760, 300))
        d_Splash.setMaximumSize(QtCore.QSize(760, 300))
        d_Splash.setStyleSheet(estilo['d_Splash'])
        d_Splash.setModal(True)
        self.l_img = QLabel(d_Splash)
        self.l_img.setGeometry(QtCore.QRect(0, 0, 760, 300))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_img.sizePolicy().hasHeightForWidth())
        self.l_img.setSizePolicy(sizePolicy)
        self.l_img.setMinimumSize(QtCore.QSize(760, 300))
        self.l_img.setMaximumSize(QtCore.QSize(760, 300))
        self.l_img.setStyleSheet(estilo['l_img'])
        self.l_img.setText("")
        self.l_img.setPixmap(pixmap)
        self.pb_close = QPushButton(d_Splash)
        self.pb_close.setGeometry(QtCore.QRect(0, 0, 760, 300))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_close.sizePolicy().hasHeightForWidth())
        self.pb_close.setSizePolicy(sizePolicy)
        self.pb_close.setMinimumSize(QtCore.QSize(760, 300))
        self.pb_close.setMaximumSize(QtCore.QSize(760, 300))
        self.pb_close.setStyleSheet(estilo['pb_close'])
        self.pb_close.setText("")
        self.pb_close.clicked.connect(clicked_pb_close)