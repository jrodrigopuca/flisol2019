# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:/flisol2019/demo-01/detector/view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 329)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnHOG = QtWidgets.QPushButton(self.centralwidget)
        self.BtnHOG.setGeometry(QtCore.QRect(20, 30, 181, 21))
        self.BtnHOG.setObjectName("BtnHOG")
        self.Lst = QtWidgets.QListWidget(self.centralwidget)
        self.Lst.setGeometry(QtCore.QRect(20, 110, 381, 171))
        self.Lst.setObjectName("Lst")
        self.Bar = QtWidgets.QProgressBar(self.centralwidget)
        self.Bar.setGeometry(QtCore.QRect(20, 70, 381, 23))
        self.Bar.setProperty("value", 0)
        self.Bar.setObjectName("Bar")
        self.BtnCSC = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCSC.setGeometry(QtCore.QRect(220, 30, 181, 23))
        self.BtnCSC.setObjectName("BtnCSC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detector"))
        self.BtnHOG.setText(_translate("MainWindow", "Buscar por HOG"))
        self.BtnCSC.setText(_translate("MainWindow", "Buscar por Cascada"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

