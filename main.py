import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import *

import ui_Dialog_Proyecto
import ui_Dialog_Ticket
import ui_Dialog_Item
import ui_splash
import dataManager
import ui_contenedor
import ui_assets
assets = ui_assets.ui_assets

indice = int(0)
unaLista = []
# Combobox
listaItems = ["Guión / Ideas", "Storyboard", "Boceto", "Diseño 2D", "Animación 2D", "Diseño 3D", "Animación 3D", "Render 3D", "Edición Video", "Audio", "Render Video", "Otros", ""]


class Organizator(QtWidgets.QMainWindow, ui_contenedor.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Organizator, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Organizator 2000 (v1.0)")
        self.setWindowIcon(QtGui.QIcon('data/organizator.ico'))
        self.showMaximized()
        self.clockGet()

        self.PantallaSplash()

        # ---------------------------------------------- CAMBIA EL ESTILO VISUAL DEL SCROLL VERTICAL --------------------------
        # ---- Cambia desde la funcion de "ui_assets" ----
        assets.ScrollVStyle(self, self.sA_Botonera)
        assets.ScrollTickets(self, self.sArea_Tickets)

        self.funciones = dataManager.ManejaArchivos
        # ---- INICIA LOS BOTONES DE PROYECTOS Y LOS AGREGA AL GUI ----
        self.iniciaBotonera(self.funciones.cargaArchivo(self))
        # ---- INICIA LOS TICKETS DEL PROYECTO INICIAL Y LOS AGREGA AL GUI ----
        self.iniciaTickets(self.funciones.cargaArchivo(self), indice)


    # **********************************************************************************************************************************
    def iniciaBotonera(self, dataProject):
        for n in range(len(dataProject['Proyectos'])):
            if n != indice:
                proyActual = dataProject['Proyectos'][n]
                self.btnProyecto(proyActual['Titulo'], n)
            else:
                proyActual = dataProject['Proyectos'][n]
                self.btnActivo(proyActual['Titulo'], n)
        self.btnProjNew(len(dataProject['Proyectos']))
        # ---- AGREGA UN "Spacer" PARA ALINEAR LA LISTA DE BOTONES A LA PARTE SUPERIOR DEL CONTENEDOR DE LA BOTONERA ----
        self.elSpacerV = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vL_sAWC_Botonera.addItem(self.elSpacerV)

    def iniciaTickets(self, dataProyect, n):
        if len(dataProyect['Proyectos']) > 0:
            proyActual = dataProyect['Proyectos'][n]
            self.l_ticketsTitulo.setText(proyActual['Titulo'])
            assets.BotonEditar(self, lambda: self.EditaProyecto(proyActual['Titulo'], proyActual['Descripcion']), self.w_ProyectoEdit, self.hL_w_ProyectoEdit)
            spacerItemTitulo = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.hL_w_ticketsTitulo.addItem(spacerItemTitulo)
            self.l_ticketsDescripcion.setText(proyActual['Descripcion'])
            canTickets = len(proyActual['Tickets'])
            posFila = 0
            posColumna = 0
            # ---- Verifica que el proyecto seleccionado tiene tickets ----
            if canTickets != 0:
                for h in range(canTickets):
                    self.btnTicket(proyActual['Tickets'][h]['Tipo'], proyActual['Tickets'][h]['Titulo'], proyActual['Tickets'][h]['Descripcion'], proyActual['Tickets'][h]['Items'], h, posFila, posColumna)
                    posColumna += 1
                    if posColumna == 3:
                        posColumna = 0
                        posFila += 1
                    # ---- Verifica que el ticket actual tiene items ----
                    canItems = len(proyActual['Tickets'][h]['Items'])
                    if canItems != 0:
                        for k in range(canItems):
                            estado = bool(proyActual['Tickets'][h]['Items'][k][0])
                            if estado == True:
                                color = "color: rgb(60, 105, 0);"
                            else:
                                color = "color: rgb(119, 0, 0);"
                            self.btnCreaItems(proyActual['Tickets'][h]['Items'][k][1], estado, n, h, k, proyActual['Tickets'][h]['Items'][k][0], color)
                    self.spacerItemItems = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
                    self.vL_w_Trabajo.addItem(self.spacerItemItems)
            self.btnTicketNew(posFila, posColumna)
            # ---- Spacer HORIZONTAL de Filas ----
            self.spacerItemF = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.vL_sAWC_Tickets.addItem(self.spacerItemF, 0, 3, 1, 1)
            # ---- Spacer VERTICAL de Columnas ----
            self.spacerItemC = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.vL_sAWC_Tickets.addItem(self.spacerItemC, posFila+1, 0, 1, 1)

    def iniciaItems(self, ventana, wCont, lCont):
        global unaLista
        if len(unaLista) != 0:
            indiceV = 0
            for i in unaLista:
                self.btnItem(i[1], i, indiceV, ventana, wCont, lCont)
                indiceV += 1
        spacerItemI = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        lCont.addItem(spacerItemI)

    # **********************************************************************************************************************************
    def btnProyecto(self, vT, valor):
        btn = assets.BotonProyecto(self, vT, lambda: self.MuestraProyecto(valor), lambda: self.EliminaProyecto(valor), self.sAWC_Botonera, self.vL_sAWC_Botonera)
    def btnActivo(self, vT, valor):
        btn_act = assets.BotonActivo(self, vT, lambda: self.EliminaProyecto(valor), self.sAWC_Botonera, self.vL_sAWC_Botonera)
    def btnProjNew(self, largo):
        btn_new = assets.BotonAgregar(self, lambda: self.CreaProyecto(largo), self.sAWC_Botonera, self.vL_sAWC_Botonera)

    def btnTicket(self, tipo, vT, vD, vI, vTckt, posF, posC):
        tckt = assets.Ticket(self, tipo, vT, vD, lambda: self.EditaTicket(tipo, vT, vD, vTckt, vI), lambda: self.EliminaTicket(vTckt), posF, posC, self.sAWC_Tickets, self.vL_sAWC_Tickets)
    def btnTicketNew(self, posF, posC):
        tckt_new = assets.BotonTicketNuevo(self, lambda: self.CreaTicket(), posF, posC, self.sAWC_Tickets, self.vL_sAWC_Tickets)

    def btnCreaItems(self, texto, estado, indP, indT, indI, chck, color):
        itm = assets.CreaItem(self, texto, estado, lambda: self.Checkeado(indP, indT, indI, chck), color)

    def btnItem(self, texto, itemI, itemIE, ventana, wCont, lCont):
        assets.Items(self, texto, lambda: self.EliminaItem(itemI, ventana, wCont, lCont), lambda: self.EditaItem(texto, itemIE, ventana, wCont, lCont), wCont, lCont)


    def Checkeado(self, indP, indT, indI, chck):
        #print(chck)
        self.funciones.checkItem(self, self.funciones.cargaArchivo(self), indP, indT, indI, chck)
        self.LimpiaPantalla()

    # **********************************************************************************************************************************
    def MuestraProyecto(self, valor):
        global indice
        indice = valor
        self.LimpiaPantalla()

    def CreaProyecto(self, largo):
        global indice
        newIndice = largo
        Dialogo = QtWidgets.QDialog()
        uiD = ui_Dialog_Proyecto.Ui_Dialog()
        uiD.setupUi(Dialogo)
        # ---- Editando la ventana de Dialogo (Encabezado y textos de los botones) ----
        # Encabezado
        uiD.l_Encabezado.setText("Creación de un nuevo Proyecto")
        # Botones
        uiD.buttonBox.button(QDialogButtonBox.Ok).setText("Aceptar")
        uiD.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        # PlaceHolders
        uiD.iT_Titulo.setPlaceholderText("Tipear el Titulo del Proyecto")
        uiD.iT_Descripcion.setPlaceholderText("Describir el Proyecto")
        # ----  ----
        Dialogo.show()
        rsp = Dialogo.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QtWidgets.QDialog.Accepted:
            self.funciones.creaProyecto(self, self.funciones.cargaArchivo(self), uiD.iT_Titulo.text(), uiD.iT_Descripcion.toPlainText())
            indice = newIndice
            self.LimpiaPantalla()

    def EditaProyecto(self, tituloP, descripcionP):
        Dialogo = QtWidgets.QDialog()
        uiD = ui_Dialog_Proyecto.Ui_Dialog()
        uiD.setupUi(Dialogo)
        # ---- Editando la ventana de Dialogo (Encabezado y textos de los botones) ----
        # Encabezado
        encabezado = "Edición del Proyecto - " + str(tituloP)
        uiD.l_Encabezado.setText(encabezado)
        Dialogo.setWindowTitle(encabezado)
        # Botones
        uiD.buttonBox.button(QDialogButtonBox.Ok).setText("Aplicar")
        uiD.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        # Textos
        uiD.iT_Titulo.setText(tituloP)
        uiD.iT_Descripcion.setText(descripcionP)
        # ----  ----
        Dialogo.show()
        rsp = Dialogo.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QtWidgets.QDialog.Accepted:
            self.funciones.editaProyecto(self, self.funciones.cargaArchivo(self), uiD.iT_Titulo.text(), uiD.iT_Descripcion.toPlainText(), indice)
            self.LimpiaPantalla()

    def EliminaProyecto(self, n):
        choise = QtWidgets.QMessageBox.question(self, "Eliminar", "¿Seguro que se quiere eliminar el Proyecto?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choise == QtWidgets.QMessageBox.Yes:
            global indice
            # ---- LLAMA A LA FUNCION DE ELIMINAR EL PROYECTO PASANDOLE EL PARAMETRO "n" EL CUAL ES EL INDICE DEL BOTON CLICKEADO ----
            self.funciones.eliminaProyecto(self, self.funciones.cargaArchivo(self), n)
            # ---- VERIFICA QUE EL INDICE DEL BOTON CLICKEADO ES MAYOR AL VALOR DEL "indice" Y QUE "indice" SEA MAYOR A "0" ----
            ind_clk = n
            if indice > 0:
                if indice >= ind_clk:
                    indice -= 1
            else:
                self.l_ticketsTitulo.setText("")
                self.l_ticketsDescripcion.setText("")
            self.LimpiaPantalla()


    def CreaTicket(self):
        global unaLista
        unaLista = []
        Dialogo = QtWidgets.QDialog()
        uiD = ui_Dialog_Ticket.Ui_Dialog()
        uiD.setupUi(Dialogo)
        # ---- Editando la ventana de Dialogo (Encabezado, textos y comboBox de los tickets) ----
        # Encabezado
        Dialogo.setWindowTitle("Creación del Ticket")
        # Botones
        uiD.buttonBox.button(QDialogButtonBox.Ok).setText("Aplicar")
        uiD.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        # PlaceHolders
        uiD.iT_Titulo.setPlaceholderText("Tipear el Titulo del Ticket")
        uiD.iT_Descripcion.setPlaceholderText("Describir el Trabajo a realizar.")
        # Combobox
        for tipo in listaItems:
            uiD.comboBox_Tipo.addItem(tipo)
        uiD.comboBox_Tipo.setCurrentIndex(0)
        # ----  ----
        self.iniciaItems(Dialogo, uiD.w_Items, uiD.vL_w_Items)
        # ------------------
        uiD.pb_addItems.clicked.connect(lambda: self.AgregaItem(uiD.lE_addItem.text(), uiD.lE_addItem, Dialogo, uiD.w_Items, uiD.vL_w_Items))
        # ------------------
        Dialogo.show()
        rsp = Dialogo.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QtWidgets.QDialog.Accepted:
            self.funciones.creaTicket(self, self.funciones.cargaArchivo(self), uiD.comboBox_Tipo.currentIndex(), uiD.iT_Titulo.text(), uiD.iT_Descripcion.toPlainText(), unaLista, indice)
            self.LimpiaPantalla()
        else:
            self.LimpiaPantalla()

    def EditaTicket(self, tipoT, tituloT, descripcionT, indiceT, itemT):
        global unaLista
        unaLista = itemT
        Dialogo = QtWidgets.QDialog()
        uiD = ui_Dialog_Ticket.Ui_Dialog()
        uiD.setupUi(Dialogo)
        # ---- Editando la ventana de Dialogo (Encabezado, textos y comboBox de los tickets) ----
        # Encabezado
        encabezado = "Edición del Ticket - " + str(tituloT)
        uiD.l_Encabezado.setText(encabezado)
        Dialogo.setWindowTitle(encabezado)
        # Botones
        uiD.buttonBox.button(QDialogButtonBox.Ok).setText("Aplicar")
        uiD.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        # Textos
        uiD.iT_Titulo.setText(tituloT)
        uiD.iT_Descripcion.setText(descripcionT)
        # Combobox
        for tipo in listaItems:
            uiD.comboBox_Tipo.addItem(tipo)
        uiD.comboBox_Tipo.setCurrentIndex(tipoT)
        # ----  ----
        self.iniciaItems(Dialogo, uiD.w_Items, uiD.vL_w_Items)
        # ------------------
        uiD.pb_addItems.clicked.connect(lambda: self.AgregaItem(uiD.lE_addItem.text(), uiD.lE_addItem, Dialogo, uiD.w_Items, uiD.vL_w_Items))
        # ------------------
        Dialogo.show()
        rsp = Dialogo.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QtWidgets.QDialog.Accepted:
            self.funciones.editaTicket(self, self.funciones.cargaArchivo(self), uiD.comboBox_Tipo.currentIndex(), uiD.iT_Titulo.text(), uiD.iT_Descripcion.toPlainText(), unaLista, indice, indiceT)
            self.LimpiaPantalla()
        else:
            self.LimpiaPantalla()

    def EliminaTicket(self, h):
        choise = QtWidgets.QMessageBox.question(self, "Eliminar", "¿Seguro que se quiere eliminar el Ticket?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choise == QtWidgets.QMessageBox.Yes:
            global indice
            # ---- LLAMA A LA FUNCION DE ELIMINAR EL TICKET PASANDOLE EL PARAMETRO "h" EL CUAL ES EL INDICE DEL TICKET CONTENIENDO EL BOTON CLICKEADO ----
            self.funciones.eliminaTicket(self, self.funciones.cargaArchivo(self), indice, h)
            self.LimpiaPantalla()


    def AgregaItem(self, valorI, valorITxt, ventana, wCont, lCont):
        global unaLista
        unaLista.append([0, valorI])
        valorITxt.setText("")
        self.unfill(lCont)
        self.iniciaItems(ventana, wCont, lCont)

    def EditaItem(self, itemAnterior, itemIE, ventana, wCont, lCont):
        global unaLista
        DialogoI = QtWidgets.QDialog()
        uiDI = ui_Dialog_Item.Ui_Dialog()
        uiDI.setupUi(DialogoI)
        DialogoI.setWindowTitle("Editar Item")
        # Botones
        uiDI.buttonBox.button(QDialogButtonBox.Ok).setText("Aplicar")
        uiDI.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        # Texto
        uiDI.lE_Item.setText(itemAnterior)
        DialogoI.show()
        rsp = DialogoI.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QtWidgets.QDialog.Accepted:
            unaLista[itemIE][1] = uiDI.lE_Item.text()
        self.unfill(lCont)
        self.iniciaItems(ventana, wCont, lCont)
        ventana.activateWindow()

    def EliminaItem(self, itemI, ventana, wCont, lCont):
        global unaLista
        unaLista.remove(itemI)
        self.unfill(lCont)
        self.iniciaItems(ventana, wCont, lCont)

    # **********************************************************************************************************************************
    def unfill(self, elLayout):
        def deleteItems(layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        deleteItems(item.layout())
        deleteItems(elLayout)

    def LimpiaPantalla(self):
        global indice
        # ---- LIMPIA BOTONERA Y VUELVE A MOSTRAR LA BOTONERA NUEVA CON EL INDICE SELECCIONADO ----
        self.unfill(self.vL_sAWC_Botonera)
        self.iniciaBotonera(self.funciones.cargaArchivo(self))
        # ---- LIMPIA TICKETS Y VUELVE A MOSTRAR LOS TICKETS DEL PROYECTO SELECCIONADO ----
        self.unfill(self.vL_sAWC_Tickets)
        self.unfill(self.hL_w_ProyectoEdit)
        self.iniciaTickets(self.funciones.cargaArchivo(self), indice)

    # **********************************************************************************************************************************
    def clockGet(self):
        # ---- Timer ----
        self.timer = QtCore.QTimer()
        # ---- Connect timer ----
        self.timer.timeout.connect(self._update)
        # ---- start ----
        self.timer.start(1000)
    def _update(self):
        # ---- Update display each one second ----
        time = QtCore.QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(time)

    # **********************************************************************************************************************************
    def PantallaSplash(self):
        Dialogo = QtWidgets.QDialog()
        splash = ui_splash.Ui_d_Splash()
        splash.setupUi(Dialogo)
        Dialogo.setWindowTitle("Organizator 2000")
        Dialogo.setWindowIcon(QtGui.QIcon('data/organizator.ico'))
        pixmap = QtGui.QPixmap("data/splash_img_big.png")
        splash.l_img.setPixmap(pixmap)
        Dialogo.setWindowFlags(Dialogo.windowFlags() | QtCore.Qt.FramelessWindowHint)
        splash.pb_close.clicked.connect(lambda: self.btn_close(Dialogo))
        Dialogo.show()
        Dialogo.close()
        Dialogo.exec_()
    def btn_close(self, ventana):
        ventana.close()
        assets.Menues(self, self.l_Encabezado, self.dateTimeEdit, self.line_Tickets)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Organizator()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()