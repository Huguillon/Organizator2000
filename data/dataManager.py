# -*- coding: utf-8 -*-
import json
from pathlib import Path

my_file = Path("Proyecto.json")
data = {}

class ManejaArchivos():
    def __init__(self):
        self.cargaArchivo()

    def cargaArchivo(self):
        if my_file.exists():
            with open(my_file) as f:
                data = json.load(f)
        else:
            # ---- Genera el diccionario Base para meter en el JSON ----
            data = {"Proyectos": [], "Indice": 0}
            # ---- Crea el archivo JSON y le mete los datos del diccionario "data" ----
            with open(my_file, 'w') as f:
                json.dump(data, f, indent=2)
        return data

    # ****************** GUARDA EL VALOR DEL INDICE EN EL ARCHIVO ******************
    def guardaIndice(self, mDatos, vIndice):
        mDatos['Indice'] = vIndice
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************** CREA UN PROYECTO NUEVO EN EL ARCHIVO ******************
    def creaProyecto(self, mDatos, tituloValor, descValor):
        # ---- Agregando nuevos proyectos al archivo ----
        mDatos['Proyectos'].append({"Titulo": tituloValor, "Descripcion": descValor, "Tickets": []})
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************** ELIMINA UN PROYECTO DEL ARCHIVO ******************
    def eliminaProyecto(self, mDatos, indProyecto):
        del mDatos['Proyectos'][indProyecto]
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************** EDITA UN PROYECTO DEL ARCHIVO ******************
    def editaProyecto(self, mDatos, titulo, descripcion, indProyecto):
        mDatos['Proyectos'][indProyecto]['Titulo'] = titulo
        mDatos['Proyectos'][indProyecto]['Descripcion'] = descripcion
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************************************************************************************************
    # ****************** CREA UN TRABAJO NUEVO EN UN PROYECTO Y LO GUARDA EN EL ARCHIVO ******************
    def creaTicket(self, mDatos, tipo, titulo, descripcion, items, indProyecto):
        # ---- Pide valores para agregar al nuevo proyecto ----
        tipoValor = tipo
        tituloValor = titulo
        descValor = descripcion
        itemValor = items
        # ---- Mete los valores pedidos en un nuevo diccionario temporal ----
        add_data = {"Tipo": tipoValor, "Titulo": tituloValor, "Descripcion": descValor, "Items": itemValor}
        # ---- Agrega el diccionario temporal "add_data" a mDatos y luego al JSON ----
        mDatos['Proyectos'][indProyecto]['Tickets'].append(add_data)
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************** ELIMINA UN TRABAJO EN UN PROYECTO Y LO GUARDA EN EL ARCHIVO ******************
    def eliminaTicket(self, mDatos, indProyecto, indTicket):
        # ---- Cuenta la cantidad de proyectos que hay en la archivo JSON ----
        del mDatos['Proyectos'][indProyecto]['Tickets'][indTicket]
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************** EDITA UN TRABAJO EN UN PROYECTO Y LO GUARDA EN EL ARCHIVO ******************
    def editaTicket(self, mDatos, tipo, titulo, descripcion, items, indProyecto, indTicket):
        mDatos['Proyectos'][indProyecto]['Tickets'][indTicket]['Tipo'] = tipo
        mDatos['Proyectos'][indProyecto]['Tickets'][indTicket]['Titulo'] = titulo
        mDatos['Proyectos'][indProyecto]['Tickets'][indTicket]['Descripcion'] = descripcion
        mDatos['Proyectos'][indProyecto]['Tickets'][indTicket]['Items'] = items
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)

    # ****************************************************************************************************************
    # ****************** CREA UN ITEM DENTRO DE UN TRABAJO EN UN PROYECTO Y LO GUARDA EN EL ARCHIVO ******************
    def checkItem(self, mDatos, indProyecto, indTrabajo, indItem, valor):
        if valor == 1:
            mDatos['Proyectos'][indProyecto]['Tickets'][indTrabajo]['Items'][indItem][0] = 0
        else:
            mDatos['Proyectos'][indProyecto]['Tickets'][indTrabajo]['Items'][indItem][0] = 1
        with open(my_file, 'w') as f:
            json.dump(mDatos, f, indent=2)


if __name__ == '__main__':
    app = ManejaArchivos()