import sys

# ---- Importa los modulos que estan dentro del directorio "data" ----
sys.path.insert(0, '/data/')
from data import fileManager
fileManager = fileManager.FileManager()
from data import gui_MainWindow, gui_MenuBotones, gui_Reloj, gui_ProyectoBoton, gui_TrabajoBoton, gui_Spacers, gui_Ticket, gui_Dialogos, gui_Splash

# mainWindow = gui_MainWindow.Ui_MainWindow()
mainWindow = gui_MainWindow

class Organizete():
    def __init__(self):
        mainWindow.Ui_MainWindow()



if __name__ == '__main__':
    app = Organizete()