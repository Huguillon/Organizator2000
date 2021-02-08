import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import json
from pathlib import Path, PureWindowsPath
from filecmp import dircmp, cmp

import fileManager
fileManager = fileManager.FileManager()
import gui_MainWindow, gui_MenuBotones, gui_Reloj, gui_ProyectoBoton, gui_TrabajoBoton, gui_Spacers, gui_Ticket, gui_Dialogos, gui_Splash

btnMenu = gui_MenuBotones.Ui_MenuBotones()
reloj = gui_Reloj.Ui_Reloj()
btnProyecto = gui_ProyectoBoton.Ui_ProyectoBoton()
btnTrabajo = gui_TrabajoBoton.Ui_TrabajoBoton()
baseTicket = gui_Ticket.Ui_Ticket()
dialogos = gui_Dialogos.Ui_Dialogos()
spacers = gui_Spacers.Ui_Spacers()
splash = gui_Splash.Ui_Splash()

indiceP = int(0)
indiceT = int(0)
unaLista = []
skin = fileManager.skins[fileManager.dataInicial['Skin']]

# Combobox
listaItems = fileManager.dataInicial['listaItems']


class Organizator(QMainWindow, gui_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Organizator, self).__init__(parent)

        self.mainWindow(self, skin)
        # ---- Setea el titulo y el icono de la ventana
        self.textoFijo = "Organizator 2000 (v2.0.3) - "
        if fileManager.igualData:
            self.setWindowTitle(self.textoFijo + fileManager.actual_file)
            self.setWindowIcon(QIcon('images/icon256.png'))
        else:
            self.setWindowTitle(self.textoFijo + fileManager.actual_file + " (*)")
            self.setWindowIcon(QIcon('images/icon256_unsave.png'))

        # ---- Maximiza la ventana a pantalla completa
        posicionInicial = (fileManager.dataInicial['PosWindow'][0], fileManager.dataInicial['PosWindow'][1])
        self.move(posicionInicial[0], posicionInicial[1])
        self.showMaximized()

        # ---- Agrega la barra de Menu
        self.menuBarFull(self.quit_trigger, self.respond, self.respSkins, self.respEdit)

        # ---- Agrega el reloj ----
        reloj.reloj(self.w_Reloj, self.hL_Reloj, skin)

        # ---- Inicia el reloj y fecha
        self.clockGet()

        # ---- Agrega los botones de Menu (Nuevo / Abrir / Guardar / Guardar Como...) ----
        btnMenu.menuBotones(self.w_Menu, self.hL_Menu, lambda: self.btnNuevo(), lambda: self.btnAbre(), lambda: self.btnGuarda(), lambda: self.btnGuardaComo(), skin)

        # ---- Inicia SPLASH ----
        self.PantallaSplash()

        # ---- Inicia los botones y los tickets ----
        self.iniciaPizarra()


    # ------------------------------------------------------------------------------------------------------------------
    # /////////////////////////////////////////////// INICIA LA PIZARRA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    def iniciaPizarra(self):
        global indiceP
        global indiceT
        indiceP = fileManager.data['Indice']
        # ---- Inicia Botones PROYECTOS ----
        for p in range(len(fileManager.data['Proyectos'])):
            if p != indiceP:
                self.botonProyecto(p)
            else:
                self.botonProyectoActivo(p)
                indiceT = fileManager.data['Proyectos'][p][2]
                if len(fileManager.data['Proyectos'][p][3]) != 0:
                    # ---- Inicia Botones TRABAJOS ----
                    for t in range(len(fileManager.data['Proyectos'][p][3])):
                        if t != indiceT:
                            self.botonTrabajo(p, t)
                        else:
                            self.botonTrabajoActivo(p, t)
                            # ---- Verifica que la cantidad de trabajos sea mayor a 0 ----
                            self.l_ticketsTitulo.setText(fileManager.data['Proyectos'][p][3][t][0])
                            self.l_ticketsDescripcion.setText(fileManager.data['Proyectos'][p][3][t][1])
                            pf = 0
                            pc = 0
                            if len(fileManager.data['Proyectos'][p][3][t][2]) != 0:
                                # ---- Inicia TICKETS ----
                                for tk in range(len(fileManager.data['Proyectos'][p][3][t][2])):
                                    self.ticket(p, t, tk, pf, pc)
                                    pc += 1
                                    if pc == 5:
                                        pc = 0
                                        pf += 1
                                    # ---- Verifica que el ticket actual tiene items ----
                                    if len(fileManager.data['Proyectos'][p][3][t][2][tk][3]) != 0:
                                        # ---- Inicia ITEMS ----
                                        for i in range(len(fileManager.data['Proyectos'][p][3][t][2][tk][3])):
                                            estado = bool(fileManager.data['Proyectos'][p][3][t][2][tk][3][i][0])
                                            if estado == True:
                                                color = skin['checkbox_uncheck']
                                            else:
                                                color = skin['checkbox_check']
                                            self.item(p, t, tk, i, color)
                            # ---- Agrega el boton "TICKET NUEVO" ----
                            baseTicket.ticketNuevo(lambda: self.btnnewTk(), self.sAWC_Tickets, self.vL_sAWC_Tickets, pf, pc, skin)
                            spacers.spacerTickets(0, 0, self.vL_sAWC_Tickets, pf+1, 5)
                else:
                    self.l_ticketsTitulo.setText("No hay trabajos en el proyecto")
                    self.l_ticketsDescripcion.setText("")
                # ---- Agrega el boton "TRABAJO NUEVO" ----
                btnTrabajo.botonTrabajoNuevo(lambda: self.btnnewT(), btnProyecto.w_btnTrabContainer, btnProyecto.vL_btnTrabContainer, skin)
        # ---- Agrega el boton "PROYECTO NUEVO" ----
        btnProyecto.botonProyNuevo(lambda: self.btnnewP(), self.sAWC_Botonera, self.vL_sAWC_Botonera, skin)
        spacers.spacer(20, 20, self.vL_sAWC_Botonera)

    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////////// BASE DE BOTONES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    def botonProyecto(self, p):
        btnProyecto.botonProyecto(fileManager.data['Proyectos'][p][0], str(p), fileManager.data['Proyectos'][p][1], lambda: self.btnShowP(p), lambda: self.btnEditP(p), lambda: self.btnDelP(p), lambda: self.btnSortP(p), self.sAWC_Botonera, self.vL_sAWC_Botonera, skin)
    def botonProyectoActivo(self, p):
        btnProyecto.botonProyActivo(fileManager.data['Proyectos'][p][0], str(p), fileManager.data['Proyectos'][p][1], lambda: self.btnEditP(p), lambda: self.btnDelP(p), self.sAWC_Botonera, self.vL_sAWC_Botonera, skin)

    def botonTrabajo(self, p, t):
        btnTrabajo.botonTrabajo(fileManager.data['Proyectos'][p][3][t][0], lambda: self.btnShowT(p, t), lambda: self.btnEditT(p, t), lambda: self.btnDelT(p, t), btnProyecto.w_btnTrabContainer, btnProyecto.vL_btnTrabContainer, skin)
    def botonTrabajoActivo(self, p, t):
        btnTrabajo.botonTrabActivo(fileManager.data['Proyectos'][p][3][t][0], lambda: self.btnEditT(p, t), lambda: self.btnDelT(p, t), btnProyecto.w_btnTrabContainer, btnProyecto.vL_btnTrabContainer, skin)

    def ticket(self, p, t, tk, pf, pc):
        baseTicket.ticket(fileManager.dataInicial['listaItems'], fileManager.data['Proyectos'][p][3][t][2][tk][0], fileManager.data['Proyectos'][p][3][t][2][tk][1], fileManager.data['Proyectos'][p][3][t][2][tk][2], lambda: self.btnDelTk(tk), lambda: self.btnEditTk(tk), lambda: self.btnCopyTk(tk), lambda: self.btnInfoTk(fileManager.data['Proyectos'][p][3][t][2][tk][2]), self.sAWC_Tickets, self.vL_sAWC_Tickets, pf, pc, skin)
    def item(self, p, t, tk, i, color):
        baseTicket.items(fileManager.data['Proyectos'][p][3][t][2][tk][3][i][1], fileManager.data['Proyectos'][p][3][t][2][tk][3][i][0], lambda: self.Checkeado(p, t, tk, i, fileManager.data['Proyectos'][p][3][t][2][tk][3][i][0]), color)
    def Checkeado(self, p, t, tk, i, chck):
        fileManager.checkItem(p, t, tk, i, chck)
        self.limpiaPantalla()

    # ------------------------------------------------------------------------------------------------------------------
    # /////////////////////////////////////////////// ACCIONES DE BOTONES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------- Menu ---------------------------------------------------
    def btnNuevo(self):
        if fileManager.igualData == False:
            if fileManager.actual_file == "":
                # Pregunta y abre DIALOGO para guardar
                choise = QMessageBox.question(self, "Advertencia", "La pizarra actual no se ha guardado ¿Guardar el archivo?", QMessageBox.Yes | QMessageBox.No)
                if choise == QMessageBox.Yes:
                    fileManager.guardarComoDialogo(self)
            else:
                # Pregunta y GUARDA
                choise = QMessageBox.question(self, "Advertencia", 'Los cambios en "' + str(fileManager.archivo) + '" no se han guardado ¿Guardar el archivo?', QMessageBox.Yes | QMessageBox.No)
                if choise == QMessageBox.Yes:
                    fileManager.guardar()
        fileManager.nuevo()
        self.limpiaPantalla()
        self.l_ticketsTitulo.setText("")
    def btnAbre(self):
        if fileManager.igualData == False:
            if fileManager.actual_file == "":
                # Pregunta y abre DIALOGO para guardar
                choise = QMessageBox.question(self, "Advertencia", "La pizarra actual no se ha guardado ¿Guardar el archivo?", QMessageBox.Yes | QMessageBox.No)
                if choise == QMessageBox.Yes:
                    fileManager.guardarComoDialogo(self)
            else:
                # Pregunta y GUARDA
                choise = QMessageBox.question(self, "Advertencia", 'Los cambios en "' + str(fileManager.archivo) + '" no se han guardado ¿Guardar el archivo?', QMessageBox.Yes | QMessageBox.No)
                if choise == QMessageBox.Yes:
                    fileManager.guardar()
        fileManager.abrirDialogo(self)
        self.limpiaPantalla()
    def btnGuarda(self):
        if fileManager.actual_file != "":
            fileManager.guardar()
        else:
            fileManager.guardarComoDialogo(self)
        self.limpiaPantalla()
    def btnGuardaComo(self):
        fileManager.guardarComoDialogo(self)
        self.limpiaPantalla()

    # ----------------------------------------------------- Botonera Proyectos -----------------------------------------
    def btnShowP(self, p):
        global indiceP
        global indiceT
        fileManager.guardaIndice(p)
        indiceP = fileManager.data['Indice']
        indiceT = fileManager.data['Proyectos'][p][2]
        self.limpiaPantalla()
    def btnDelP(self, p):
        global indiceP
        choise = QMessageBox.question(self, "Eliminar Trabajo", "¿Seguro que quiere eliminar el Proyecto?", QMessageBox.Yes | QMessageBox.No)
        if choise == QMessageBox.Yes:
            fileManager.eliminaProyecto(p)
            indiceP = fileManager.data['Indice']
            self.limpiaPantalla()
    def btnEditP(self, p):
        dialogos.dialogoProyecto(self, False, fileManager.data['Proyectos'][p][0], fileManager.data['Proyectos'][p][1], "Editar Proyecto\n" + str(fileManager.data['Proyectos'][p][0]), skin)
        if dialogos.rspDialogP == QDialog.Accepted:
            fileManager.editaProyecto(p, dialogos.le_TituloP.text(), dialogos.te_DescripcionP.toPlainText())
            self.limpiaPantalla()
    def btnnewP(self):
        global indiceP
        dialogos.dialogoProyecto(self, True, "Escribir un Titulo del Proyecto", "Describir el Proyecto", "Crear un nuevo Proyecto", skin)
        if dialogos.rspDialogP == QDialog.Accepted:
            fileManager.creaProyecto(dialogos.le_TituloP.text(), dialogos.te_DescripcionP.toPlainText())
            indiceP = fileManager.data['Indice']
            self.limpiaPantalla()
    def btnSortP(self, p):
        fileManager.ordenaLista(fileManager.data['Proyectos'], p, 5)
        self.limpiaPantalla()

    # ----------------------------------------------------- Botonera Trabajos ------------------------------------------
    def btnShowT(self, p, t):
        global indiceT
        fileManager.guardaIndTrabajo(p, t)
        indiceT = fileManager.data['Proyectos'][p][2]
        self.limpiaPantalla()
    def btnDelT(self, p, t):
        global indiceT
        choise = QMessageBox.question(self, "Eliminar Trabajo", "¿Seguro que quiere eliminar el Trabajo?", QMessageBox.Yes | QMessageBox.No)
        if choise == QMessageBox.Yes:
            fileManager.eliminaTrabajo(p, t)
            indiceT = fileManager.data['Proyectos'][p][2]
            self.limpiaPantalla()
    def btnEditT(self, p, t):
        dialogos.dialogoProyecto(self, False, fileManager.data['Proyectos'][p][3][t][0], fileManager.data['Proyectos'][p][3][t][1], "Editar Trabajo - " + str(fileManager.data['Proyectos'][p][3][t][0]), skin)
        if dialogos.rspDialogP == QDialog.Accepted:
            fileManager.editaTrabajo(p, t, dialogos.le_TituloP.text(), dialogos.te_DescripcionP.toPlainText())
            self.limpiaPantalla()
    def btnnewT(self):
        global indiceT
        dialogos.dialogoProyecto(self, True, "Escribir un Titulo del Trabajo", "Describir el Trabajo", "Crear un nuevo Trabajo", skin)
        if dialogos.rspDialogP == QDialog.Accepted:
            fileManager.creaTrabajo(indiceP, dialogos.le_TituloP.text(), dialogos.te_DescripcionP.toPlainText())
            indiceT = fileManager.data['Proyectos'][indiceP][2]
            self.limpiaPantalla()
    def btnSortT(self, p, t):
        fileManager.ordenaLista(fileManager.data['Proyectos'][p][3], t, 5)
        self.limpiaPantalla()

    # ----------------------------------------------------- Botonera Tickets -------------------------------------------
    def btnDelTk(self, tk):
        choise = QMessageBox.question(self, "Eliminar Ticket", "¿Seguro que quiere eliminar el Ticket?", QMessageBox.Yes | QMessageBox.No)
        if choise == QMessageBox.Yes:
            fileManager.eliminaTicket(indiceP, indiceT, tk)
            self.limpiaPantalla()
    def btnEditTk(self, tk):
        global unaLista
        unaLista = fileManager.data['Proyectos'][indiceP][3][indiceT][2][tk][3]
        Dialogo = QDialog(self)
        dialogos.dialogTicket(listaItems, Dialogo, False, fileManager.data['Proyectos'][indiceP][3][indiceT][2][tk][0], fileManager.data['Proyectos'][indiceP][3][indiceT][2][tk][1], fileManager.data['Proyectos'][indiceP][3][indiceT][2][tk][2], "Edición del Ticket - " + str(fileManager.data['Proyectos'][indiceP][3][indiceT][2][tk][1]), lambda: self.btnAddI(dialogos.le_addItem.text(), dialogos.le_addItem, dialogos.w_Items, dialogos.vL_w_Items), skin)
        self.iniciaItems(dialogos.w_Items, dialogos.vL_w_Items)
        # ----  ----
        Dialogo.show()
        rsp = Dialogo.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QDialog.Accepted:
            fileManager.editaTicket(indiceP, indiceT, tk, dialogos.comboBox_Tipo.currentIndex(), dialogos.le_TituloT.text(), dialogos.te_DescripcionT.toPlainText(), unaLista)
            self.limpiaPantalla()
    def btnCopyTk(self, tk):
        fileManager.copiaTicket(indiceP, indiceT, tk)
        self.limpiaPantalla()
    def btnInfoTk(self, descripcion):
        aviso = QMessageBox.information(self, "Información", descripcion, QMessageBox.Ok)
    def btnnewTk(self):
        global unaLista
        unaLista = []
        Dialogo = QDialog(self)
        dialogos.dialogTicket(listaItems, Dialogo, True, 0, "Escribir un Titulo del Ticket", "Describir el Ticket", "Crear un nuevo Ticket", lambda: self.btnAddI(dialogos.le_addItem.text(), dialogos.le_addItem, dialogos.w_Items, dialogos.vL_w_Items), skin)
        self.iniciaItems(dialogos.w_Items, dialogos.vL_w_Items)
        # ----  ----
        Dialogo.show()
        rsp = Dialogo.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QDialog.Accepted:
            fileManager.creaTicket(indiceP, indiceT, dialogos.comboBox_Tipo.currentIndex(), dialogos.le_TituloT.text(), dialogos.te_DescripcionT.toPlainText(), unaLista)
            self.limpiaPantalla()
    def btnSortTk(self, tk):
        # fileManager.ordenaLista(fileManager.data['Proyectos'][p][3], t, 5)
        fileManager.ordenaLista(fileManager.data['Proyectos'][indiceP][3][indiceT][2], tk, 5)
        self.limpiaPantalla()

    def iniciaItems(self, wCont, lCont):
        global unaLista
        if len(unaLista) != 0:
            indiceV = 0
            for i in unaLista:
                self.btnItem(i[1], i, indiceV, wCont, lCont)
                indiceV += 1
    def btnItem(self, texto, itemI, itemIE, wCont, lCont):
        dialogos.btnDialogItem(texto, lambda: self.btnDelI(itemI, wCont, lCont), lambda: self.btnEditI(texto, itemIE, wCont, lCont), wCont, lCont, skin)

    # ------------------------------------------------- Edición de ITEMS -----------------------------------------------
    # ---- Agrega un item en la ventana de Dialogo
    def btnAddI(self, valorI, campoT, wCont, lCont):
        global unaLista
        unaLista.append([1, valorI])
        campoT.setText("")
        self.unfill(lCont)
        self.iniciaItems(wCont, lCont)
    # ---- Elimina un item de la ventana de Dialogo
    def btnDelI(self, itemI, wCont, lCont):
        global unaLista
        unaLista.remove(itemI)
        self.unfill(lCont)
        self.iniciaItems(wCont, lCont)
    # ---- Edita un item de la ventana de Dialogo
    def btnEditI(self, itemAnterior, itemI, wCont, lCont):
        global unaLista
        listaTemp = unaLista
        DialogoI = QDialog(self)
        dialogos.dialogItem(DialogoI, itemAnterior, skin)
        DialogoI.setWindowTitle("Editar Item")
        DialogoI.show()
        rsp = DialogoI.exec_()  # exec_() es para que no se cierre inmediatamente la ventana de Dialogo
        if rsp == QDialog.Accepted:
            listaTemp[itemI][1] = dialogos.lE_Item.text()
            unaLista = listaTemp
        self.unfill(lCont)
        self.iniciaItems(wCont, lCont)

    def quit_trigger(self):
        if fileManager.igualData == False:
            choise = QMessageBox.question(self, "Salir", "¿Guardar la pizarra antes de salir?", QMessageBox.Yes | QMessageBox.No)
            if choise == QMessageBox.Yes:
                if fileManager.actual_file != "":
                    self.btnGuarda()
                else:
                    self.btnGuardaComo()
        fileManager.guardaPos(self.x(), self.y())
        sys.exit(qApp.exec_())

    def respond(self, q):
        signal = q.text()
        if signal == 'Nuevo':
            self.btnNuevo()
        elif signal == 'Abrir':
            self.btnAbre()
        elif signal == 'Guardar':
            self.btnGuarda()
        elif signal == 'Guardar como...':
            self.btnGuardaComo()

    def respSkins(self, q):
        global skin
        signal = q.text()
        fileManager.guardaSkin(signal)
        skin = fileManager.skins[fileManager.dataInicial['Skin']]
        self.menuBar.setStyleSheet(skin['menuBar'])
        self.centralwidget.setStyleSheet(skin['centralwidget'])
        self.l_ticketsTitulo.setStyleSheet(skin['l_ticketsTitulo'])
        self.line_Tickets.setStyleSheet(skin['line_Tickets'])
        self.l_ticketsDescripcion.setStyleSheet(skin['l_ticketsDescripcion'])
        self.sAWC_Tickets.setStyleSheet(skin['sAWC_Tickets'])
        self.limpiaCabezal()
        self.limpiaPantalla()

    def respEdit(self, q):
        signal = q.text()
        if signal == 'Ideas Generales':
            fileManager.creaTicket(indiceP, indiceT, 0, "Ideas generales", "(En un TXT) Cerrar las ideas generales de lo que sería la serie, y anotar ideas sueltas de los capitulos que se me vayan ocurriendo.", [[1, "Ideas generales"], [1, "Ideas de Capitulos"]])
            self.limpiaPantalla()
        elif signal == 'Guión':
            fileManager.creaTicket(indiceP, indiceT, 0, "Guión", "Crear el guión.", [[1, "Idea general"], [1, "Refinamiento"]])
            self.limpiaPantalla()
        elif signal == 'Storyboard':
            fileManager.creaTicket(indiceP, indiceT, 1, "Storyboard / Animatic", "Crear el Storyboard y el Animatic", [[1, "Storyboard"], [1, "Animatic"]])
            self.limpiaPantalla()
        elif signal == 'Diseño 3D':
            fileManager.creaTicket(indiceP, indiceT, 5, "Titulo temporal", "Descripción temporal", [[1, "Modelado"], [1, "UVW"], [1, "Texturas"], [1, "Rigging"]])
            self.limpiaPantalla()

    # ------------------------------------------------------------------------------------------------------------------
    # ////////////////////////////////////////// LIMPIA Y REINICIA LA PANTALLA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
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

    def limpiaPantalla(self):
        # ---- LIMPIA BOTONERA Y VUELVE A MOSTRAR LA BOTONERA NUEVA CON EL INDICE SELECCIONADO ----
        self.unfill(self.vL_sAWC_Botonera)
        # # ---- LIMPIA TICKETS Y VUELVE A MOSTRAR LOS TICKETS DEL PROYECTO SELECCIONADO ----
        self.unfill(self.vL_sAWC_Tickets)
        fileManager.resetData()
        self.iniciaPizarra()
        if fileManager.igualData:
            self.setWindowTitle(self.textoFijo + fileManager.actual_file)
            self.setWindowIcon(QIcon('images/icon256.png'))
        else:
            self.setWindowTitle(self.textoFijo + fileManager.actual_file + " (*)")
            self.setWindowIcon(QIcon('images/icon256_unsave.png'))
    def limpiaCabezal(self):
        self.unfill(self.hL_Menu)
        self.unfill(self.hL_Reloj)
        # ---- Agrega los botones de Menu (Nuevo / Abrir / Guardar / Guardar Como...) ----
        btnMenu.menuBotones(self.w_Menu, self.hL_Menu, lambda: self.btnNuevo(), lambda: self.btnAbre(), lambda: self.btnGuarda(), lambda: self.btnGuardaComo(), skin)
        # ---- Agrega el reloj ----
        reloj.reloj(self.w_Reloj, self.hL_Reloj, skin)

    # ---- Metodo para obtener la posición de la ventana en la pantalla ----
    def moveEvent(self, e):
        super(Organizator, self).moveEvent(e)

    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////// RELOJ Y TEMPORIZADOR \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    def clockGet(self):
        # ---- Timer ----
        self.timer = QTimer()
        # ---- Connect timer ----
        self.timer.timeout.connect(self._update)
        # ---- start ----
        self.timer.start(1000)

    def _update(self):
        # ---- Update display each one second ----
        time = QDateTime.currentDateTime()
        # self.dateTimeEdit.setDateTime(time)
        reloj.dateTimeEdit.setDateTime(time)

    # ------------------------------------------------------------------------------------------------------------------
    # //////////////////////////////////////////////// PANTALLA SPLASH \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    def PantallaSplash(self):
        Dialogo = QDialog()
        pixmap = QPixmap("images/splash_v2b.png")
        splash.Splash(Dialogo, pixmap, lambda: self.btn_close(Dialogo), skin)
        Dialogo.setWindowFlags(Dialogo.windowFlags() | Qt.FramelessWindowHint)
        Dialogo.show()
        self.clockGetClose(Dialogo)
        Dialogo.exec_()
    def clockGetClose(self, ventanaClose):
        # ---- Timer ----
        self.timerClose = QTimer()
        # ---- Connect timer ----
        self.timerClose.timeout.connect(lambda: self.btn_close(ventanaClose))
        # ---- start ----
        self.timerClose.start(1700)
    def btn_close(self, ventana):
        ventana.close()

    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////////// CERRAR VENTANA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Evento que permite que al precionar la X de la ventana se abra un popup preguntando si se quiere guardar el archivo antes de cerrar
    def closeEvent(self, event):
        # ---- print("User has clicked the red x on the main window") ----
        self.quit_trigger()



if __name__ == '__main__':
    # main()
    app = QApplication(sys.argv)
    ventana = Organizator()
    ventana.show()
    # sys.exit(app.exec_())
    sys.exit(ventana.closeEvent(app.exec_()))