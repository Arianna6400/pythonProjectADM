from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QVBoxLayout, QPushButton, QLabel, QMessageBox

from listamenu.controller.ControlloreListaMenu import ControlloreListaMenu
from ordinazione.controller.ControlloreOrdinazione import ControlloreOrdinazione
from ordinazione.model.Ordinazione import Ordinazione
from ordinazione.views.VistaOrdinazione import VistaOrdinazione
from prodotto.controller.ControlloreProdotto import ControlloreProdotto
from prodotto.views.VistaProdotto import VistaProdotto


# Questa classe definisce la Vista del Menu dall'interfaccia Cliente

class VistaListaMenuCliente(QWidget):

    def __init__(self, nome, tavolo):

        super(VistaListaMenuCliente, self).__init__()

        self.controller = ControlloreListaMenu()
        self.ordinazione = ControlloreOrdinazione(Ordinazione(nome, tavolo), self.controller)
        self.controller.update()

        # Definizione della parte statica, che comprende il font e la dimensione della finestra

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        # Costruzione del Widget centrale con QtDesigner

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaListaMenuCliente")
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

        # Costruzione della griglia principale con layout verticale che contiene la lista del menu

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
        self.verticalLayoutWidget_2.setGeometry(QRect(1230, 150, 281, 750))
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
        self.pushButton_open.setMinimumSize(QtCore.QSize(5, 5))
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

        self.pushButton_order = QPushButton(self.verticalLayoutWidget)
        self.pushButton_order.setObjectName("pushButton_order")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_order.sizePolicy().hasHeightForWidth())
        self.pushButton_order.setSizePolicy(sizePolicy)
        self.pushButton_order.setMinimumSize(QtCore.QSize(5, 5))
        self.pushButton_order.setMinimumHeight(self.height / 10)
        self.pushButton_order.setMaximumHeight(self.height / 10)
        self.pushButton_order.setStyleSheet("border:2px solid;\n"
                                            "max-height:48px;\n"
                                            "border-top-right-radius:20px;\n"
                                            "border-bottom-left-radius:20px;\n"
                                            "background-color: rgb(242, 242, 242);\n"
                                            " color:black;\n"
                                            " border-style: outset;\n"
                                            "border-width: 4px;\n"
                                            "border-color: black;\n"
                                            "font: 18pt \\\"Eras Demi ITC\\\";")
        self.verticalLayout_2.addWidget(self.pushButton_order)

        self.pushButton_delete = QPushButton(self.verticalLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(5, 5))
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

        self.pushButton_view = QPushButton(self.verticalLayoutWidget)
        self.pushButton_view.setObjectName("pushButton_add")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_view.sizePolicy().hasHeightForWidth())
        self.pushButton_view.setSizePolicy(sizePolicy)
        self.pushButton_view.setMinimumSize(QtCore.QSize(5, 5))
        self.pushButton_view.setMinimumHeight(self.height / 10)
        self.pushButton_view.setMaximumHeight(self.height / 10)
        self.pushButton_view.setStyleSheet("border:2px solid;\n"
                                           "max-height:48px;\n"
                                           "border-top-right-radius:20px;\n"
                                           "border-bottom-left-radius:20px;\n"
                                           "background-color: rgb(242, 242, 242);\n"
                                           " color:black;\n"
                                           " border-style: outset;\n"
                                           "border-width: 4px;\n"
                                           "border-color: black;\n"
                                           "font: 18pt \\\"Eras Demi ITC\\\";")
        self.verticalLayout_2.addWidget(self.pushButton_view)

        self.pushButton_check = QPushButton(self.verticalLayoutWidget)
        self.pushButton_check.setObjectName("pushButton_check")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_check.sizePolicy().hasHeightForWidth())
        self.pushButton_check.setSizePolicy(sizePolicy)
        self.pushButton_check.setMinimumSize(QtCore.QSize(5, 5))
        self.pushButton_check.setMinimumHeight(self.height / 10)
        self.pushButton_check.setMaximumHeight(self.height / 10)
        self.pushButton_check.setStyleSheet("border:2px solid;\n"
                                            "max-height:48px;\n"
                                            "border-top-right-radius:20px;\n"
                                            "border-bottom-left-radius:20px;\n"
                                            "background-color: rgb(242, 242, 242);\n"
                                            " color:black;\n"
                                            " border-style: outset;\n"
                                            "border-width: 4px;\n"
                                            "border-color: black;\n"
                                            "font: 18pt \\\"Eras Demi ITC\\\";")
        self.verticalLayout_2.addWidget(self.pushButton_check)

        self.setWindowTitle("Menù Cliente")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):  # Funzione che connette i pulsanti alle rispettive funzioni
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaListaMenuCliente",
                                                      "<html>"
                                                      "<head/>"
                                                      "<body>"
                                                      "<p align=\"center\">"
                                                      "<span style=\" font-size:25pt; font-weight:600;\">"
                                                      "Seleziona il prodotto:"
                                                      "</span>"
                                                      "</p>"
                                                      "</body>"
                                                      "</html>"))  # Codice in formato HTML per la scritta della label

        self.pushButton_open.setText(QCoreApplication.translate("VistaListaMenuCliente", "Apri"))
        self.pushButton_open.clicked.connect(self.show_selected_info)

        self.pushButton_order.setText(QCoreApplication.translate("VistaListaMenuCliente", "Aggiungi Ordine"))
        self.pushButton_order.clicked.connect(self.add_ordinazione)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaListaMenuCLiente", "Elimina Ordine"))
        self.pushButton_delete.clicked.connect(self.delete_ordinazione)

        self.pushButton_view.setText(QCoreApplication.translate("VistaListaMenuCliente", "Visualizza Ordine "))
        self.pushButton_view.clicked.connect(self.view_ordinazione)

        self.pushButton_check.setText(QCoreApplication.translate("VistaListaMenuCliente", "Conferma Ordine"))
        self.pushButton_check.clicked.connect(self.check_ordinazione)

    def show_selected_info(self):  # Funzione che permette di aprire un elemento selezionato
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
            self.vista_prodotto = VistaProdotto(prodotto_selezionato)
            self.vista_prodotto.show()

    def update_ui(self):  # Funzione che aggiorna la lista
        self.listview_model = QStandardItemModel(self.listView)
        for ProdottoSingolo in self.controller.get_lista_menu():
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText("{} ".format(ProdottoSingolo.prodotto) + "{}€".format(ProdottoSingolo.prezzo))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

    def add_ordinazione(self):  # Funzione che permette di aggiungere un elemento selezionato all'ordine
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
            if not self.ordinazione.inserisci_prodotto(ControlloreProdotto(prodotto_selezionato)):
                msg = QMessageBox()
                msg.setWindowTitle("Attenzione!")
                msg.setText('Prodotto non disponibile!')
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal,
                               QtGui.QIcon.On)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec_()

    def delete_ordinazione(self):  # Funzione che cancella l'intera lista dell'ordinazione effettuata
        reply = QMessageBox.question(self, 'Attenzione!',
                                     'Vuoi cancellare questo ordine?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ordinazione.elimina_ordinazione()

    def view_ordinazione(self):  # Funzione che permette di visualizzare la lista dell'ordinazione effettuata

        if self.ordinazione.get_ordinazione():
            self.vista_ordinazione = VistaOrdinazione(self.ordinazione)
            self.vista_ordinazione.show()
        else:
            msg = QMessageBox()
            msg.setText('Ordine vuoto')
            msg.setWindowTitle("Attenzione!")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal,
                           QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

    def check_ordinazione(self):  # Funzione che controlla se la lista è vuota o meno, permettendo ci confermare l'ordinazione
        if len(self.ordinazione.get_ordinazione()) == 0:
            msg = QMessageBox()
            msg.setText('Ordine vuoto')
            msg.setWindowTitle("Attenzione!")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal,
                           QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        else:
            self.ordinazione.conferma_ordinazione()
            msg = QMessageBox()
            msg.setText('Ordine confermato!')
            msg.setWindowTitle("Avviso")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal,
                           QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
            self.close()
