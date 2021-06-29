from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox, QGridLayout, QLabel, QLineEdit

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino

class VistaMagazzino(QWidget):

    def __init__(self):
        super(VistaMagazzino, self).__init__()

        self.controller = ControlloreMagazzino()

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)

        for ingrediente, qt in self.controller.get_magazzino().items():
            item = QStandardItem()
            item.setText("ingrediente:{} ".format(ingrediente) + "          quantità:{} ".format(qt))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        self.h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        add_layout = QGridLayout()

        self.label_ingrediente = QLabel('<font size="4"> Ingrediente </font>')
        self.ingrediente = QLineEdit()
        add_layout.addWidget(label_ingrediente, 0, 0)
        add_layout.addWidget(self.ingrediente, 0, 1)

        self.label_quantita = QLabel('<font size="4"> Quantità </font>')
        self.quantita = QLineEdit()
        add_layout.addWidget(label_quantita, 1, 0)
        add_layout.addWidget(self.quantita, 1, 1)

        buttons_layout.addLayout(add_layout)

        add_button = QPushButton("Aggiungi ingrediente")
        add_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(add_button)

        edit_button = QPushButton("Modifica ingrediente")
        edit_button.clicked.connect(self.edit_button)
        buttons_layout.addWidget(edit_button)

        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.setLayout(self.h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Magazzino")

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()

    def add_ingrediente(self):
        self.vista_inserisci_ingrediente = VistaInserisciIngrediente(self.controller, self.update_ui)
        self.vista_inserisci_ingrediente.show()

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            ordinazione = self.controller.get_ordinazione_by_index(selected)
            self.vista_ordinazione = VistaOrdinazione(ordinazione)
            self.vista_ordinazione.show()

    def delete_ordinazione(self):
        reply = QMessageBox.question(self, 'Quit', 'Vuoi cancellare l\'ordine?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes and len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            self.controller.elimina_ordinazione(selected)

