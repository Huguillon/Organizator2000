# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_splash.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_d_Splash(object):
    def setupUi(self, d_Splash):
        d_Splash.setObjectName("d_Splash")
        d_Splash.resize(760, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(d_Splash.sizePolicy().hasHeightForWidth())
        d_Splash.setSizePolicy(sizePolicy)
        d_Splash.setMinimumSize(QtCore.QSize(760, 300))
        d_Splash.setMaximumSize(QtCore.QSize(760, 300))
        d_Splash.setStyleSheet("background-color: rgb(125, 200, 25);")
        d_Splash.setModal(True)
        self.l_img = QtWidgets.QLabel(d_Splash)
        self.l_img.setGeometry(QtCore.QRect(0, 0, 760, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_img.sizePolicy().hasHeightForWidth())
        self.l_img.setSizePolicy(sizePolicy)
        self.l_img.setMinimumSize(QtCore.QSize(760, 300))
        self.l_img.setMaximumSize(QtCore.QSize(760, 300))
        self.l_img.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.l_img.setText("")
        self.l_img.setObjectName("l_img")
        self.pb_close = QtWidgets.QPushButton(d_Splash)
        self.pb_close.setGeometry(QtCore.QRect(0, 0, 760, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_close.sizePolicy().hasHeightForWidth())
        self.pb_close.setSizePolicy(sizePolicy)
        self.pb_close.setMinimumSize(QtCore.QSize(760, 300))
        self.pb_close.setMaximumSize(QtCore.QSize(760, 300))
        self.pb_close.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")

        self.retranslateUi(d_Splash)
        QtCore.QMetaObject.connectSlotsByName(d_Splash)

    def retranslateUi(self, d_Splash):
        _translate = QtCore.QCoreApplication.translate
        d_Splash.setWindowTitle(_translate("d_Splash", "Dialog"))

