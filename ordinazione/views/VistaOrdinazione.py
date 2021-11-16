from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView


class VistaOrdinazione(QWidget):

    def __init__(self, ordinazione):
        super(VistaOrdinazione, self).__init__()

        self.controller = ordinazione

        self.setWindowTitle('Vista Ordinazione')
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb(235, 255, 219);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 581, 581))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet("background-color: rgb(235, 255, 219);")
        self.update_ui()
        self.horizontalLayout.addWidget(self.listView)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.listView)

        for Prodotto, qt in self.controller.get_ordinazione().items():
            item = QStandardItem()
            item.setFont(QFont('Eras Demi ITC'))
            item.setText("{}, ".format(Prodotto) + "{} ".format(qt))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)
