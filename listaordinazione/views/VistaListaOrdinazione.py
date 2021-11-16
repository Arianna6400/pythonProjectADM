from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QVBoxLayout, QPushButton, QLabel, QMessageBox

from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione
from ordinazione.views.VistaOrdinazione import VistaOrdinazione


class VistaListaOrdinazione(QWidget):

    def __init__(self):
        super(VistaListaOrdinazione, self).__init__()

        self.controller = ControlloreListaOrdinazione()

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaListaOrdinazione")
        self.centralwidget.setGeometry(QRect(130, 0, 1600, 1000))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 4px;\n"
                                         "border-color: black;\n")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 150, 900, 750))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 16pt \"Eras Demi ITC\";")
        self.verticalLayout.addWidget(self.label)

        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet("background-color: rgb(235, 255, 219);")
        self.update_ui()
        self.verticalLayout.addWidget(self.listView)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1230, 220, 281, 431))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.pushButton_open = QPushButton(self.verticalLayoutWidget)
        self.pushButton_open.setObjectName("pushButton_open")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        self.pushButton_open.setMinimumSize(QtCore.QSize(8, 8))
        self.pushButton_open.setMinimumHeight(self.height / 10)
        self.pushButton_open.setMaximumHeight(self.height / 10)
        self.pushButton_open.setStyleSheet("border-radius:22px;\n"
                                           "background-color: rgb(197, 255, 134);\n"
                                           "color:black;\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-color: black;\n"
                                           "font: 16pt \"Eras Demi ITC\";")
        self.verticalLayout_2.addWidget(self.pushButton_open)

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
                                          "font: 16pt \"Eras Demi ITC\";")
        self.verticalLayout_2.addWidget(self.pushButton_delete)

        self.setWindowTitle("Lista Ordinazione")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaListaOrdinazione","<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Seleziona l'ordine:</span></p></body></html>"))

        self.pushButton_open.setText(QCoreApplication.translate("VistaListaOrdinazione", "Apri"))
        self.pushButton_open.clicked.connect(self.show_selected_info)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaListaOrdinazione", "Elimina"))
        self.pushButton_delete.clicked.connect(self.delete_ordinazione)

    def show_selected_info(self):
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            ordinazione = self.controller.get_ordinazione_by_index(selected)
            self.vista_ordinazione = VistaOrdinazione(ordinazione)
            self.vista_ordinazione.show()

    def delete_ordinazione(self):
        reply = QMessageBox.question(self, 'Attenzione!',
                                     'Vuoi cancellare questo ordine?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes and len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            self.controller.elimina_ordinazione(selected)
        self.update_ui()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.listView)

        for ordinazione in self.controller.get_lista_ordinazione():
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText("Nome:{} ".format(ordinazione.get_nome()) +
                         "Tavolo:{} ".format(ordinazione.get_tavolo()))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)