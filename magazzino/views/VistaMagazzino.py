from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QVBoxLayout, QPushButton, QLabel, QGridLayout, QLineEdit

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino


class VistaMagazzino(QWidget):

    def __init__(self):
        super(VistaMagazzino, self).__init__()
        self.controller = ControlloreMagazzino()

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("VistaMagazzino")
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
        self.verticalLayoutWidget.setGeometry(QRect(250, 150, 800, 750))
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

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(1130, 200, 481, 750))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label_ingrediente = QLabel(self.gridLayoutWidget)
        self.label_ingrediente.setObjectName("label_ingrediente")
        self.label_ingrediente.setStyleSheet("font: 16pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.label_ingrediente,  0, 0, 1, 1)

        self.lineEdit_ingrediente = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ingrediente.setObjectName("lineEdit_ingrediente")
        self.lineEdit_ingrediente.setStyleSheet("background-color: rgb(235, 255, 219);")
        self.gridLayout.addWidget(self.lineEdit_ingrediente, 0, 1, 1, 1)

        self.label_quantita = QLabel(self.gridLayoutWidget)
        self.label_quantita.setObjectName("label_quantita")
        self.label_quantita.setStyleSheet("font: 16pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.label_quantita, 1, 0, 1, 1)

        self.lineEdit_quantita = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_quantita.setObjectName("lineEdit_quantita")
        self.lineEdit_quantita.setStyleSheet("background-color: rgb(235, 255, 219);")
        self.gridLayout.addWidget(self.lineEdit_quantita, 1, 1, 1, 1)

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
        self.pushButton_add.setStyleSheet("border-radius:22px;\n"
                                           "background-color: rgb(197, 255, 134);\n"
                                           "color:black;\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-color: black;\n"
                                           "font: 16pt \"Eras Demi ITC\";")
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
        self.pushButton_edit.setStyleSheet("border-radius:22px;\n"
                                           "background-color: rgb(197, 255, 134);\n"
                                           "color:black;\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-color: black;\n"
                                           "font: 16pt \"Eras Demi ITC\";")
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
        self.pushButton_delete.setStyleSheet("border-radius:22px;\n"
                                             "background-color: rgb(197, 255, 134);\n"
                                             "color:black;\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: black;\n"
                                             "font: 16pt \"Eras Demi ITC\";")
        self.gridLayout.addWidget(self.pushButton_delete, 4, 1, 1, 1)

        self.setWindowTitle("Magazzino")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(QCoreApplication.translate("VistaMagazzino",
                                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Visualizza le scorte:</span></p></body></html>"))

        self.label_ingrediente.setText(QCoreApplication.translate("VistaMagazzino","Ingrediente"))
        self.label_quantita.setText(QCoreApplication.translate("VistaMagazzino", "Quantità"))

        self.pushButton_add.setText(QCoreApplication.translate("VistaMagazzino", "Aggiungi ingrediente"))
        self.pushButton_add.clicked.connect(self.add_ingrediente)

        self.pushButton_edit.setText(QCoreApplication.translate("VistaMagazzino", "Modifica ingrediente"))
        self.pushButton_edit.clicked.connect(self.edit_ingrediente)

        self.pushButton_delete.setText(QCoreApplication.translate("VistaMagazzino", "Elimina ingrediente"))
        self.pushButton_delete.clicked.connect(self.delete_ingrediente)

    def add_ingrediente(self):
        if not self.lineEdit_ingrediente.text() == "" or self.lineEdit_quantita.text() == "":
            self.controller.add_ingrediente(self.lineEdit_ingrediente.text(), float(self.lineEdit_quantita.text()))
            self.update_ui()

    def edit_ingrediente(self):
        if not self.lineEdit_ingrediente.text() == "" or self.lineEdit_quantita.text() == "":
            self.controller.edit_ingrediente(self.lineEdit_ingrediente.text(), float(self.lineEdit_quantita.text()))
            self.update_ui()

    def delete_ingrediente(self):
        if len(self.listView.selectedIndexes()) > 0:
            selected = self.listView.selectedIndexes()[0].row()
            self.controller.delete_ingrediente(selected)
        self.update_ui()

    def update_ui(self):
        self.controller.sort()
        self.listview_model = QStandardItemModel(self.listView)
        for ingrediente, qt in self.controller.get_magazzino().items():
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText("Ingrediente:{0:<20}{1:>20} ".format(ingrediente, qt))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(16)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()


