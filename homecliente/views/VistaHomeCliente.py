import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QGridLayout, QSpacerItem, QSizePolicy, \
    QMessageBox

from listamenu.views.VistaListaMenuCliente import VistaListaMenuCliente


class VistaHomeCliente(QWidget):
    def __init__(self, nome, tavolo):
        self.nome = nome
        self.tavolo = tavolo
        super(VistaHomeCliente, self).__init__()

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("Home Cliente")
        self.centralwidget.setGeometry(QRect(130, 0, 1600, 1000))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 4px;\n"
                                         "border-color: black;\n")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(400, 100, 1100, 450))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        pixmap = QPixmap('listamenu/data/images/logo_menù.png')
        self.label_2.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(300, 300, 1200, 900))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_menu= QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_menu.setSizePolicy(sizePolicy)
        self.pushButton_menu.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_menu.setMinimumHeight(self.height / 5)
        self.pushButton_menu.setMaximumHeight(self.height / 5)
        self.pushButton_menu.setObjectName("pushButton_cliente")
        self.pushButton_menu.setStyleSheet(" border-radius:22px;\n"
                                              " background-color: rgb(197, 255, 134);\n"
                                              " color:black;\n"
                                              " border-style: outset;\n"
                                              "border-width: 4px;\n"
                                              "border-color: black;\n"
                                              "font: 18pt \\\"Eras Demi ITC\\\";")

        self.gridLayout_2.addWidget(self.pushButton_menu, 0, 0, 1, 1)
        self.setWindowTitle("Home Cliente")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(QCoreApplication.translate("HomeCliente",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Visualizza, scegli e ordina!</span></p></body></html>"))

        self.pushButton_menu.setText(QCoreApplication.translate("HomeCliente", "Visualizza Menu"))
        self.pushButton_menu.clicked.connect(self.go_vista_menu)

    def go_vista_menu(self):
        self.vista_menu = VistaListaMenuCliente(self.nome, self.tavolo)
        self.vista_menu.showMaximized()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Attenzione!',
                                     'Vuoi chiudere il programma?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()

