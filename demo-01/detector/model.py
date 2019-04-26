import numpy as np
import cv2
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets

def actualizar(self, val):
    #print(val)
    self.setValue(val)

class Detector:    
    def __init__(self, entradaDir):
        self.entrada= entradaDir
        self.eventos =[]


    def traerEventos(self):
        return list(self.eventos)

    def metHOG(self, metodo, imagen, seg):
        rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # Capturo los puntos en donde posiblemente se encuentre la persona
        rects, weights = metodo.detectMultiScale(
            rgb, winStride=(16, 16), padding=(32, 32))

        # Dibujo rectángulo
        for i, (x, y, w, h) in enumerate(rects):
            cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 10)
            fuente = cv2.FONT_HERSHEY_SIMPLEX
            peso = weights[i]
            if (weights[i] > 0):
                self.eventos.append(f'[INFO] Segundo {seg}: Encontró algo!')
            y2 = x - 15 if x - 15 > 15 else x + 15
            cv2.putText(imagen, str(peso), (h, y2),
                        fuente, 0.75, (0, 255, 0), 2)
        return imagen

    def detectarHOG(self, salidaDir, barra):
        video = cv2.VideoCapture(self.entrada)
        fps = video.get(cv2.CAP_PROP_FPS)
        codec =cv2.VideoWriter_fourcc(*'XVID')
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        cantidad = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        self.eventos=[]
        #tiempo = datetime.datetime.now()
        i = 0     # num de frame
        seg = 0   # segundos
        #self.agregarAvances(0)
        actualizar(barra, 0)

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        nuevoVideo = cv2.VideoWriter(salidaDir,codec,fps,size)

        success, frame = video.read()
        self.eventos.append('[INFO] Inicio método HOG')
        while success:
            i += 1
            #self.agregarAvances(int(i*100/cantidad))  # mostrar avance
            actualizar(barra, int(i*100/cantidad))
            if (i % fps == 0):
                seg += 1
            if frame.size != 0:
                frame = self.metHOG(hog, frame, seg)
                nuevoVideo.write(frame)
            success, frame = video.read()
        
        nuevoVideo.release()
        video.release()
        self.eventos.append('[INFO] Fin')

    def metCSC(self,metodo, imagen, seg):
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        rects = metodo.detectMultiScale(gris)

        for (x,y,w,h) in rects:
            cv2.rectangle(imagen, (x, y), (x+w,y+h),(0,255,0),2)
            self.eventos.append(f'[INFO] Segundo {seg}: Encontró algo!')
        return imagen

    def detectarCSC(self,salidaDir, barra):
        #TO DO: Refactoring
        video = cv2.VideoCapture(self.entrada)
        fps = video.get(cv2.CAP_PROP_FPS)
        codec =cv2.VideoWriter_fourcc(*'XVID')
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        cantidad = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        self.eventos=[]
        #tiempo = datetime.datetime.now()
        i = 0     # num de frame
        seg = 0   # segundos
        actualizar(barra, 0)

        cascada=cv2.CascadeClassifier(os.path.join('detector/body.xml'))

        nuevoVideo = cv2.VideoWriter(salidaDir,codec,fps,size)

        success, frame = video.read()
        self.eventos.append(f'[INFO] Inicio método cascada')
        while success:
            i += 1
            #self.agregarAvances(int(i*100/cantidad))  # mostrar avance
            actualizar(barra, int(i*100/cantidad))
            if (i % fps == 0):
                seg += 1
            if frame.size != 0:
                frame = self.metCSC(cascada, frame, seg)
                nuevoVideo.write(frame)
            success, frame = video.read()
        self.eventos.append(f'[INFO] Fin')
        nuevoVideo.release()
        video.release()
        


