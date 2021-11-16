from datetime import datetime
import calendar

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QGridLayout, QPushButton, QVBoxLayout, QListView
from PyQt5.QtCore import QDate

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioni(QWidget):
    def __init__(self):
        super(VistaListaPrenotazioni, self).__init__()

        self.currentMonth = datetime.now().month  # da datetime prendiamo il mese attuale
        self.currentYear = datetime.now().year  # da datetime prendiamo l'anno attuale

        self.controller = ControlloreListaPrenotazioni()  # inizializziamo il controller a un controllore lista
        # prenotazione che contiene le prenotazioni presenti fino inseriti fino alla data attuale
        self.vista_aggiungi_prenotazione = VistaPrenotazione(self.controller)  # inizializziamo la vista per
        # inserire una nuova prenotazione in caso sia neccesario

        grid_layout = QGridLayout()
        self.list_view = QListView()

        self.calendar = QCalendarWidget(self)  # widget calendario per gestire in modo più semplice le prenotazioni
        # presenti
        self.calendar.move(20, 20)
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumDate(QDate(self.currentYear, self.currentMonth - 1, 1))
        self.calendar.setMaximumDate(QDate(self.currentYear, self.currentMonth + 1,
                                           calendar.monthrange(self.currentYear, self.currentMonth)[1]))
        self.calendar.setSelectedDate(QDate(self.currentYear, self.currentMonth, 1))
        self.calendar.clicked.connect(self.print_info)

        buttons_layout = QVBoxLayout()
        add_button = QPushButton("Aggiungi prenotazione")
        add_button.clicked.connect(self.aggiungi_prenotazione)
        buttons_layout.addWidget(add_button)

        delete_button = QPushButton("Elimina prenotazione")
        delete_button.clicked.connect(self.elimina_prenotazione)
        buttons_layout.addWidget(delete_button)

        grid_layout.addWidget(self.calendar, 0, 0)
        grid_layout.addLayout(buttons_layout, 0, 1)
        grid_layout.addWidget(self.list_view, 1, 0)

        self.resize(900, 600)
        self.setWindowTitle('Lista Prenotazioni')
        self.setLayout(grid_layout)

    def print_info(self, selected_date):
        self.listview_model = QStandardItemModel(self.list_view)

        item = QStandardItem()
        custom_font = QFont("DejaVu Sans Mono", 10)
        custom_font.setFamily('Monospace')
        custom_font.setFixedPitch(True)
        item.setFont(custom_font)
        item.setText("{0:<15}{1:<12}{2:<10}{3}".format("Nome: ", "Telefono:", "Persone:", "Orario:"))
        item.setEditable(False)
        self.listview_model.appendRow(item)

        for prenotazione in self.controller.get_prenotazioni_by_data(
                datetime(selected_date.year(), selected_date.month(), selected_date.day())):
            item = QStandardItem()
            item.setFont(custom_font)
            item.setText(
                "{0:<15}{1:<12}{2:<10}{3}".format(prenotazione.get_nome(), prenotazione.get_telefono(),
                                                  prenotazione.get_num_persone(), prenotazione.get_data().hour))
            item.setEditable(False)
            self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)

    def aggiungi_prenotazione(self):
        self.vista_aggiungi_prenotazione.show()

    def elimina_prenotazione(self):
        selected = self.list_view.selectedIndexes()[0].row() - 1
        prenotazione_da_eliminare = self.controller.get_prenotazioni_by_data(
            datetime(self.data_selezionata.year(), self.data_selezionata.month(), self.data_selezionata.day()))[
            selected]
        self.controller.elimina_prenotazione(prenotazione_da_eliminare)
