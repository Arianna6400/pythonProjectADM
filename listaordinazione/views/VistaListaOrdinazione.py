from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox

from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione
from ordinazione.views.VistaOrdinazione import VistaOrdinazione


class VistaListaOrdinazione(QWidget):

    def __init__(self):
        super(VistaListaOrdinazione, self).__init__()

        self.controller = ControlloreListaOrdinazione()

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()

        self.update_ui()

        self.h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()

        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        delete_button = QPushButton("Elimina ordine")
        delete_button.clicked.connect(self.delete_ordinazione)
        buttons_layout.addWidget(delete_button)

        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.setLayout(self.h_layout)
        self.resize(800, 400)
        self.setWindowTitle("Lista Ordinazione")

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()

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

        self.update_ui()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)

        for ordinazione in self.controller.get_lista_ordinazione():
            item = QStandardItem()
            fontstd = QFont("DejaVu Sans Mono", 10)
            fontstd.setFamily('Monospace')
            fontstd.setFixedPitch(True)
            item.setFont(fontstd)
            item.setText("{0:<8} tavolo:{1} nome:{2:>10}".format(ordinazione.get_orario(),
                                                                 ordinazione.get_tavolo(), ordinazione.get_nome()))
            item.setEditable(False)
            self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)
