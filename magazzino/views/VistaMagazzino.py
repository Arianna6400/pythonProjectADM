from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QFont

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino


class VistaMagazzino(QWidget):

    def __init__(self):
        super(VistaMagazzino, self).__init__()

        self.controller = ControlloreMagazzino()

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()

        self.update_ui()

        self.h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        add_layout = QGridLayout()

        self.label_ingrediente = QLabel('<font size="4"> Ingrediente </font>')
        self.ingrediente = QLineEdit()
        add_layout.addWidget(self.label_ingrediente, 0, 0)
        add_layout.addWidget(self.ingrediente, 0, 1)

        self.label_quantita = QLabel('<font size="4"> Quantità </font>')
        self.quantita = QLineEdit()
        add_layout.addWidget(self.label_quantita, 1, 0)
        add_layout.addWidget(self.quantita, 1, 1)

        buttons_layout.addLayout(add_layout)

        add_button = QPushButton("Aggiungi ingrediente")
        add_button.clicked.connect(self.add_ingrediente)
        buttons_layout.addWidget(add_button)

        edit_button = QPushButton("Modifica ingrediente")
        edit_button.clicked.connect(self.edit_ingrediente)
        buttons_layout.addWidget(edit_button)

        delete_button = QPushButton("Elimina ingrediente")
        delete_button.clicked.connect(self.delete_ingrediente)
        buttons_layout.addWidget(delete_button)

        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.setLayout(self.h_layout)
        self.resize(1200, 400)
        self.setWindowTitle("Magazzino")

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()

    def add_ingrediente(self):
        if not self.ingrediente.text() == "" or self.quantita.text() == "":
            self.controller.add_ingrediente(self.ingrediente.text(), float(self.quantita.text()))
            self.update_ui()

    def edit_ingrediente(self):
        if not self.ingrediente.text() == "" or self.quantita.text() == "":
            self.controller.edit_ingrediente(self.ingrediente.text(), float(self.quantita.text()))
            self.update_ui()

    def delete_ingrediente(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            self.controller.delete_ingrediente(selected)
        self.update_ui()

    def update_ui(self):
        self.controller.sort()
        self.listview_model = QStandardItemModel(self.list_view)
        for ingrediente, qt in self.controller.get_magazzino().items():
            item = QStandardItem()
            item.setFont(QFont('DejaVu Sans Mono', 10))
            item.setText("ingrediente:{0:<20}{1:>20} ".format(ingrediente, qt))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


