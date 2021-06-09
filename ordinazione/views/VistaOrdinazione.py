from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView

from ordinazione.controller.ControlloreOrdinazione import ControlloreOrdinazione


class VistaOrdinazione(QWidget):

    def __init__(self, ordinazione):
        super(VistaOrdinazione, self).__init__()

        self.controller = ControlloreOrdinazione(ordinazione)

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for Prodotto in ordinazione.get_ordinazione():
            item = QStandardItem()
            item.setText("{} ".format(Prodotto) + "{} ".format(ordinazione.get_ordinazione()[Prodotto]))
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