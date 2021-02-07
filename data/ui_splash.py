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
        d_Splash.resize(760, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(d_Splash.sizePolicy().hasHeightForWidth())
        d_Splash.setSizePolicy(sizePolicy)
        d_Splash.setMinimumSize(QtCore.QSize(760, 507))
        d_Splash.setMaximumSize(QtCore.QSize(760, 507))
        d_Splash.setStyleSheet("background-color: rgb(125, 200, 25);")
        d_Splash.setModal(True)
        self.l_img = QtWidgets.QLabel(d_Splash)
        self.l_img.setGeometry(QtCore.QRect(5, 5, 750, 497))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_img.sizePolicy().hasHeightForWidth())
        self.l_img.setSizePolicy(sizePolicy)
        self.l_img.setMinimumSize(QtCore.QSize(750, 497))
        self.l_img.setMaximumSize(QtCore.QSize(750, 497))
        self.l_img.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.l_img.setText("")
        self.l_img.setObjectName("l_img")
        self.w_texto = QtWidgets.QWidget(d_Splash)
        self.w_texto.setGeometry(QtCore.QRect(15, 391, 730, 101))
        self.w_texto.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.w_texto.setObjectName("w_texto")
        self.l_txt = QtWidgets.QLabel(self.w_texto)
        self.l_txt.setGeometry(QtCore.QRect(9, 9, 712, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_txt.sizePolicy().hasHeightForWidth())
        self.l_txt.setSizePolicy(sizePolicy)
        self.l_txt.setMinimumSize(QtCore.QSize(712, 83))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setItalic(True)
        self.l_txt.setFont(font)
        self.l_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.l_txt.setWordWrap(True)
        self.l_txt.setObjectName("l_txt")
        self.pb_close = QtWidgets.QPushButton(d_Splash)
        self.pb_close.setGeometry(QtCore.QRect(0, 0, 760, 507))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_close.sizePolicy().hasHeightForWidth())
        self.pb_close.setSizePolicy(sizePolicy)
        self.pb_close.setMinimumSize(QtCore.QSize(760, 507))
        self.pb_close.setMaximumSize(QtCore.QSize(760, 507))
        self.pb_close.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")

        self.retranslateUi(d_Splash)
        QtCore.QMetaObject.connectSlotsByName(d_Splash)

    def retranslateUi(self, d_Splash):
        _translate = QtCore.QCoreApplication.translate
        d_Splash.setWindowTitle(_translate("d_Splash", "Dialog"))
        self.l_txt.setText(_translate("d_Splash", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))

