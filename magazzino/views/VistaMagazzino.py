from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QVBoxLayout, QPushButton, QLabel, QGridLayout, QLineEdit

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino


# Questa classe definisce la Vista del magazzino dall'interfaccia Amministratore

class VistaMagazzino(QWidget):

    def __init__(self):
        super(VistaMagazzino, self).__init__()
        self.controller = ControlloreMagazzino()

        # Definizione della parte statica, che comprende il font e la dimensione della finestra

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        # Costruzione del Widget centrale con QtDesigner

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaMagazzino")
        self.centralwidget.setGeometry(QRect(130, 0, 1600, 1000))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 4px;\n"
                                         "border-color: black;\n")

        # Inserimento dello sfondo in background della vista

        self.image = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('listamenu/data/images/irish.jpeg')
        self.image.setPixmap(pixmap)
        self.image.show()
        self.image.setGeometry(QRect(130, 0, 1600, 1000))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Costruzione della griglia principale con layout verticale che contiene la lista dei prodotti in magazzino

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 150, 800, 750))
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

        # Definizione della seconda griglia che contiene i pulsanti di funzionamento e le linee di scrittura per l'inserimento
        # di nuovi ingredienti

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(1130, 200, 481, 750))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Label contenente la linea di scrittura del nome dell'ingrediente

        self.label_ingrediente = QLabel(self.gridLayoutWidget)
        self.label_ingrediente.setObjectName("label_ingrediente")
        self.label_ingrediente.setStyleSheet("font: 16pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.label_ingrediente, 0, 0, 1, 1)

        self.lineEdit_ingrediente = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ingrediente.setObjectName("lineEdit_ingrediente")
        self.lineEdit_ingrediente.setStyleSheet("background-color: white;")
        self.gridLayout.addWidget(self.lineEdit_ingrediente, 0, 1, 1, 1)

        # Label contenente la linea di scrittura delle quantità

        self.label_quantita = QLabel(self.gridLayoutWidget)
        self.label_quantita.setObjectName("label_quantita")
        self.label_quantita.setStyleSheet("font: 16pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.label_quantita, 1, 0, 1, 1)

        self.lineEdit_quantita = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_quantita.setObjectName("lineEdit_quantita")
        self.lineEdit_quantita.setStyleSheet("background-color: white;")
        self.gridLayout.addWidget(self.lineEdit_quantita, 1, 1, 1, 1)

        # Definizione dei pulsanti a lato

        self.pushButton_add = QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(10, 10))
        self.pushButton_add.setMinimumHeight(self.height / 10)
        self.pushButton_add.setMaximumHeight(self.height / 10)
        self.pushButton_add.setStyleSheet("border:2px solid;\n"
                                          "max-height:48px;\n"
                                          "border-top-right-radius:20px;\n"
                                          "border-bottom-left-radius:20px;\n"
                                          "background-color: rgb(242, 242, 242);\n"
                                          " color:black;\n"
                                          " border-style: outset;\n"
                                          "border-width: 4px;\n"
                                          "border-color: black;\n"
                                          "font: 15pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_add, 2, 1, 1, 1)

        self.pushButton_edit = QPushButton(self.gridLayoutWidget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_edit.sizePolicy().hasHeightForWidth())
        self.pushButton_edit.setSizePolicy(sizePolicy)
        self.pushButton_edit.setMinimumSize(QtCore.QSize(10, 10))
        self.pushButton_edit.setMinimumHeight(self.height / 10)
        self.pushButton_edit.setMaximumHeight(self.height / 10)
        self.pushButton_edit.setStyleSheet("border:2px solid;\n"
                                           "max-height:48px;\n"
                                           "border-top-right-radius:20px;\n"
                                           "border-bottom-left-radius:20px;\n"
                                           "background-color: rgb(242, 242, 242);\n"
                                           " color:black;\n"
                                           " border-style: outset;\n"
                                           "border-width: 4px;\n"
                                           "border-color: black;\n"
                                           "font: 15pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_edit, 3, 1, 1, 1)

        self.pushButton_delete = QPushButton(self.gridLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(10, 10))
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
                                             "font: 15pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_delete, 4, 1, 1, 1)

        self.setWindowTitle("Magazzino")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):  # Funzione che connette i pulsanti alle rispettive funzioni
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaMagazzino",
                                                      "<html>"
                                                      "<head/>"
                                                      "<body>"
                                                      "<p align=\"center\">"
                                                      "<span style=\" font-size:25pt; font-weight:600;\">"
                                                      "Visualizza le scorte:"
                                                      "</span>"
                                                      "</p>"
                                                      "</body>"
                                                      "</html>"))  # Codice in formato HTML per la scritta della label

        self.label_ingrediente.setText(QCoreApplication.translate("VistaMagazzino", "Ingrediente"))
        self.label_quantita.setText(QCoreApplication.translate("VistaMagazzino", "Quantità"))

        self.pushButton_add.setText(QCoreApplication.translate("VistaMagazzino", "Aggiungi ingrediente"))
        self.pushButton_add.clicked.connect(self.add_ingrediente)

        self.pushButton_edit.setText(QCoreApplication.translate("VistaMagazzino", "Modifica ingrediente"))
        self.pushButton_edit.clicked.connect(self.edit_ingrediente)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaMagazzino", "Elimina ingrediente"))
        self.pushButton_delete.clicked.connect(self.delete_ingrediente)

    def add_ingrediente(self):  # Funzione che permette d'inserire un nuovo ingrediente dopo aver compilato nome e quantità nelle
        # linee di scrittura
        if not self.lineEdit_ingrediente.text() == "" or self.lineEdit_quantita.text() == "":
            self.controller.add_ingrediente(self.lineEdit_ingrediente.text(), float(self.lineEdit_quantita.text()))
            self.update_ui()

    def edit_ingrediente(self):  # Funzione che permette di modificare un ingrediente dopo aver compilato nome e quantità nelle
        # linee di scrittura
        if not self.lineEdit_ingrediente.text() == "" or self.lineEdit_quantita.text() == "":
            self.controller.edit_ingrediente(self.lineEdit_ingrediente.text(), float(self.lineEdit_quantita.text()))
            self.update_ui()

    def delete_ingrediente(self):  # Funzione che permette di cancellare un ingrediente dalla lista dopo averlo selezionato
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            self.controller.delete_ingrediente(selected)
        self.update_ui()

    def update_ui(self):  # Funzione che aggiorna la lista
        self.controller.sort()
        self.listview_model = QStandardItemModel(self.listView)
        for ingrediente, qt in self.controller.get_magazzino().items():
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText("Ingrediente:{0:<20}\t\t{1} ".format(ingrediente, qt))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(16)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
