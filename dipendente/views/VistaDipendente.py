from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, controllore, callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = dipendente  # controllore del dipendente singolo
        self.controllore_lista_dipendenti = controllore  # controllore della lista dei dipendenti
        self.callback = callback  # callback per aggiornare la vista in caso si elimini un dipendente

        v_layout = QVBoxLayout()

        # parte del codice per visualizzare i dati del dipendente selezionato
        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("ID: {}".format(self.controller.get_id_dipendente())))
        v_layout.addWidget(self.get_info("Codice Fiscale: {}".format(self.controller.get_cf_dipendente())))
        v_layout.addWidget(self.get_info("Data Nascita: {}".format(self.controller.get_data_nascita_dipendente())))
        v_layout.addWidget(self.get_info("Luogo Nascita: {}".format(self.controller.get_luogo_nascita_dipendente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_dipendente())))
        v_layout.addWidget(self.get_info("Ruolo: {}".format(self.controller.get_ruolo_dipendente())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        delete_button = QPushButton("Elimina")  # bottone nel caso si voglia eliminare un dipendente
        delete_button.clicked.connect(self.elimina_dipendente)
        v_layout.addWidget(delete_button)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_dipendente())

    @staticmethod
    def get_info(text):  # metodo statico che dato una stringa crea una label per tale stringa
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente(self):  # metodo per eliminare un dipendente dalla lista dei dipendenti
        self.controllore_lista_dipendenti.elimina_dipendente_by_id(self.controller.get_id_dipendente())
        self.callback()
        self.close()
