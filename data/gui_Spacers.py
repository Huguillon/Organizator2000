from PyQt5.Qt import *

class Ui_Spacers(object):
    def spacer(self, ancho, alto, layoutContainer):
        # ---- AGREGA UN "Spacer" PARA ALINEAR LA LISTA DE BOTONES A LA PARTE SUPERIOR DEL CONTENEDOR DE LA BOTONERA ----
        elSpacerV = QSpacerItem(ancho, alto, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        layoutContainer.addItem(elSpacerV)

    def spacerTickets(self, ancho, alto, layoutContainer, f, c):
        # ---- AGREGA UN "Spacer" PARA ALINEAR LOS TICKETS A LA PARTE SUPERIOR IZQUIERDA DEL CONTENEDOR DE TICKETS ----
        elSpacerV = QSpacerItem(ancho, alto, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        layoutContainer.addItem(elSpacerV, f, c, 1, 1)
