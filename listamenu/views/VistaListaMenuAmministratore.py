from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QVBoxLayout, QPushButton, QLabel

from listamenu.controller.ControlloreListaMenu import ControlloreListaMenu
from prodotto.views.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.views.VistaProdotto import VistaProdotto


class VistaListaMenuAmministratore(QWidget):

    def __init__(self):
        super(VistaListaMenuAmministratore, self).__init__()

        self.controller = ControlloreListaMenu()

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaListaMenuAmministratore")
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

        self.pushButton_new = QPushButton(self.verticalLayoutWidget)
        self.pushButton_new.setObjectName("pushButton_new")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_new.sizePolicy().hasHeightForWidth())
        self.pushButton_new.setSizePolicy(sizePolicy)
        self.pushButton_new.setMinimumSize(QtCore.QSize(8, 8))
        self.pushButton_new.setMinimumHeight(self.height / 10)
        self.pushButton_new.setMaximumHeight(self.height / 10)
        self.pushButton_new.setStyleSheet("border-radius:22px;\n"
                                          "background-color: rgb(197, 255, 134);\n"
                                          "color:black;\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-color: black;\n"
                                          "font: 16pt \"Eras Demi ITC\";")
        self.verticalLayout_2.addWidget(self.pushButton_new)

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

        self.setWindowTitle("Menù Amministratore")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaListaMenuAmministratore",
                                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Seleziona il prodotto:</span></p></body></html>"))

        self.pushButton_open.setText(QCoreApplication.translate("VistaListaMenuAmministratore", "Apri"))
        self.pushButton_open.clicked.connect(self.show_selected_info)

        self.pushButton_new.setText(QCoreApplication.translate("VistaListaMenuAmministratore", "Nuovo"))
        self.pushButton_new.clicked.connect(self.add_info)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaListaMenuAmministratore", "Elimina"))
        self.pushButton_delete.clicked.connect(self.delete_selected_info)

    def show_selected_info(self):
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
            self.vista_prodotto = VistaProdotto(prodotto_selezionato)
            self.vista_prodotto.show()

    def delete_selected_info(self):
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
            self.controller.elimina_prodotto(prodotto_selezionato)
            self.update_ui()
            self.verticalLayout.replaceWidget(self.listView, self.listView)

    def add_info(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.update_ui)
        self.vista_inserisci_prodotto.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.listView)
        for prodotto in self.controller.get_lista_menu():
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText(prodotto.prodotto + " {}".format(prodotto.prezzo) + "€")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()