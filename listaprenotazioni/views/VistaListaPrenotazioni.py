from datetime import *
import calendar
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QGridLayout, QPushButton, QVBoxLayout, QListView, \
    QLabel
from PyQt5.QtCore import QDate, QRect, QCoreApplication

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioni(QWidget):
    global currentYear, currentMonth

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    def __init__(self):
        super(VistaListaPrenotazioni, self).__init__()

        self.controller = ControlloreListaPrenotazioni()

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaListaPrenotazioni")
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
        self.gridLayoutWidget.setGeometry(QRect(250, 150, 900, 800))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 16pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setMinimumDate(QDate(currentYear, currentMonth - 1, 1))
        self.calendarWidget.setMaximumDate(
            QDate(currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth)[1]))
        self.calendarWidget.setSelectedDate(QDate(currentYear, currentMonth, 1))
        self.calendarWidget.setStyleSheet("background-color: rgb(106, 228, 41);\n"
                                          "font: 10pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.calendarWidget, 1, 0, 1, 1)

        self.listView = QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet("background-color: rgb(197, 255, 134);")
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 1)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1230, 220, 281, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton_add = QPushButton(self.verticalLayoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(8, 8))
        self.pushButton_add.setMinimumHeight(self.height / 10)
        self.pushButton_add.setMaximumHeight(self.height / 10)
        self.pushButton_add.setStyleSheet("border-radius:22px;\n"
                                          "background-color: rgb(197, 255, 134);\n"
                                          "color:black;\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-color: black;\n"
                                          "font: 14pt \"Eras Demi ITC\";")
        self.verticalLayout.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(self.verticalLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(8, 8))
        self.pushButton_delete.setMinimumHeight(self.height / 10)
        self.pushButton_delete.setMaximumHeight(self.height / 10)
        self.pushButton_delete.setStyleSheet("border-radius:22px;\n"
                                             "background-color: rgb(197, 255, 134);\n"
                                             "color:black;\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: black;\n"
                                             "font: 14pt \"Eras Demi ITC\";")
        self.verticalLayout.addWidget(self.pushButton_delete)

        self.setWindowTitle("Lista Prenotazioni")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaListaPrenotazioni",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Controlla le prenotazioni:</span></p></body></html>"))

        self.pushButton_add.setText(QCoreApplication.translate("VistaListaPrenotazioni", "Aggiungi prenotazione"))
        self.pushButton_add.clicked.connect(self.aggiungi_prenotazione)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaListaPrenotazioni", "Elimina prenotazione"))
        self.pushButton_delete.clicked.connect(self.elimina_prenotazione)

        self.calendarWidget.clicked.connect(self.printInfo)

    def printInfo(self, qDate):
        self.data_selezionata = qDate
        self.listview_model = QStandardItemModel(self.listView)
        item = QStandardItem()
        item.setFont(QFont('Eras Demi ITC'))
        item.setText("{0:<15}\t{1:<14}\t\t{2:<12}\t{3}".format("Nome: ", "Telefono:", "Persone:", "Orario:"))
        item.setEditable(False)
        font = item.font()
        font.setPointSize(16)
        item.setFont(font)
        self.listview_model.appendRow(item)

        for prenotazione in self.controller.get_prenotazioni_by_data(
                datetime(qDate.year(), qDate.month(), qDate.day())):
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText(
                "{0:<15}\t{1:<14}\t{2:<12}\t{3}".format(prenotazione.nome, prenotazione.telefono,
                                                        prenotazione.num_persone, prenotazione.data.hour))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(16)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

    def aggiungi_prenotazione(self):
        self.vista_aggiungi_prenotazione = VistaPrenotazione(self.controller)
        self.vista_aggiungi_prenotazione.show()

    def elimina_prenotazione(self):
        selected = self.listView.selectedIndexes()[0].row() - 1
        prenotazione_da_eliminare = self.controller.get_prenotazioni_by_data(
            datetime(self.data_selezionata.year(), self.data_selezionata.month(), self.data_selezionata.day()))[
            selected]
        self.controller.elimina_prenotazione(prenotazione_da_eliminare)

    def closeEvent(self, event):
        self.controller.save_data()
