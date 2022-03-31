from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QVBoxLayout, QPushButton, QLabel, QMessageBox

from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione
from ordinazione.views.VistaOrdinazione import VistaOrdinazione

#Questa classe definisce la Vista delle ordinazioni dall'interfaccia Amministratore

class VistaListaOrdinazione(QWidget):

    def __init__(self):
        super(VistaListaOrdinazione, self).__init__()

        self.controller = ControlloreListaOrdinazione()

        # Definizione della parte statica, che comprende il font e la dimensione della finestra

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        # Costruzione del Widget centrale con QtDesigner

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaListaOrdinazione")
        self.centralwidget.setGeometry(QRect(130, 0, 1600, 1000))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 4px;\n"
                                         "border-color: black;\n")

        # Inserimento dello sfondo in background della vista

        self.image = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('listamenu/data/images/birra.jpeg')
        self.image.setPixmap(pixmap)
        self.image.show()
        self.image.setGeometry(QRect(130, 0, 1600, 1000))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Costruzione della griglia principale con layout verticale che contiene la lista delle ordinazioni

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 150, 900, 750))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Label in cima alla lista contenente una scritta

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: \"Eras Demi ITC\";")
        self.verticalLayout.addWidget(self.label)

        # Definizione della lista

        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet("background-color: rgb(209, 207, 207);")
        self.update_ui()
        self.verticalLayout.addWidget(self.listView)

        # Definizione della seconda griglia verticale che contiene i pulsanti di funzionamento

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1230, 220, 281, 431))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Definizione dei pulsanti a lato

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
        self.pushButton_open.setStyleSheet("border:2px solid;\n"
                                            "max-height:48px;\n"
                                            "border-top-right-radius:20px;\n"
                                            "border-bottom-left-radius:20px;\n"
                                            "background-color: rgb(242, 242, 242);\n"
                                            " color:black;\n"
                                            " border-style: outset;\n"
                                            "border-width: 4px;\n"
                                            "border-color: black;\n"
                                            "font: 18pt \\\"Eras Demi ITC\\\";")
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
        self.pushButton_delete.setStyleSheet("border:2px solid;\n"
                                            "max-height:48px;\n"
                                            "border-top-right-radius:20px;\n"
                                            "border-bottom-left-radius:20px;\n"
                                            "background-color: rgb(242, 242, 242);\n"
                                            " color:black;\n"
                                            " border-style: outset;\n"
                                            "border-width: 4px;\n"
                                            "border-color: black;\n"
                                            "font: 18pt \\\"Eras Demi ITC\\\";")
        self.verticalLayout_2.addWidget(self.pushButton_delete)

        self.setWindowTitle("Lista Ordinazione")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #Funzione che connette i pulsanti alle rispettive funzioni
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaListaOrdinazione",
                                                      "<html>"
                                                      "<head/>"
                                                      "<body>"
                                                      "<p align=\"center\">"
                                                      "<span style=\" font-size:25pt; font-weight:600;\">"
                                                      "Seleziona l'ordine:"
                                                      "</span>"
                                                      "</p>"
                                                      "</body>"
                                                      "</html>")) #Codice in formato HTML per la scritta del label

        self.pushButton_open.setText(QCoreApplication.translate("VistaListaOrdinazione", "Apri"))
        self.pushButton_open.clicked.connect(self.show_selected_info)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaListaOrdinazione", "Elimina"))
        self.pushButton_delete.clicked.connect(self.delete_ordinazione)

    def show_selected_info(self): #Funzione che permette di aprire un elemento selezionato
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            ordinazione = self.controller.get_ordinazione_by_index(selected)
            self.vista_ordinazione = VistaOrdinazione(ordinazione)
            self.vista_ordinazione.show()

    def delete_ordinazione(self): #Funzione che permette di eliminare un elemento selezionato
        reply = QMessageBox.question(self, 'Attenzione!',
                                     'Vuoi cancellare questo ordine?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes and len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            self.controller.elimina_ordinazione(selected)
        self.update_ui()

    def update_ui(self): #Funzione che aggiorna la lista
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

    def closeEvent(self, event):
        self.controller.save_data()