# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_spinbox2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(70, 100, 41, 21))
        self.spinBox.setFrame(False)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)

        self.spinBox.setStyleSheet("QSpinBox {\b"
                                   "background-color: yellow;\b"
                                   "padding-right: 15px;\b"
                                   "border-image: url(:/images/frame.png) 4;\b"
                                   "border-width: 3;}")
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setAccelerated(True)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(500)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
