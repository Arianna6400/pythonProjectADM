import sys
from datetime import *
import calendar

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QGridLayout, QPushButton, QVBoxLayout, QListView
from PyQt5.QtCore import QDate

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioni(QWidget):
	global currentYear, currentMonth

	currentMonth = datetime.now().month
	currentYear = datetime.now().year

	def __init__(self):
		super(VistaListaPrenotazioni, self).__init__()
		grid_layout = QGridLayout()
		self.controller = ControlloreListaPrenotazioni()
		self.list_view = QListView()

		self.calendar = QCalendarWidget(self)
		self.calendar.move(20, 20)
		self.calendar.setGridVisible(True)
		self.calendar.setMinimumDate(QDate(currentYear, currentMonth - 1, 1))
		self.calendar.setMaximumDate(QDate(currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth)[1]))

		buttons_layout = QVBoxLayout()
		add_button = QPushButton("Aggiungi prenotazione")
		add_button.clicked.connect(self.aggiungi_prenotazione)
		buttons_layout.addWidget(add_button)



		grid_layout.addWidget(self.calendar, 0, 0)
		grid_layout.addLayout(buttons_layout, 0, 1)
		grid_layout.addWidget(self.list_view, 1, 0)

		self.calendar.setSelectedDate(QDate(currentYear, currentMonth, 1))

		self.calendar.clicked.connect(self.printInfo)
		self.resize(600, 400)
		self.setWindowTitle('Lista Prenotazioni')
		self.setLayout(grid_layout)

	def printInfo(self, qDate):
		print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
		print(f'Day Number of the year: {qDate.dayOfYear()}')
		print(f'Day Number of the week: {qDate.dayOfWeek()}')

		self.listview_model = QStandardItemModel(self.list_view)
		item = QStandardItem()
		item.setFont(QFont('DejaVu Sans Mono', 10))
		item.setText("{0:<15}{1:<12}{2:<10}{3}".format("Nome: ", "Telefono:", "Persone:", "Orario:"))
		item.setEditable(False)
		font = item.font()
		font.setPointSize(12)
		item.setFont(font)
		self.listview_model.appendRow(item)

		for prenotazione in self.controller.get_prenotazioni_by_data(datetime(qDate.year(), qDate.month(), qDate.day())):
			item = QStandardItem()
			item.setFont(QFont('DejaVu Sans Mono', 10))
			item.setText("{0:<15}{1:<12}{2:<10}{3}".format(prenotazione.nome, prenotazione.telefono, prenotazione.num_persone, prenotazione.data.hour))
			item.setEditable(False)
			font = item.font()
			font.setPointSize(12)
			item.setFont(font)
			self.listview_model.appendRow(item)
		self.list_view.setModel(self.listview_model)

	def aggiungi_prenotazione(self):
		self.vista_aggiungi_prenotazione = VistaPrenotazione(self.controller)
		self.vista_aggiungi_prenotazione.show()



