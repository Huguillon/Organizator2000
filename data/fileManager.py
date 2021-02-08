# -*- coding: utf-8 -*-
import json
from pathlib import Path
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

skin_file = Path("data/skins.json")
my_file = Path("")
temp_file = Path("data/temp.json")
# test_file = Path("data/test.json")
init_file = Path("data/dataInicial.json")
tabulacion = 4

class FileManager():
    data = {}
    dataTemp = {}
    dataInicial = {}
    actual_file = Path("")
    igualData = True
    archivo = ""
    skins = {}
    # recientes = []
    def __init__(self):
        self.iniciaSkin()
        self.iniciaData()
        self.iniciaPrograma()



    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////////////// ARCHIVOS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Inicia el programa ----
    def iniciaPrograma(self):
        global temp_file
        global my_file
        archivoInicial = self.dataInicial['Ultimo']
        # ---- TRY por si el archivo fue eliminado o movido, evita que el programa crashee ----
        try:
            if archivoInicial != "":
                # ---- Copia el  contenido del archivo JSON en el diccionario "data" ----
                with open(archivoInicial, 'r') as f:
                    self.data = json.load(f)
                # ---- Copia el  contenido del diccionario "data" en el JSON temporal ----
                with open(temp_file, 'w') as t:
                    json.dump(self.data, t, indent=tabulacion)
                my_file = archivoInicial
                self.actual_file = archivoInicial
                self.igualData = True
                # filename_ruta = os.path.basename(self.actual_file)
                # filename = os.path.split(filename_ruta)
                # self.archivo = filename[1]
                # self.archivo = filename_ruta
            else:
                self.nuevo()
        except:
            self.nuevo()
            self.dataInicial['Ultimo'] = ""
            with open(init_file, 'w') as d:
                json.dump(self.dataInicial, d, indent=tabulacion)

    # ---- Nuevo Archivo ----
    def nuevo(self):
        global temp_file
        global my_file
        # ---- Genera el diccionario Base para meter en el JSON ----
        self.data = {"Proyectos": [], "Indice": 0}
        my_file = ""
        self.actual_file = my_file
        # ----  ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)
        self.igualData = False
        return self.data

    # ---- Abre Archivo Dialogo ----
    def abrirDialogo(self, ubicacion):
        global temp_file
        global my_file
        global init_file
        #---- USA UN TRY PARA QUE AL CANCELAR EL ABRIR EL ARCHIVO NO CRASHEE EL PROGRAMA ----
        try:
            filename = QFileDialog.getOpenFileName(ubicacion, 'Abrir Archivo', "", 'All Files (*.json)', os.getenv('HOME'))
            with open(filename[0], 'r') as f:
                self.data = json.load(f)
                # ---- Copia el  contenido del diccionario "data" en el JSON temporal ----
                with open(temp_file, 'w') as t:
                    json.dump(self.data, t, indent=tabulacion)
                #----- Obtiene la ruta del archivo abierto y Guardar la ruta (Path) del archivo original abierto "filename"
                my_file = filename[0]
                self.actual_file = my_file
                self.igualData = True
                # ---- Guarda la ruta del archivo abierto para volver a abrirlo automaticamente la siguiente vez que se inicia el programa ----
                self.dataInicial['Ultimo'] = my_file
                # ---- Guarda la ruta del archivo abierto en la lista de "archivos recientes" ----
                # # ---- Organiza la lista de recientes para ubicar el ultimo abierto en la parte superior
                if my_file in self.dataInicial['Recientes']:
                    self.dataInicial['Recientes'].remove(my_file)
                self.dataInicial['Recientes'].insert(0, my_file)
                # ---- Guarda las modificaciones en el archivo "init_file" ----
                with open(init_file, 'w') as d:
                    json.dump(self.dataInicial, d, indent=tabulacion)
        except:
            pass


    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------- Carga archivo version original del v1.00 ----
    def abreReciente(self, elArchivo):
        global temp_file
        global my_file
        with open(elArchivo) as f:
            self.data = json.load(f)
        # ---- Copia el contenido del diccionario "data" en el JSON temporal ----
        with open(temp_file, 'w') as t:
            json.dump(self.data, t, indent=tabulacion)
        # ---- Obtiene la ruta del archivo abierto y Guardar la ruta (Path) del archivo original abierto "filename"
        my_file = elArchivo
        self.actual_file = my_file
        self.igualData = True
        # ---- Organiza la lista de recientes para ubicar el ultimo abierto en la parte superior
        tempList = self.dataInicial['Recientes'].copy()
        tempList.remove(my_file)
        tempList.insert(0, my_file)
        self.dataInicial['Recientes'] = tempList
        # ---- Guarda la ruta del archivo abierto para volver a abrirlo automaticamente la siguiente vez que se inicia el programa ----
        self.dataInicial['Ultimo'] = my_file
        # ---- Guarda las modificaciones en el archivo "init_file" ----
        with open(init_file, 'w') as d:
            json.dump(self.dataInicial, d, indent=tabulacion)

    def missingReciente(self, elArchivo):
        global my_file
        # ---- Obtiene la ruta del archivo abierto y Guardar la ruta (Path) del archivo original abierto "filename"
        my_file = elArchivo
        # ---- Organiza la lista de recientes para ubicar el ultimo abierto en la parte superior
        self.dataInicial['Recientes'].remove(my_file)
        # tempList = self.dataInicial['Recientes'].copy()
        # tempList.remove(my_file)
        # tempList.insert(0, my_file)
        # self.dataInicial['Recientes'] = tempList
        # ---- Guarda las modificaciones en el archivo "init_file" ----
        with open(init_file, 'w') as d:
            json.dump(self.dataInicial, d, indent=tabulacion)

    # ---- Guarda Archivo ----
    def guardar(self):
        global my_file
        self.igualData = True
        self.resetData()
        # ---- Copia el  contenido del diccionario "data" en el JSON ----
        with open(my_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Guarda Archivo Dialogo ----
    def guardarComoDialogo(self, ubicacion):
        global temp_file
        global my_file
        try:
            filename = QFileDialog.getSaveFileName(ubicacion, 'Guardar Archivo', "", 'All Files (*.json)', os.getenv('HOME'))
            with open(filename[0], 'w') as f:
                json.dump(self.data, f, indent=tabulacion)
            # ---- Copia el  contenido del diccionario "data" en el JSON temporal ----
            with open(temp_file, 'w') as t:
                json.dump(self.data, t, indent=tabulacion)
            #----- Obtiene la ruta del archivo abierto y Guardar la ruta (Path) del archivo original abierto "filename"
            my_file = filename[0]
            self.actual_file = my_file
            self.igualData = True
            # ---- Guarda la ruta del archivo abierto para volver a abrirlo automaticamente la siguiente vez que se inicia el programa ----
            self.dataInicial['Ultimo'] = my_file
            # ---- Guarda la ruta del archivo abierto en la lista de "archivos recientes" ----
            self.dataInicial['Recientes'].insert(0, my_file)
            # ---- Guarda las modificaciones en el archivo "init_file" ----
            with open(init_file, 'w') as d:
                json.dump(self.dataInicial, d, indent=tabulacion)
        except:
            pass


    # ---- Nuevo Indice Proyecto ----
    def guardaIndice(self, vIndice):
        global temp_file
        global my_file
        # ---- Modifica el valor de 'Indice' en el diccionario "data" y mantiene todos los cambios temporales ----
        self.data['Indice'] = vIndice
        # ---- Copia el  contenido del diccionario "data" en el JSON TEMPORAL ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)
        # ----------------------------------------------------------- Guarda SOLO el inidice en el archivo ORIGINAL ----
        if self.igualData == True:
            # ---- Abre el archivo original y guarda el contenido en "dataTemp" ----
            with open(my_file, 'r') as mf:
                self.dataTemp = json.load(mf)
            # ---- Modifica el valor de 'Indice' en el diccionario "dataTemp" ----
            self.dataTemp['Indice'] = vIndice
            # ---- Copia el  contenido del diccionario "dataTemp" en el JSON ORIGINAL ----
            with open(my_file, 'w') as t:
                json.dump(self.dataTemp, t, indent=tabulacion)

    # ---- Guarda Indice Trabajo ----
    def guardaIndTrabajo(self, proy, vIndice):
        global temp_file
        global my_file
        # ---- Modifica el valor de 'Indice' en el diccionario "data" y mantiene todos los cambios temporales ----
        self.data['Proyectos'][proy][2] = vIndice
        # ---- Copia el  contenido del diccionario "data" en el JSON TEMPORAL ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)
        # ----------------------------------------------------------- Guarda SOLO el inidice en el archivo ORIGINAL ----
        if self.igualData == True:
            # ---- Abre el archivo original y guarda el contenido en "dataTemp" ----
            with open(my_file, 'r') as mf:
                self.dataTemp = json.load(mf)
            # ---- Modifica el valor de 'Indice' en el diccionario "dataTemp" ----
            self.dataTemp['Proyectos'][proy][2] = vIndice
            # ---- Copia el  contenido del diccionario "dataTemp" en el JSON ORIGINAL ----
            with open(my_file, 'w') as t:
                json.dump(self.dataTemp, t, indent=tabulacion)

    # # ---- Guarda Archivos abiertos recientes ----
    # def guardaRecientes(self):
    #     listaTemp = self.dataInicial['Recientes']



    # ------------------------------------------------------------------------------------------------------------------
    # //////////////////////////////////////////////////// PROYECTOS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Nuevo Proyecto ----
    def creaProyecto(self, tituloValor, descValor):
        global temp_file
        self.igualData = False
        # ---- Agregando nuevos proyectos al archivo ----
        self.data['Proyectos'].append([tituloValor, descValor, 0, []])
        self.data['Indice'] = len(self.data['Proyectos']) - 1
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Elimina Proyecto ----
    def eliminaProyecto(self, indProyecto):
        global temp_file
        self.igualData = False
        # ---- Hace que el trabajo seleccionado siga seleccionado si se borra un trabajo anterior ----
        if self.data['Indice'] > 0 and self.data['Indice'] >= indProyecto:
                self.data['Indice'] -= 1
        # ---- Elimina el trabajo ----
        del self.data['Proyectos'][indProyecto]
        # ---- Copia el  contenido del diccionario "data" en el JSON TEMP ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Edita Proyecto ----
    def editaProyecto(self, indProyecto, titulo, descripcion):
        global temp_file
        self.igualData = False
        self.data['Proyectos'][indProyecto][0] = titulo
        self.data['Proyectos'][indProyecto][1] = descripcion
        # ---- Copia el  contenido del diccionario "data" en el JSON TEMP ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)


    # ------------------------------------------------------------------------------------------------------------------
    # //////////////////////////////////////////////////// TRABAJOS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Nuevo Trabajo ----
    def creaTrabajo(self, indProyecto, tituloValor, descValor):
        global temp_file
        self.igualData = False
        self.data['Proyectos'][indProyecto][3].append([tituloValor, descValor, []])
        self.data['Proyectos'][indProyecto][2] = len(self.data['Proyectos'][indProyecto][3])-1
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Elimina Trabajo ----
    def eliminaTrabajo(self, indProyecto, indTrabajo):
        global temp_file
        self.igualData = False
        # ---- Hace que el trabajo seleccionado siga seleccionado si se borra un trabajo anterior ----
        if self.data['Proyectos'][indProyecto][2] > 0 and self.data['Proyectos'][indProyecto][2] >= indTrabajo: self.data['Proyectos'][indProyecto][2] -= 1
        # ---- Elimina el trabajo ----
        del self.data['Proyectos'][indProyecto][3][indTrabajo]
        # ---- Copia el  contenido del diccionario "data" en el JSON TEMP ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Edita Trabajo ----
    def editaTrabajo(self, indProyecto, indTrabajo, titulo, descripcion):
        global temp_file
        self.igualData = False
        self.data['Proyectos'][indProyecto][3][indTrabajo][0] = titulo
        self.data['Proyectos'][indProyecto][3][indTrabajo][1] = descripcion
        # ---- Copia el  contenido del diccionario "data" en el JSON TEMP ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)


    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////////////// TICKETS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Nuevo Ticket ----
    def creaTicket(self, indProyecto, indTrabajo, tipo, titulo, descripcion, items):
        global temp_file
        self.igualData = False
        self.data['Proyectos'][indProyecto][3][indTrabajo][2].append([tipo, titulo, descripcion, items])
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Elimina Ticket ----
    def eliminaTicket(self, indProyecto, indTrabajo, indTicket):
        global temp_file
        self.igualData = False
        del self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket]
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Edita Ticket ----
    def editaTicket(self, indProyecto, indTrabajo, indTicket, tipo, titulo, descripcion, items):
        global temp_file
        self.igualData = False
        self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][0] = tipo
        self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][1] = titulo
        self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][2] = descripcion
        self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][3] = items
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    # ---- Duplica Ticket ----
    def copiaTicket(self, indProyecto, indTrabajo, indTicket):
        global temp_file
        self.igualData = False
        # ---- Mete los valores pedidos en una nueva lista temporal ----
        add_data = self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket]
        # ---- Agrega el diccionario temporal "add_data" a mDatos y luego al JSON ----
        self.data['Proyectos'][indProyecto][3][indTrabajo][2].append(add_data)
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)


    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////////// ORDENA LISTA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Re ordena los archivos ----
    def ordenaLista(self, listaCambia, itemCambiado, ubicacionNueva):
        # ---- Quita el item pedido de la lista ----
        elDato = listaCambia.pop(itemCambiado)
        # Agrega el dato en la lista
        listaCambia.insert(ubicacionNueva, elDato)

    def ordenaProyecto(self, itemCambiado, ubicacionNueva):
        global temp_file
        self.igualData = False
        # ---- Metodo que ordena la lista
        self.ordenaLista(self.data['Proyectos'], itemCambiado, ubicacionNueva)
        # ---- Hace que el PROYECTO seleccionado siga seleccionado si se modifica en la posición de la lista ----
        if self.data['Indice'] < itemCambiado and self.data['Indice'] >= ubicacionNueva:
            self.data['Indice'] += 1
        elif self.data['Indice'] > itemCambiado and self.data['Indice'] <= ubicacionNueva:
            self.data['Indice'] -= 1
        elif self.data['Indice'] == itemCambiado:
            self.data['Indice'] = ubicacionNueva
        # ---- Guarda las modificaciones en el archivo temporal a la espera de guardar el proyecto ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    def ordenaTrabajo(self, indProyecto, itemCambiado, ubicacionNueva):
        global temp_file
        self.igualData = False
        # ---- Metodo que ordena la lista
        self.ordenaLista(self.data['Proyectos'][indProyecto][3], itemCambiado, ubicacionNueva)
        # ---- Hace que el TRABAJO seleccionado siga seleccionado si se modifica en la posición de la lista ----
        if self.data['Proyectos'][indProyecto][2] < itemCambiado and self.data['Proyectos'][indProyecto][2] >= ubicacionNueva:
                self.data['Proyectos'][indProyecto][2] += 1
        elif self.data['Proyectos'][indProyecto][2] > itemCambiado and self.data['Proyectos'][indProyecto][2] <= ubicacionNueva:
            self.data['Proyectos'][indProyecto][2] -= 1
        elif self.data['Proyectos'][indProyecto][2] == itemCambiado:
            self.data['Proyectos'][indProyecto][2] = ubicacionNueva
        # ---- Guarda las modificaciones en el archivo temporal a la espera de guardar el proyecto ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)

    def ordenaTicket(self, indProyecto, indTrabajo, itemCambiado, ubicacionNueva):
        global temp_file
        self.igualData = False
        # ---- Metodo que ordena la lista
        self.ordenaLista(self.data['Proyectos'][indProyecto][3][indTrabajo][2], itemCambiado, ubicacionNueva)
        # ---- Guarda las modificaciones en el archivo temporal a la espera de guardar el proyecto ----
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)


    # ------------------------------------------------------------------------------------------------------------------
    # ///////////////////////////////////////////////////// ITEMS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Nuevo Item ----
    def creaItem(self, indProyecto, indTrabajo, indTicket, items):
        self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][3].append(items)

    # ---- Modifica los CheckBox de los Ticket ----
    def checkItem(self, indProyecto, indTrabajo, indTicket, indItem, valor):
        global temp_file
        self.igualData = False
        if valor == 1:
            self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][3][indItem][0] = 0
        else:
            self.data['Proyectos'][indProyecto][3][indTrabajo][2][indTicket][3][indItem][0] = 1
        with open(temp_file, 'w') as f:
            json.dump(self.data, f, indent=tabulacion)


    # ---- Resetea el diccionario "data" cargandole los valores del archivo "temp_file" ----
    def resetData(self):
        with open(temp_file, 'r') as f:
            self.data = json.load(f)


    # ------------------------------------------------------------------------------------------------------------------
    # ////////////////////////////////////////////////// DATA GENERAL \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ------------------------------------------------------------------------------------------------------------------
    # ---- Carga los datos iniciales del archivo "init_file" para usar en el seteo inicial del programa ----
    def iniciaData(self):
        with open(init_file, encoding="utf-8") as f:
            self.dataInicial = json.load(f)

    # ---- Guarda en el archivo "init_file" la posición X e Y de la ventana ----
    def guardaPos(self, posicionX, posicionY):
        self.dataInicial['PosWindow'][0] = posicionX
        self.dataInicial['PosWindow'][1] = posicionY
        with open(init_file, 'w') as f:
            json.dump(self.dataInicial, f, indent=tabulacion)

    # ---- Guarda en el archivo "init_file" la posición X e Y de la ventana ----
    def guardaMedida(self, ancho, alto):
        if ancho < 1600:
            self.dataInicial['MedidaWindow'][0] = ancho
        if alto < 870:
            self.dataInicial['MedidaWindow'][1] = alto
        with open(init_file, 'w') as f:
            json.dump(self.dataInicial, f, indent=tabulacion)


    # ---- Carga los datos iniciales del archivo "init_file" para usar en el seteo inicial del programa ----
    def iniciaSkin(self):
        with open(skin_file) as f:
            self.skins = json.load(f)

    def guardaSkin(self, sValor):
        self.dataInicial['Skin'] = sValor
        with open(init_file, 'w') as f:
            json.dump(self.dataInicial, f, indent=tabulacion)
        self.iniciaSkin()


if __name__ == '__main__':
    app = FileManager()