# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_botonymenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 180, 201, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.hasFocus()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 230, 171, 71))
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label.blockSignals(True)
        self.label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        MainWindow.setCentralWidget(self.centralwidget)

        print("1920 / 2 =", 1920/2)
        print("-1920 / 2 =", -1920/2)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuRecents = QtWidgets.QMenu(self.menuFile)
        self.menuRecents.setObjectName("menuRecents")

        MainWindow.setMenuBar(self.menubar)

        self.actionPrimero = QtWidgets.QAction(MainWindow)
        self.actionPrimero.setObjectName("actionPrimero")

        self.actionSegundo = QtWidgets.QAction(MainWindow)
        self.actionSegundo.setObjectName("actionSegundo")

        self.menuRecents.addAction(self.actionPrimero)
        self.menuRecents.addAction(self.actionSegundo)

        self.menuFile.addAction(self.menuRecents.menuAction())
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRecents.setTitle(_translate("MainWindow", "Recents"))
        self.actionPrimero.setText(_translate("MainWindow", "Primero"))
        self.actionSegundo.setText(_translate("MainWindow", "Segundo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())