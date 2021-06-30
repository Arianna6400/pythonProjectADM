from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView


class VistaOrdinazione(QWidget):

    def __init__(self, ordinazione):
        super(VistaOrdinazione, self).__init__()

        self.controller = ordinazione

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for Prodotto, qt in self.controller.get_ordinazione().items():
            item = QStandardItem()
            item.setText("{}, ".format(Prodotto) + "{} ".format(qt))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        self.h_layout.addWidget(self.list_view)
        self.setLayout(self.h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Ordinazione")
