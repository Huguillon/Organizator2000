# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba_LabelMouse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 60, 311, 151))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 221, 91))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 71))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setStyleSheet("font: 75 14pt \"Calibri\";")
        self.label.setLineWidth(-1)
        self.label.setMidLineWidth(-1)
        self.label.setText("El Proyecto")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------ESTA ES LA SOLUCION!!!!! ---------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        self.label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        # self.label.raise_()
        # self.pushButton.raise_()
        # self.label.raise_()
        # self.pushButton.raise_()
        # self.pushButton.raise_()
        #self.label.raise_()
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(420, 60, 311, 151))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 40, 221, 91))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 221, 91))
        self.label_2.setStyleSheet("font: 75 14pt \"Calibri\";")
        self.label_2.setLineWidth(0)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_2.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        # self.label_2.raise_()
        # self.pushButton_2.raise_()
        # self.pushButton_2.raise_()
        # self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "El Proyecto"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
