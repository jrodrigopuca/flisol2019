from .view import *
from .model import * 
import sys
import cv2 
import numpy as np
import datetime
import matplotlib.pyplot as plt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        # conectar
        self.BtnHOG.clicked.connect(self.clickHOG)
        self.BtnCSC.clicked.connect(self.clickCSC)

        self.Bar.actualizar=actualizar

    def clickHOG(self):
        self.pedirVideo()

    def clickCSC(self):
        self.pedirVideo(False)


    def pedirVideo(self, isHOG=True):
        archivo, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Video", "","(*.mp4;)" )
        detector = Detector(archivo)
        self.Lst.clear()
        bar= self.Bar
        if isHOG:
            detector.detectarHOG("resultados/resultadoHOG.mp4", bar)
        else:
            detector.detectarCSC("resultados/resultadoCSC.mp4", bar)
        self.Lst.addItems(detector.traerEventos())
        
def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()